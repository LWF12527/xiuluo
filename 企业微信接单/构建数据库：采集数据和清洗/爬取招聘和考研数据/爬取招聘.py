# encoding = 'utf-8'
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


def requests_html(url):
    headers= {'User-Agent':str(UserAgent().random)}
    return requests.get(url=url,headers=headers).text


if __name__ == '__main__':
    start_url = 'https://xiaoyuan.zhaopin.com/job/CC000954865J00101384586?from=sz?refcode=4019&srccode=401901&preactionid=dcfb9c02-f295-4019-9a43-d042dd6beaad'
    html_text = requests_html(start_url)
    print(html_text)
