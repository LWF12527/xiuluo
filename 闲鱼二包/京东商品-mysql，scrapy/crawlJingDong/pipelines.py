# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


# useful for handling different item types with a single interface


class CrawljingdongPipeline:
    # def open_spider(self, spider):
    #     self.file = open('coments.txt', 'w+')
    #
    # def close_spider(self, spider):
    #     self.file.close()

    def dbHandle(self):
        conn = pymysql.connect(
            host="localhost",
            user="root",
            passwd="123456",
            charset="utf8",
            use_unicode=False
        )
        return conn

    def process_item(self, item, spider):
        dbObject = self.dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE jd_store")
        str = '\n'.join(item['UserComments'])
        sql = "INSERT INTO jd(`id`, `prodectName`, `storeName`, `price`, `address`, `userComments`) VALUES ('%s','%s','%s',%f,'%s','%s')"
        try:
            cursor.execute(sql%(item['id'], item['productName'], item['storeName'], item['price'],item['address'],str))
            cursor.connection.commit()
        except BaseException as e:
            print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
            dbObject.rollback()
        return item
