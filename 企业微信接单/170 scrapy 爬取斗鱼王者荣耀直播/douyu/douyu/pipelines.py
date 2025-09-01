# coding=gbk
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DouyuPipeline:
    # 连接数据库
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='douyu',
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()

    # 存入数据
    def process_item(self, item, spider):
        # 插入数据
        sql = "INSERT INTO douyu (url, gkrs, user_id, title, user_tx) VALUES (%s, %s, %s, %s, %s)"
        values = (
            item['url'],
            item['gkrs'],
            item['user_id'],
            item['title'],
            item['user_tx']
        )
        self.cursor.execute(sql, values)
        self.conn.commit()  # 提交执行sql

        return item
    # 关闭连接
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
