import configparser
import logging
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from pypinyin import pinyin, Style  # 只用于城市拼音

from basic_main import BasicMain
from mysql import DbManager

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 全局配置
MAX_WORKERS = 5
BATCH_SIZE = 20
MAX_RETRY = 3

# 读取配置文件
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)


class ListPageCollector:
    def __init__(self):
        self.db_manager = DbManager(config=0)
        self.basic_main = BasicMain()

        # 房源类型映射
        self.house_type_map = {
            '不限': '',
            '一室': 'j1',
            '两室': 'j2',
            '三室': 'j3',
            '四室': 'j4',
            '四室以上': 'j5'
        }

        # 租赁方式映射
        self.rental_mode_map = {
            '不限': 'chuzu',
            '租房': 'zufang',
            '合租/单间': 'hezu'
        }

    def chinese_to_pinyin(self, text, style=Style.NORMAL):
        """城市中文转拼音（区域拼音已由数据库提供，不再翻译）"""
        if not text:
            return ""
        pinyin_list = pinyin(text, style=style)
        return "".join(item[0] for item in pinyin_list)

    def build_list_url(self, task, page_num=1):
        """构建列表页URL"""
        # 城市拼音首字母
        city_pinyin = self.chinese_to_pinyin(task['city'], Style.FIRST_LETTER)

        # 区域拼音直接使用数据库字段
        area_pinyin = task['area_pingyin']

        # 租赁方式
        rental_mode = self.rental_mode_map.get(task['rental_mode'], 'chuzu')

        # 房源类型
        house_type_param = self.house_type_map.get(task['house_type'], '')

        url_parts = [
            f"https://{city_pinyin}.58.com",
            area_pinyin,
            rental_mode
        ]

        if house_type_param and task['rental_mode'] != '合租/单间':
            url_parts.append(house_type_param)

        if page_num > 1:
            url_parts.append(f"pn{page_num}")

        base_url = "/".join(url_parts) + "/"
        base_url += f"?minprice={task['min_price']}_{task['max_price']}"

        return base_url


    def process_task(self, task):
        """处理单个采集任务 - 仅采集列表页"""
        try:
            current_page = task['current_page'] + 1

            while current_page <= task['max_pages']:
                # 构建列表URL
                list_url = self.build_list_url(task, current_page)
                logger.info(f"ID={task['id']}-处理列表页: {list_url}")

                try:
                    # 获取列表页内容
                    html_content = self.basic_main.fetch_page(list_url)

                    # 解析列表页获取详情页链接和实际最大页数
                    actual_max_page, house_detail_list = self.basic_main.parse_detail_page(html_content)

                    # 记录获取到的详情页链接数量
                    logger.info(f"ID={task['id']}-page={current_page}-获取到 {len(house_detail_list)} 个详情页链接")

                    # 更新最大页数（如果实际页数小于预设值）
                    if actual_max_page < task['max_pages']:
                        self.db_manager.table_update(
                            table="58_queue",
                            data={"max_pages": actual_max_page},
                            where={"id": task['id']}
                        )
                        logger.info(f"ID={task['id']} 更新最大页数: {actual_max_page}")

                    self.db_manager.table_insert_batch(
                        table="58_detail",
                        data=house_detail_list,
                        ignore_duplicate=True  # 唯一索引冲突，忽略重复行
                    )

                    # 更新当前页码
                    self.db_manager.table_update(
                        table="58_queue",
                        data={"current_page": current_page},
                        where={"id": task['id']}
                    )
                    current_page += 1

                except Exception as e:
                    logger.error(f"ID={task['id']}-page={current_page}, 处理列表页失败: {list_url} - {str(e)}")
                    error_log = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {str(e)}"
                    if "反爬" not in str(e) and '没有' not in str(e): # 反爬错误不记录
                        # 更新错误计数和日志
                        self.db_manager.table_update(
                            table="58_queue",
                            data={
                                "retry_count": task['retry_count'] + 1,
                                "error_log": error_log
                            },
                            where={"id": task['id']}
                        )
                        continue

            # 标记任务完成
            if current_page > task['max_pages']:
                self.db_manager.table_update(
                    table="58_queue",
                    data={"sync_status": 1},
                    where={"id": task['id']}
                )
                logger.info(f"任务完成: {task['id']}")

        except Exception as e:
            logger.error(f"处理任务失败: {task['id']} - {str(e)}")

    def run(self):
        """主运行方法"""
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            while True:
                try:
                    # 获取待处理任务
                    tasks = self.db_manager.table_select(
                        f"SELECT * FROM 58_queue WHERE sync_status=0 AND retry_count<3 LIMIT {BATCH_SIZE}",
                    )

                    if not tasks:
                        logger.info("无待处理任务，等待3600s...")
                        time.sleep(3600)
                        continue

                    # 提交到线程池
                    futures = [executor.submit(self.process_task, task) for task in tasks]

                    # 等待所有完成
                    for future in as_completed(futures):
                        future.result()  # 获取结果并处理异常

                    logger.info(f"批次完成: 处理 {len(tasks)} 个任务")

                except Exception as e:
                    logger.error(f"主循环错误: {str(e)}")
                    time.sleep(30)


if __name__ == "__main__":
    collector = ListPageCollector()
    collector.run()