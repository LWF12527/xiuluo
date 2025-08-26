import os
import sys

import pymysql
import logging as Logger
import configparser

# 读取数据1
os.getcwd()
# os.chdir('E:/')

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.ini')

config = configparser.ConfigParser()
files_read = config.read(config_path)

# 正式bstcollect库
collect_dev = config['collect_dev']



# 连接MySQL
class DbManager(object):
    # 构造函数
    def __init__(self, config=4):
        self.conn = None
        self.cur = None
        self.config = config

    # 连接数据库
    def connectDatabase(self):
        try:
            # 正式bstcollect库
            if self.config == 0:
                self.conn = pymysql.connect(host=collect_dev['hostname'], user=collect_dev['username'],
                                            password=collect_dev['password'], database=collect_dev['database'],
                                            charset=collect_dev['charset'], port=int(collect_dev['port']))
            self.cur = self.conn.cursor()
            return True
        except:
            Logger.error("connectDatabase failed")
            return False

    # 关闭数据库
    def close(self):
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 基本的执行SQL方法，下面几乎都调用这个
    def execute(self, sql, params=None, exe_many=False):
        res = self.connectDatabase()
        if not res:
            return False
        cnt = 0
        try:
            if self.conn and self.cur:
                if exe_many:
                    cnt = self.cur.executemany(sql, params)
                else:
                    cnt = self.cur.execute(sql, params)
                self.conn.commit()
        except Exception as e:
            print(sql)
            Logger.error("execute failed: " + sql)
            Logger.error(str(e) + "\n\n")
            return False
        self.close()
        return cnt

    ################################################################
    ################ 以下为封装好的执行方法：表、字段方式 ################
    ################################################################
    # 新增并返回新增ID
    def table_insert(self, **kwargs):
        """
        table：必填，表名，如：table="test_table"
        data ：必填，更新数据，字典类型，如：data={"aaa": "666'6", "bbb": "888"}
        """
        table = kwargs["table"]
        data = kwargs["data"]
        sql = "insert into %s (" % table
        fields = ""
        values = []
        flag = ""
        for k, v in data.items():
            fields += "%s," % k
            values.append(str(v))
            flag += "%s,"
        fields = fields.rstrip(",")
        values = tuple(values)
        flag = flag.rstrip(",")
        sql += fields + ") values (" + flag + ");"
        Logger.info("sql：\n{} [{}]\n".format(sql, values))
        try:
            self.execute(sql, values)
            # 获取自增id
            res = self.cur.lastrowid
            return res
        except:
            self.conn.rollback()
            raise Exception('添加失败')

    def table_insert_batch(self, table, data):
        """
        批量插入数据到指定表
        :param table: 表名，如 "test_table"
        :param data: 字典列表，形如 [{"column1": "value1", "column2": "value2"}, {"column1": "value3", "column2": "value4"}]
        """
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("data 必须是字典列表")

        if not data:
            raise ValueError("data 不能为空")

        fields = data[0].keys()
        sql = f"INSERT INTO {table} ({', '.join(fields)}) VALUES "

        # 构建占位符和参数列表
        placeholders = []
        values = []
        for item in data:
            placeholders.append("(" + ", ".join(["%s"] * len(fields)) + ")")
            values.extend(item.values())

        sql += ", ".join(placeholders) + ";"

        Logger.info("sql：\n{} [{}]\n".format(sql, values))
        try:
            self.execute(sql, values)
            # 获取最后插入的自增ID（如果需要的话）
            res = self.cur.lastrowid
            return res
        except Exception as e:
            self.conn.rollback()
            Logger.error(f"插入失败: {e}")
            return None

    # 修改数据并返回影响的行数
    def table_update(self, **kwargs):
        """
        table：必填，表名，如：table="test_table"
        data ：必填，更新数据，字典类型，如：data={"aaa": "666'6", "bbb": "888"}
        where：必填，更新条件，字典类型用于=，如：where={"aaa": 333, "bbb": 2}；字符串类型用于非等于判断，如：where="aaa>=333"
        """
        table = kwargs["table"]
        data = kwargs["data"]
        where = kwargs["where"]
        sql = "update %s set " % table
        values = []
        for k, v in data.items():
            sql += "{}=%s,".format(k)
            values.append(str(v))
        sql = sql.rstrip(",")
        sql += " where 1=1 "
        if type(where) == dict:
            for k, v in where.items():
                if type(v) == list:
                    sql += " and {} in ({})".format(k, ','.join(['%s'] * len(v)))
                    values.extend([str(i) for i in v])
                else:
                    sql += " and {}=%s".format(k)
                    values.append(str(v))
        elif type(where) == str:
            sql += " and %s" % where
        sql += ";"
        values = tuple(values)
        Logger.info("sql：\n{} [{}]\n".format(sql, values))
        try:
            self.execute(sql, values)
            rowcount = self.cur.rowcount
            return rowcount
        except:
            self.conn.rollback()

    # 删除并返回影响行数
    def table_delete(self, **kwargs):
        """
        table：必填，表名，如：table="test_table"
        where：必填，删除条件，字典类型用于=，如：where={"aaa": 333, "bbb": 2}；字符串类型用于非等于判断，如：where="aaa>=333"
        """
        table = kwargs["table"]
        where = kwargs["where"]
        sql = "delete from %s where 1=1" % (table)
        values = []
        if type(where) == dict:
            for k, v in where.items():
                sql += " and {} in (%s)".format(k)
                values.append(str(v))
        elif type(where) == str:
            sql += " and %s" % where
        sql += ";"
        values = tuple(values)
        Logger.info("sql：\n{} [{}]\n".format(sql, values))
        try:
            self.execute(sql, values)
            rowcount = self.cur.rowcount
            return rowcount
        except:
            self.conn.rollback()

    def table_select(self, sql):
        try:
            self.execute(sql)
            data = self.cur.fetchall()
            column = [index[0] for index in self.cur.description]  # 列名
            data_dict = [dict(zip(column, row)) for row in data]  # row是数据库返回的一条一条记录，其中的每一天和column写成字典，最后就是字典数组

            return data_dict
        except:
            self.conn.rollback()

    # 查一条数据
    def table_select_one(self, **kwargs):
        """
        table：必填，表名，如：table="test_table"
        where：必填，查询条件，字典类型用于=，如：where={"aaa": 333, "bbb": 2}；字符串类型用于非等于判断，如：where="aaa>=333"
        field： 非必填，查询列名，字符串类型，如：field="aaa, bbb"，不填默认*
        order： 非必填，排序字段，字符串类型，如：order="ccc"
        sort：  非必填，排序方式，字符串类型，如：sort="asc"或者"desc"，不填默认asc
        """
        table = kwargs["table"]
        field = "field" in kwargs and kwargs["field"] or "*"
        where = kwargs["where"]
        order = "order" in kwargs and "order by " + kwargs["order"] or ""
        sort = kwargs.get("sort", "asc")
        if order == "":
            sort = ""
        sql = "select %s from %s where 1=1 " % (field, table)
        values = []
        if type(where) == dict:
            for k, v in where.items():
                sql += " and {} in (%s)".format(k)
                values.append(str(v))
        elif type(where) == str:
            sql += " and %s" % where
        sql += " %s %s limit 1;" % (order, sort)
        values = tuple(values)
        Logger.info("sql：\n{} [{}]\n".format(sql, values))
        try:
            self.execute(sql, values)
            data = self.cur.fetchone()
            return data
        except:
            self.conn.rollback()

    # 查批量数据
    def table_select_many(self, **kwargs):
        """
        table：必填，表名，如：table="test_table"
        where：必填，查询条件，字典类型用于=，如：where={"aaa": 333, "bbb": 2}；字符串类型用于非等于判断，如：where="aaa>=333"
        field： 非必填，查询列名，字符串类型，如：field="aaa, bbb"，不填默认*
        order： 非必填，排序字段，字符串类型，如：order="ccc"
        sort：  非必填，排序方式，字符串类型，如：sort="asc"或者"desc"，不填默认asc
        offset：非必填，偏移量，如翻页，不填默认0
        limit： 非必填，条数，不填默认100
        """
        table = kwargs["table"]
        field = "field" in kwargs and kwargs["field"] or "*"
        order = "order" in kwargs and "order by " + kwargs["order"] or ""
        sort = kwargs.get("sort", "asc")
        if order == "":
            sort = ""
        where = kwargs["where"]
        offset = kwargs.get("offset", 0)
        limit = kwargs.get("limit", 100)
        sql = "select %s from %s where 1=1 " % (field, table)
        values = []
        if type(where) == dict:
            for k, v in where.items():
                sql += " and {} in (%s)".format(k)
                values.append(str(v))
        elif type(where) == str:
            sql += " and %s" % where
        values = tuple(values)
        sql += " %s %s limit %s, %s;" % (order, sort, offset, limit)
        Logger.info("sql：\n{} [{}]\n".format(sql, values))
        try:
            self.execute(sql, values)
            data = self.cur.fetchall()
            return data
        except:
            self.conn.rollback()

    # 查条数
    def table_count(self, **kwargs):
        """
        table：必填，表名，如：table="test_table"
        where：必填，查询条件，字典类型用于=，如：where={"aaa": 333, "bbb": 2}；字符串类型用于非等于判断，如：where="aaa>=333"
        """
        table = kwargs["table"]
        where = kwargs["where"]
        sql = "select count(1) as count from %s where 1=1 " % (table)
        values = []
        if type(where) == dict:
            for k, v in where.items():
                sql += " and {} in (%s)".format(k)
                values.append(str(v))
        elif type(where) == str:
            sql += " and %s;" % where
        values = tuple(values)
        Logger.info("sql：\n{} [{}]\n".format(sql, values))
        try:
            self.execute(sql, values)
            data = self.cur.fetchone()
            return data[0]
        except:
            self.conn.rollback()

