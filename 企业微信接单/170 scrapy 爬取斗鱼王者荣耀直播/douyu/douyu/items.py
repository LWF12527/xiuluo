# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    url = scrapy.Field()  # 直播地址
    gkrs = scrapy.Field()  # 观看人数
    user_id = scrapy.Field()  # 用户id
    title = scrapy.Field()    # 直播标题
    user_tx = scrapy.Field()  # 用户头像地址
