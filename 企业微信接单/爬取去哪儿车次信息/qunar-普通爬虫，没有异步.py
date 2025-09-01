# 预算不足，只能普通爬虫，很慢，为了反爬，爬取一个停顿一秒，一千多个链接，差不多22分钟。

# encoding = 'utf-8'
# 导入所需要的库
import json
import time

from fake_useragent import UserAgent
from glom import glom
from lxml import etree
import pandas as pd
import requests
import os.path
import re

# 要填写/修改的参数：
# 文件名即出发地点，列名，日期（大于当前日期），到达地点

from_station_read = pd.read_excel(r"./中原.xlsx", 0)["市/县"]   # 数据框通过键提取列
from_station_save = []  # 清洗之后的出发城市
# 清洗数据，去掉县市
for i in from_station_read:
    list_i = list(i)
    if list_i[-1] == '市' or '县' and len(list_i) > 2:
        del list_i[-1]
    from_station_save.append("".join(list_i))

# 到达城市
# to_station = ["太原", "郑州", "武汉", "长沙", "南昌"]
to_station = ["洛阳"]
# 输入年月日，xxxx-xx-xx
year = '2023'
yue = '02'
day = '11'
date = "{}-{}-{}".format(year, yue, day)

#  定义的列表
checi_number_list = []  # 车次号
from_station_list = []  # 始发站
to_station_list = []  # 终/过站
checi_zhoguo_list = []  # 终/过标签
url_list = []  # 请求链接


def requests_html(url, headers):
    HTML = requests.get(url=url, headers=headers).text
    return HTML


# 解析数据，xpath/json,保存数据
def data_fetch_save(html_):
    #     tree = etree.HTML(html)
    #     li_list = tree.xpath("//*[@class='mt15 clearfix pic-list gallery']/li")
    #     for li in li_list:
    #         name = li.xpath(".//*/a[1]/@title")
    #         href = li.xpath(".//*/img/@src")
    #         print(name, "\n", href)

    # 后面得到的列表，不是字典所以不能用golm
    checi_info_list = glom(html_, "data.s2sBeanList")
    for checi_info in checi_info_list:
        checi_number = checi_info["trainNo"]
        from_station = checi_info["dptStationName"]
        to_station = checi_info["arrStationName"]
        checi_zhoguo = checi_info["extraBeanMap"]["stationType"]
        checi_number_list.append(checi_number)
        from_station_list.append(from_station)
        to_station_list.append(to_station)
        checi_zhoguo_list.append(checi_zhoguo)


if __name__ == '__main__':
    try:
        url_qnl = 'https://train.qunar.com/dict/open/s2s.do?callback=jQuery17205042356380172157_1676038497874' \
                  '&dptStation={}&arrStation={}&date={' \
                  '}&type=normal&user=neibu&source=site&start=1&num=500&sort=3&_=1676038498318 '
        # 拼接from_station x to_station个url
        for i in from_station_save:
            for j in to_station:
                url_list.append(url_qnl.format(i, j, date))

        sl = 0  # 爬虫次数
        for urli in url_list:
            sl = sl + 1
            time.sleep(1)  # 跑的太快封ip
            print("第{}次爬取，当前时间:".format(sl), time.strftime('%H:%M:%S'))
            print(urli)
            # 随机请求头
            headers = {'User-Agent': str(UserAgent().random)}
            html_text = requests_html(url=urli, headers=headers)
            # 清洗数据，转化为json
            html_text = re.split('[()]', html_text)
            html_json = html_text[1]
            # print(html_json)
            # 将json数据转换为字典，分别提取
            html_dict = json.loads(html_json)
            # print(html_dict)
            # 提取车次信息,
            # 判断该县市是否有火车站
            if html_dict['ret'] == False:
                # 提取数据
                print("该始发站未被收录！")
            else:
                data_fetch_save(html_dict)
    except:
        print("出错了，可能是网络错误，也可能是其他原因！")
    # 出错也保存现在的文件
    finally:
        # 保存文件
        checi_dict = {
            "车次号": checi_number_list,
            "始发站": from_station_list,
            "终点站": to_station_list,
            "终/过标签": checi_zhoguo_list
        }
        checi_df = pd.DataFrame(checi_dict)
        checi_df.to_excel("checi_info2.xlsx", sheet_name="qunar.com")