# if __name__ == "__main__":
#     # 示例
#     mysqldb = DbManager()
#     # ###################### ↓↓↓ 表、字段方式操作示例 ↓↓↓ ######################
#     # 插入数据
#     #i = mysqldb.table_insert(table="test_table", data={"aaa": '123"456', "bbb": "987'654", "ccc": 666})
#     #print("自增ID：", i)
#
#     #sys.exit(0)
#     # 更新数据
#     #c = mysqldb.table_update(table="test_table", data={"aaa": "666'6", "bbb": "888"}, where={"ccc": 3})
#     #print("更新行数：", c)
#
#     # 删除数据
#     #c = mysqldb.table_delete(table="test_table", where={"aaa": "666'6", "bbb": 777})
#     #print("删除行数：", c)
#
#     rows = mysqldb.table_select("SELECT pl_id,collect_url FROM platform_collect_plan WHERE sync_count<3 AND service='amazon_product' limit 100")
#     for row in rows:
#         print(row)
#     sys.exit(0)
#
#     # 查询一条
#     s = mysqldb.table_select_one(table="platform_collect_plan", field="aaa, bbb", where={"service": 333, "bbb": 1}, order="ccc", sort="asc")
#     print(s)
#
#     # 批量查询，默认查询100条
#     # 完整参数示例
#
#     l = mysqldb.table_select_many(table="test_table", field="*", where="aaa=333", order="ccc", sort="desc")
#     print(type(l))
#     # 必填参数示例
#     l = mysqldb.table_select_many(table="test_table", field="aaa, bbb", where={"aaa": 333, "bbb": 2})
#     print(l)
#
#     # 查条数
#     count = mysqldb.table_count(table="test_table", where={"aaa": 333, "bbb": 2})
#     print(count)
#

# host: 这个是ip地址，因为我这里是本地的，所以填127.0.0.1，也可以填localhost。
# user：用户名，如果你也是本地的，就填root好了
# password：这个是密码
# database：这个是数据库名
# port：这个是端口，本地的一般都是3306
# charset：这个是编码方式，要和你数据库的编码方式一致，要不会连接失败
