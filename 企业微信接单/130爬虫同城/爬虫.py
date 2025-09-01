import sys
# 导入所需要的库
import datetime
import json
import random
import time

from fake_useragent import UserAgent
from glom import glom
from lxml import etree
import pandas as pd
import requests
import os.path
import re

from fake_useragent import UserAgent
import requests

# Set stdout to UTF-8
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)


def requests_html(url):
    headers = {'User-Agent': str(UserAgent().random)}
    response = requests.get(url=url, headers=headers)

    # 如果编码未知，可以尝试从响应头中推断
    if response.encoding is None or response.encoding == 'ISO-8859-1':
        response.encoding = response.apparent_encoding  # 根据内容自动检测编码

    return response.text


if __name__ == '__main__':
    # start_url = 'https://www.qcc.com/'
    for i in range(1, 55):
        start_url = 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=25794&page={}&pageSize=10&labId=1&sort=0&iid=0.17022760611673626'.format(
            i)
        html_text = requests_html(start_url)
        with open("./data/pl_{}.json".format(i), "w", encoding="utf-8") as f:
            f.write(html_text)
### 爬取多页数据，每页数据做提取，如何存储在文件里面
