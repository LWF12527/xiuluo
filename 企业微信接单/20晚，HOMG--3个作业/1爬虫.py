# coding=utf-8
import re

import jieba
import numpy as np
import pandas as pd
import requests
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import wordcloud

background = Image.open(r"data/chinamap.png")
# 将背景图转换为ndarray类型的数据
mask = np.array(background)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/71.0.3578.98 Safari/537.36",
}
response = requests.get("https://api.bilibili.com/x/v1/dm/list.so?oid=456486205", headers=headers)
# print(response.text)
html_doc = response.content.decode('utf-8')
# soup = BeautifulSoup(html_doc,'lxml')
pattern = re.compile("<d.*?>(.*?)</d>")
DanMu = pattern.findall(html_doc)

DanMu_df = pd.DataFrame(DanMu)
DanMu_df.to_csv(r'b站弹幕.csv', encoding='utf-8')
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',
                        mask=mask,  # 有问题
                        scale=15,
                        stopwords={' '},
                        contour_width=5,
                        contour_color='red')

# 对来自外部文件的文本进行中文分词，得到string
f = open(r'data/b站弹幕.csv', encoding='utf-8')
txt = f.read()
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)
# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)
# 将词云图片导出到当前文件夹
w.to_file(r'data/词云--JOJO的奇妙冒险 石之海.png')
plt.imshow(w, interpolation='bilinear')
plt.axis('off')
plt.show()