# coding=gbk
import json
import scrapy

from douyu.items import DouyuItem
# headers 放setting里面了

class DySpider(scrapy.Spider):
    name = "dy"
    allowed_domains = ["www.douyu.com"]
    start_urls = []

    def __init__(self, name=None):
        super().__init__(name)

    def start_requests(self):
        # 发起初始请求
        for i in range(1, 6):
            url = "https://www.douyu.com/gapi/rkc/directory/mixList/2_181/{}".format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 解析初始请求的响应
        data_json = json.loads(response.text)
        for i in range(0, len(data_json['data']['rl']) - 1):
            self.item = DouyuItem()
            # 获取字典的url_id,拼接为完整的url
            self.url = "https://www.douyu.com" + data_json['data']['rl'][i]['url']
            print("请求:",self.url)
            self.item['url'] = self.url
            # 使用回调函数
            yield scrapy.Request(
                url=response.urljoin(self.url),
                callback=self.parse_detail,
                meta={'item': self.item}  # 将item传递给下一个回调函数
            )

    # 回调函数
    def parse_detail(self, response):
        # 解析详情页的响应
        self.item = response.meta['item']  # 从meta中获取item

        # 解析观看人数
        gkrs = response.xpath("//*[@id='js-player-title']/div/div[2]/div[2]/div[1]/div[3]/a/div/text()").extract_first()
        self.item['gkrs'] = gkrs

        # 解析用户ID
        user_id = response.xpath('//*[@id="js-player-title"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/h2/text()').extract_first()
        self.item['user_id'] = user_id

        # 解析标题
        title = response.xpath('//*[@id="js-player-title"]/div[1]/div[2]/div[1]/div[2]/div[1]/h3/text()').extract_first()
        self.item['title'] = title

        # 解析用户头像
        user_tx = response.xpath('//*[@id="js-player-title"]/div/div[1]/div/a/div/img/@src').extract_first()
        self.item['user_tx'] = user_tx

        # 返回字段给管道存储
        yield self.item
