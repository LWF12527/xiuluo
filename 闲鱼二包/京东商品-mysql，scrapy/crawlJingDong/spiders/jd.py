import re
import sys
import json
import scrapy
from crawlJingDong import items
import requests as rq
from lxml import etree

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                  'Safari/537.36'}


class JdSpider(scrapy.Spider):
    #
    keyword = input('输入搜索的关键字：')
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?keyword={}'.format(keyword)]

    def parse(self, response):
        rep = response.text
        ans_html = etree.HTML(rep)
        data = ans_html.xpath("//*[@class='gl-warp clearfix']/li")

        for it in data:
            item = items.CrawljingdongItem()
            id = it.attrib["data-sku"]
            # e=it.xpath("*[@class='onekeyvip-jd-box-area xh-highlight']")
            price = float(it.xpath("./div/div[3]//i//text()")[0])
            prodectName = it.xpath("./div/div[4]//em//text()")[0]
            comment = it.xpath("./div/div[5]//a/@href")[0]
            storeName = it.xpath("./div/div[7]//a/text()")[0]
            address = it.xpath("./div/div[9]")[0].attrib["data-province"]

            # 变字典
            item["id"] = id
            item["price"] = price
            item["productName"] = prodectName
            item["comment"] = comment
            item["storeName"] = storeName
            item["address"] = address
            """由于评论数据是ajax异步加载的，所以在一开始获取的界面中是无法得到评论数据的，但是根据网页分析可以知道，
            评论数据都在js中存放，拿京东来说，找到productPageComments文件，根据url进行获取，就能得到json格式的评论数据
            """
            comJson = rq.get(
                f"https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={id}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1",
                headers=header)
            # 由于直接得到的text并不是json格式（有jquery这些），所以需要先转换成json（就是字典格式）
            str = comJson.text.strip()
            loads = json.loads(re.findall('\{.*\}', str)[0])
            UserComment = []
            list(map(lambda x: UserComment.append((x['content'])), loads['comments']))
            item['UserComments'] = UserComment
            yield item

        # 爬取100页评论数据（即1000条）
        for i in range(0, 100):
            url = self.url_head + self.url_middle + str(i) + self.url_end
            print("当前页面：", url)
            url='https://club.jd.com/comment/productPageComments.action?&productId=100008348542&score=3&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'
            yield scrapy.Request(url=url, callback=self.parse)
