# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QunarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    checi_number = scrapy.Field()
    from_station = scrapy.Field()
    to_station = scrapy.Field()
    checi_zhoguo = scrapy.Field()