# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    url = scrapy.Field()  # ֱ����ַ
    gkrs = scrapy.Field()  # �ۿ�����
    user_id = scrapy.Field()  # �û�id
    title = scrapy.Field()    # ֱ������
    user_tx = scrapy.Field()  # �û�ͷ���ַ
