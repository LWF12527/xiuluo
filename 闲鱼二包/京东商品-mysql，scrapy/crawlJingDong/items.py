# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawljingdongItem(scrapy.Item):
    id=scrapy.Field()
    comment=scrapy.Field()
    productName=scrapy.Field()
    storeName=scrapy.Field()
    address=scrapy.Field()
    price=scrapy.Field()
    UserComments=scrapy.Field()


