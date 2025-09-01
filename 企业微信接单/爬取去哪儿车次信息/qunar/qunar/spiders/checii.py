import json
import re
import scrapy
import pandas as pd
from glom import glom
from qunar.items import QunarItem


def url_pingjie():
    # 读取文件中的出发地址
    from_station = pd.read_excel(r"D:\Users\86183\Desktop\程序开发接单\闲鱼接单\爬取去哪儿车次信息\fromCity.xlsx", 0)["出发城市"]
    # print(from_station[0])
    to_station = ["太原", "郑州", "武汉", "长沙", "南昌"]
    year = '2023'
    yue = '02'
    day = '09'
    date = "{}-{}-{}".format(year, yue, day)
    url = 'https://train.qunar.com/dict/open/s2s.do?callback=jQuery172031156339318063897_1675844627170&dptStation' \
          '={}&arrStation={}&date={}&type=normal&user=neibu&source=site&start=1&num=500&sort=3&_=1675844627553'
    # 拼接url并返回
    for i in from_station:
        for j in to_station:
            yield url.format(i, j, date)


class CheciiSpider(scrapy.Spider):
    name = 'checii'
    allowed_domains = ['qunar.com']

    # 放在url都会被异步请求，全部都会请求完
    start_urls = url_pingjie()  # 生成函数让yield返回，比append效率高

    def parse(self, response, **kwargs):
        # print(response.text)
        # 清洗数据，转化为json
        html_text = re.split('[()]', response.text)
        html_json = html_text[1]
        # print(html_json)
        # 将json数据转换为字典
        html_dict = json.loads(html_json)
        # print(html_dict)
        # 提取车次信息,
        # 判断该县市是否有火车站
        if html_dict['ret'] == False:
            print("该始发站未被收录！")
        else:
            # 提取数据
            # 后面得到的列表，不是字典所以不能用golm
            checi_info_list = glom(html_dict, "data.s2sBeanList")
            # 从列表提取车次号等
            for i in checi_info_list:
                checi_number = i["trainNo"]
                from_station = i["dptStationName"]
                to_station = i["arrStationName"]
                checi_zhoguo = i["extraBeanMap"]["stationType"]

                chechi_info = QunarItem()
                chechi_info['checi_number'] = checi_number
                chechi_info['from_station'] = from_station
                chechi_info['to_station'] = to_station
                chechi_info['checi_zhoguo'] = checi_zhoguo
                yield chechi_info  # 返回管道存储
