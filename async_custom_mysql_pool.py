# -*- coding: utf-8 -*-
# 导入操作系统相关模块
import asyncio
# 日志模块
from loguru import logger
import os
import warnings

# 使用异步MySQL驱动
import aiomysql
import configparser

# 读取数据1
os.getcwd()
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.ini')

config = configparser.ConfigParser()
files_read = config.read(config_path)


#本地
bstcollect_dev = config['collect_dev']

# 忽略唯一索引导致的警告
warnings.filterwarnings('ignore', category=Warning, message=".*Duplicate entry.*")

# 定义一个异步数据库管理类
class DbManager(object):
    def __init__(self, config=2):
        self.pool = None
        self.config = config  # 保存数字参数
        self.fsign = 0  # 0是线程池低连接数，1是协程高连接数：注意只有协程且并发数量高才需要，，否则会耗尽数据库服务器连接数
        # 初始化配置解析器并读取文件
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read(config_path)
        print(f'注意数据库配置——config = {self.config}')

    async def close_pool(self):
        """关闭连接池"""
        if self.pool is not None:
            self.pool.close()
            await self.pool.wait_closed()
            self.pool = None

    def _get_db_config(self):
        """通过数字参数选择数据库配置，实际配置从config.ini读取"""
        config_mapping = {
            0: 'collect_dev',  # 本地环境
        }

        if self.config not in config_mapping:
            raise ValueError(f"无效的数据库配置参数: {self.config}")

        section = config_mapping[self.config]
        if not self.config_parser.has_section(section):
            raise ValueError(f"配置文件中缺少 [{section}] 节")

        try:
            return {
                'host': self.config_parser[section]['hostname'],
                'port': int(self.config_parser[section]['port']),
                'user': self.config_parser[section]['username'],
                'password': self.config_parser[section]['password'],
                'db': self.config_parser[section]['database'],
                'charset': self.config_parser[section]['charset']
            }
        except KeyError as e:
            raise ValueError(f"配置文件中 [{section}] 节缺少必要的配置项: {str(e)}")

    async def __aenter__(self):
        """异步上下文管理器入口"""
        if self.pool is None:
            self.pool_size = {'minsize': 1, 'maxsize': 3} if self.fsign == 0 else {'minsize': 20, 'maxsize': 50}
            try:
                self.pool = await aiomysql.create_pool(
                    minsize=self.pool_size.get('minsize'),
                    maxsize=self.pool_size.get('maxsize'),
                    pool_recycle=300,  # 每5分钟回收连接
                    autocommit=True,
                    **self._get_db_config()
                )
            except Exception as e:
                raise RuntimeError(f"数据库连接失败: {str(e)}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步上下文管理器退出"""
        if self.pool:
           await self.close_pool()

    async def __execute_with_retry(self, func, *args, **kwargs):
        """带重试的异步SQL执行包装器"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                async with self.pool.acquire() as conn:
                    async with conn.cursor(aiomysql.DictCursor) as cur:
                        result = await func(conn, cur, *args, **kwargs)
                        await conn.commit()
                        return result
            except aiomysql.OperationalError as e:
                if attempt == max_retries - 1:
                    raise
                logger.warning(f"数据库操作失败，重试中... ({attempt + 1}/{max_retries}) {e}")
                await asyncio.sleep(1)
                return None
            except Exception as e:
                logger.error(f"数据库操作异常: {str(e)}")
                raise
        return None

    async def execute(self, sql, params=None, exe_many=False):
        """执行SQL语句"""

        async def _exec(conn, cur):
            if exe_many:
                return await cur.executemany(sql, params or ())
            return await cur.execute(sql, params or ())

        return await self.__execute_with_retry(_exec)

    ################################################################
    ################ 以下为封装好的异步执行方法：表、字段方式 ################
    ################################################################

    async def table_insert(self, table, data, on_duplicate=None):
        """
        异步插入单条数据并返回记录的ID，支持重复指定更新操作
        table：表名
        data ：插入数据（字典类型）
        on_duplicate：可选，重复记录处理方式
            - None（默认）：忽略重复记录（INSERT IGNORE）
            - "update"：更新重复记录（ON DUPLICATE KEY UPDATE）
            - 自定义字符串：如 "attempt_count = attempt_count + 1"
            （注意，这里变化差值，只对第一个字段生效，因为是按照书写字段顺序更新，而不是整条同时更新）
            （或者先查询再更新：使用子查询：
                on_duplicate = ""
                    score = VALUES(score),
                    evaluate = VALUES(evaluate),
                    eva_wave = VALUES(evaluate) - (
                        SELECT old.evaluate
                        FROM cdiscount_scores AS old
                        WHERE old.id = cdiscount_scores.id
                    )
                    ""
        """
        if not data:
            logger.warning("table_insert: 插入数据为空，跳过执行")
            return None

        fields = list(data.keys())
        values = [str(data[field]) for field in fields]
        placeholder = ", ".join(["%s"] * len(fields))

        # 构建基础SQL
        if on_duplicate == "update":
            # 不在update_clause的字段不会被修改
            update_clause = ", ".join([f"{field}=VALUES({field})" for field in fields])
            sql = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({placeholder}) ON DUPLICATE KEY UPDATE {update_clause}"
        elif on_duplicate:
            sql = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({placeholder}) ON DUPLICATE KEY UPDATE {on_duplicate}"
        else:
            sql = f"INSERT IGNORE INTO {table} ({', '.join(fields)}) VALUES ({placeholder})"

        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    await cur.execute(sql, values)

                    # 对于ON DUPLICATE场景总是返回记录ID
                    if on_duplicate:
                        if cur.lastrowid:
                            await conn.commit()
                            logger.info(f"插入/更新{table}成功，记录ID: {cur.lastrowid}")
                            return cur.lastrowid
                        else:
                            # 可能是没有自增主键的更新操作
                            await conn.commit()
                            return 0
                    else:
                        # IGNORE模式检测重复
                        if cur.rowcount == 0:
                            # logger.warning(f"插入{table}重复，数据: {data}")
                            return None

                        lastrowid = cur.lastrowid
                        await conn.commit()
                        logger.info(f"插入{table}成功，记录ID: {lastrowid}")
                        return lastrowid
        except Exception as e:
            logger.error(f"插入数据失败: {e}")
            if 'conn' in locals():
                await conn.rollback()
            raise Exception('插入失败')

    async def table_insert_batch(self, table, data, batch_size=200, on_duplicate=None):
        """
                异步批量插入数据
                table：必填，表名
                data ：必填，插入数据列表，每个元素是字典类型
                batch_size：可选，每批处理的数量，默认200
                on_duplicate：可选，重复记录处理方式
                    - None（默认）：忽略重复记录（INSERT IGNORE）
                    - "update"：更新重复记录（ON DUPLICATE KEY UPDATE）
                    - "on_duplicate="attempt_count = attempt_count + 1""：自定义SQL语句
                    （注意，这里变化差值，只对第一个字段生效，因为是按照书写字段顺序更新，而不是整条同时更新）
                    （或者先查询再更新：使用子查询：
                        on_duplicate = ""
                            score = VALUES(score),
                            evaluate = VALUES(evaluate),
                            eva_wave = VALUES(evaluate) - (
                                SELECT old.evaluate
                                FROM cdiscount_scores AS old
                                WHERE old.id = cdiscount_scores.id
                            )
                            ""
                """
        if not data:
            logger.warning("table_insert_batch: 批量插入数据为空，跳过执行")
            return 0

        # 安全处理表名和字段名
        safe_table = f"`{table}`"
        fields = list(data[0].keys())
        safe_fields = [f"`{field}`" for field in fields]
        fields_str = ', '.join(safe_fields)

        # 准备值列表，不再手动加单引号
        values = [[item[field] for field in fields] for item in data]
        placeholder = f"({', '.join(['%s'] * len(fields))})"

        # 构建 SQL
        if on_duplicate == "update":
            update_clause = ", ".join([f"{field}=VALUES({field})" for field in safe_fields])
            base_sql = f"INSERT INTO {safe_table} ({fields_str}) VALUES {placeholder} ON DUPLICATE KEY UPDATE {update_clause}"
        elif on_duplicate:
            base_sql = f"INSERT INTO {safe_table} ({fields_str}) VALUES {placeholder} ON DUPLICATE KEY UPDATE {on_duplicate}"
        else:
            base_sql = f"INSERT IGNORE INTO {safe_table} ({fields_str}) VALUES {placeholder}"

        total_rows_affected = 0

        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    # 分批插入
                    for i in range(0, len(values), batch_size):
                        batch_values = values[i:i + batch_size]
                        batch_placeholders = ', '.join([placeholder] * len(batch_values))
                        batch_sql = base_sql.replace(placeholder, batch_placeholders)
                        flat_values = [item for sublist in batch_values for item in sublist]

                        try:
                            await cur.execute(batch_sql, flat_values)
                            total_rows_affected += cur.rowcount
                        except aiomysql.OperationalError as e:
                            logger.error(f"数据库操作错误: {e}")
                            await conn.rollback()
                            raise
                        except aiomysql.DataError as e:
                            logger.error(f"数据类型错误: {e}")
                            logger.info(flat_values)
                            await conn.rollback()
                            raise
                        except aiomysql.IntegrityError as e:
                            logger.error(f"完整性错误（如唯一约束）: {e}")
                            await conn.rollback()
                            raise
                        except Exception as batch_e:
                            logger.error(f"批量插入批次 {i // batch_size + 1} 失败: {batch_e}")
                            await conn.rollback()
                            raise

                    await conn.commit()
                    return total_rows_affected

        except Exception as e:
            logger.error(f"批量插入整体失败: {e}")
            if 'conn' in locals():
                await conn.rollback()
            raise

    async def table_update(self, **kwargs):
        """
        异步更新数据
        table：必填，表名
        data ：必填，更新数据，字典类型
        where：必填，更新条件
        """
        table = kwargs["table"]
        data = kwargs["data"]
        where = kwargs["where"]
        if not data:
            logger.warning("table_update: 更新数据为空，跳过执行")
            return 0  # 返回0表示没有行被更新

        set_clause = []
        values = []

        for k, v in data.items():
            set_clause.append(f"{k}=%s")
            values.append(str(v))

        sql = f"UPDATE {table} SET {', '.join(set_clause)} WHERE 1=1"

        if isinstance(where, dict):
            for k, v in where.items():
                if isinstance(v, list):
                    sql += f" AND {k} IN ({', '.join(['%s'] * len(v))})"
                    values.extend([str(i) for i in v])
                else:
                    sql += f" AND {k}=%s"
                    values.append(str(v))
        elif isinstance(where, str):
            sql += f" AND {where}"

        sql += ";"
        logger.info(f"SQL: {sql} [参数: {values}]")

        try:
            await self.execute(sql, values)
            async with self.pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    return cur.rowcount
        except Exception as e:
            logger.error(f"更新数据失败: {e}")
            raise

    async def table_update_batch(self, **kwargs):
        """
        异步批量更新数据
        table：必填，表名
        data ：必填，更新数据列表，每个元素是字典类型，必须包含主键字段
        where_key：必填，用于匹配的条件字段名（可以是单个字段或字段列表）
        batch_size：可选，每批处理的数量，默认200

        data={
            'sku_id': '123',  # 主键字段1
            'ymd': '2025-07-30',  # 主键字段2
            'data': {
                'value_heat': 123.45  # 要更新的字段
            }
        }
        where_key=["sku_id", "ymd"],
        batch_size：可选，每批处理的数量，默认200
        """

        table = kwargs["table"]
        data = kwargs["data"]
        where_key = kwargs["where_key"]
        batch_size = kwargs.get("batch_size", 200)

        if not data:
            logger.warning("table_update_batch: 批量更新数据为空，跳过执行")
            return 0

        # 将where_key统一为列表
        if isinstance(where_key, str):
            where_keys = [where_key]
        else:
            where_keys = where_key

        total_affected = 0
        all_fields = list(data[0]['data'].keys())

        # 分批处理
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]

            # 构建批量UPDATE SQL
            set_clauses = []
            params = []

            # 为每个字段构建CASE WHEN表达式
            for field in all_fields:
                case_parts = []
                for item in batch:
                    # 构建WHEN条件：多个字段的条件
                    conditions = []
                    for key in where_keys:
                        conditions.append(f"{key}=%s")
                        params.append(item[key])
                    # 添加THEN值
                    case_parts.append(f"WHEN {' AND '.join(conditions)} THEN %s")
                    params.append(item['data'][field])
                set_clauses.append(f"{field}=CASE {' '.join(case_parts)} ELSE {field} END")

            # 构建WHERE条件（使用OR连接多个条件）
            where_conditions = []
            for item in batch:
                conditions = []
                for key in where_keys:
                    conditions.append(f"{key}=%s")
                    params.append(item[key])
                where_conditions.append(f"({' AND '.join(conditions)})")
            where_clause = " OR ".join(where_conditions)

            # 完整SQL
            sql = f"""
            UPDATE {table} 
            SET {', '.join(set_clauses)}
            WHERE {where_clause}
            """

            logger.debug(f"批量更新SQL: {sql} [参数: {params}]")

            try:
                async with self.pool.acquire() as conn:
                    async with conn.cursor(aiomysql.DictCursor) as cur:
                        await cur.execute(sql, params)
                        total_affected += cur.rowcount
                        await conn.commit()
            except Exception as e:
                logger.error(f"批量更新数据失败: {e}")
                # 可以选择回滚并抛出异常，或者继续处理下一批
                raise

        return total_affected

    async def table_delete(self, **kwargs):
        """
        异步删除数据
        table：必填，表名
        where：必填，删除条件
        """
        table = kwargs["table"]
        where = kwargs["where"]

        sql = f"DELETE FROM {table} WHERE 1=1"
        values = []

        if isinstance(where, dict):
            for k, v in where.items():
                if isinstance(v, list):
                    sql += f" AND {k} IN ({', '.join(['%s'] * len(v))})"
                    values.extend([str(i) for i in v])
                else:
                    sql += f" AND {k}=%s"
                    values.append(str(v))
        elif isinstance(where, str):
            sql += f" AND {where}"

        sql += ";"
        logger.info(f"SQL: {sql} [参数: {values}]")

        try:
            await self.execute(sql, values)
            async with self.pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    return cur.rowcount
        except Exception as e:
            logger.error(f"删除数据失败: {e}")
            raise

    async def table_select(self, sql, params=None):
        """异步执行SQL查询并返回结果
        :param sql: SQL查询语句，使用%s作为占位符
        :param params: 查询参数(tuple/list/dict)
        """
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    if params:
                        await cur.execute(sql, params)  # 使用参数化查询
                    else:
                        await cur.execute(sql)
                    return await cur.fetchall()
        except Exception as e:
            logger.error(f"查询失败: {sql}")
            logger.error(f"参数: {params}")  # 添加参数日志
            logger.error(f"错误信息: {str(e)}")
            raise

    async def table_select_one(self, **kwargs):
        """
        异步查询单条数据
        table：必填，表名
        where：必填，查询条件
        field： 非必填，查询列名
        order： 非必填，排序字段
        sort：  非必填，排序方式
        """
        table = kwargs["table"]
        field = kwargs.get("field", "*")
        where = kwargs["where"]
        order = kwargs.get("order", "")
        sort = kwargs.get("sort", "")

        sql = f"SELECT {field} FROM {table} WHERE 1=1"
        values = []

        if isinstance(where, dict):
            for k, v in where.items():
                if isinstance(v, list):
                    sql += f" AND {k} IN ({', '.join(['%s'] * len(v))})"
                    values.extend([str(i) for i in v])
                else:
                    sql += f" AND {k}=%s"
                    values.append(str(v))
        elif isinstance(where, str):
            sql += f" AND {where}"

        if order:
            sql += f" ORDER BY {order} {sort}"

        sql += " LIMIT 1;"
        logger.info(f"SQL: {sql} [参数: {values}]")

        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    await cur.execute(sql, values)
                    return await cur.fetchone()
        except Exception as e:
            logger.error(f"查询单条数据失败: {e}")
            raise

    async def table_select_many(self, **kwargs):
        """
        异步查询多条数据
        table：必填，表名
        where：必填，查询条件
        field： 非必填，查询列名
        order： 非必填，排序字段
        sort：  非必填，排序方式
        offset：非必填，偏移量
        limit： 非必填，条数
        """
        table = kwargs["table"]
        field = kwargs.get("field", "*")
        where = kwargs["where"]
        order = kwargs.get("order", "")
        sort = kwargs.get("sort", "asc")
        offset = kwargs.get("offset", 0)
        limit = kwargs.get("limit", 100)

        sql = f"SELECT {field} FROM {table} WHERE 1=1"
        values = []

        if isinstance(where, dict):
            for k, v in where.items():
                if isinstance(v, list):
                    sql += f" AND {k} IN ({', '.join(['%s'] * len(v))})"
                    values.extend([str(i) for i in v])
                else:
                    sql += f" AND {k}=%s"
                    values.append(str(v))
        elif isinstance(where, str):
            sql += f" AND {where}"

        if order:
            sql += f" ORDER BY {order} {sort}"

        sql += f" LIMIT {offset}, {limit};"
        logger.info(f"SQL: {sql} [参数: {values}]")

        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    await cur.execute(sql, values)
                    return await cur.fetchall()
        except Exception as e:
            logger.error(f"查询多条数据失败: {e}")
            raise

    async def table_count(self, **kwargs):
        """
        异步计数查询
        table：必填，表名
        where：必填，查询条件
        """
        table = kwargs["table"]
        where = kwargs["where"]

        sql = f"SELECT COUNT(1) AS count FROM {table} WHERE 1=1"
        values = []

        if isinstance(where, dict):
            for k, v in where.items():
                if isinstance(v, list):
                    sql += f" AND {k} IN ({', '.join(['%s'] * len(v))})"
                    values.extend([str(i) for i in v])
                else:
                    sql += f" AND {k}=%s"
                    values.append(str(v))
        elif isinstance(where, str):
            sql += f" AND {where}"

        sql += ";"
        logger.info(f"SQL: {sql} [参数: {values}]")

        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    await cur.execute(sql, values)
                    result = await cur.fetchone()
                    return result['count'] if result else 0
        except Exception as e:
            logger.error(f"计数查询失败: {e}")
            raise
