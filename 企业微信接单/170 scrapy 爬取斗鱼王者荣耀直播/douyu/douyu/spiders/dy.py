# coding=gbk
import json
import scrapy

from douyu.items import DouyuItem
# headers ��setting������

class DySpider(scrapy.Spider):
    name = "dy"
    allowed_domains = ["www.douyu.com"]
    start_urls = []

    def __init__(self, name=None):
        super().__init__(name)

    def start_requests(self):
        # �����ʼ����
        for i in range(1, 6):
            url = "https://www.douyu.com/gapi/rkc/directory/mixList/2_181/{}".format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # ������ʼ�������Ӧ
        data_json = json.loads(response.text)
        for i in range(0, len(data_json['data']['rl']) - 1):
            self.item = DouyuItem()
            # ��ȡ�ֵ��url_id,ƴ��Ϊ������url
            self.url = "https://www.douyu.com" + data_json['data']['rl'][i]['url']
            print("����:",self.url)
            self.item['url'] = self.url
            # ʹ�ûص�����
            yield scrapy.Request(
                url=response.urljoin(self.url),
                callback=self.parse_detail,
                meta={'item': self.item}  # ��item���ݸ���һ���ص�����
            )

    # �ص�����
    def parse_detail(self, response):
        # ��������ҳ����Ӧ
        self.item = response.meta['item']  # ��meta�л�ȡitem

        # �����ۿ�����
        gkrs = response.xpath("//*[@id='js-player-title']/div/div[2]/div[2]/div[1]/div[3]/a/div/text()").extract_first()
        self.item['gkrs'] = gkrs

        # �����û�ID
        user_id = response.xpath('//*[@id="js-player-title"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/h2/text()').extract_first()
        self.item['user_id'] = user_id

        # ��������
        title = response.xpath('//*[@id="js-player-title"]/div[1]/div[2]/div[1]/div[2]/div[1]/h3/text()').extract_first()
        self.item['title'] = title

        # �����û�ͷ��
        user_tx = response.xpath('//*[@id="js-player-title"]/div/div[1]/div/a/div/img/@src').extract_first()
        self.item['user_tx'] = user_tx

        # �����ֶθ��ܵ��洢
        yield self.item
