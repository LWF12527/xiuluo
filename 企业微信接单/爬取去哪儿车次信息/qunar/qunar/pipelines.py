# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import time
from itemadapter import ItemAdapter


class QunarPipeline:
    # 存入csv文件
    """
    我们希望的是, 在爬虫开始的时候. 打开这个文件
    在执行过程中. 不断的往里存储数据
    在执行完毕时, 关掉这个文件
    open_spider，close_spider，是scrapy默认的最开始和最终执行的文件
    """

    def open_spider(self, spider):
        print("开始存储，正在打开管道/存储文件。")
        self.f = open("./checi_info.csv", mode="a", encoding="utf-8")

    def close_spider(self, spider):
        if self.f:
            self.f.close()
        print("存储完毕，已关闭管道/存储文件。")

    def process_item(self, item, spider):
        self.f.write(f"{item['checi_number']},{item['from_station']},{item['to_station']},{item['checi_zhoguo']}\n")
        print("写入记录中，当前时间:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

        return item
