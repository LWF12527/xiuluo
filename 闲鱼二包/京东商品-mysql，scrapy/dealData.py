import jieba
import jieba.analyse
import pandas as pd

import pymysql as pl
from matplotlib import pyplot as plt
from wordcloud import WordCloud

plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = 'SimHei'

conn = pl.connect(host='localhost', user='root', password='135157', db='JDstore', port=3306)
query = "SELECT * FROM `jdstore`.`jd` LIMIT 0,1000"
data = pd.read_sql_query(query, conn)
sumDes = data.describe()
print(f'数据信息的描述统计：\n{sumDes}')
# 得到价格区间
end, sta = int(sumDes.loc['max', 'price'] // 1000), int(sumDes.loc['min', 'price'] // 1000)
label = list(map(lambda x: str(x * 1000) + '-' + str((x + 1) * 1000), range(sta, end + 1)))
# 将商品价格划分到区间中
data['pStage'] = data['price'].apply(lambda x: int(x // 1000))
# 对商品价格区间内的商品数量使用条形图进行可视化
dataByP = data.groupby('pStage').count()['prodectName']
plt.bar(range(5),dataByP)
plt.title('价格分布')
plt.xticks(range(5),label,rotation=-10)
plt.yticks( rotation=-10)
plt.xlabel('价格(元)')
plt.ylabel('商品数量(个)')
plt.show(block=True)
# 对店铺地址进行统计并使用饼图进行可视化
dataByA = data.groupby('address').count()['storeName']
dataByA.plot(kind='pie',ylabel='',title='店铺地点分布',legend=True,cmap='rainbow')
plt.show(block=True)

# 将所有评论连接起来成一段文章
comStr = "".join(list(data['prodectName'])).replace('\n', ' ')
# 直接进行关键词分析
wordFlag = jieba.analyse.extract_tags(comStr)
print('\n开始制作词云……')  # 提示当前状态
wc = WordCloud(
    font_path='C:/Windows/Fonts/SimHei.ttf',  # 设置字体（这里选择“仿宋”）
    background_color='white',  # 背景颜色
    # mask=mask,  # 文字颜色+形状（有mask参数再设定宽高是无效的）
    # max_font_size=150  # 最大字号
)
wc.generate(' '.join(wordFlag))
plt.imshow(wc)  # 处理词云
plt.axis('off')
plt.show(block=True)
# 同上，不过操作对象是商品名称
comStr = "".join(list(data['userComments'])).replace('\n', ' ')
# 直接进行关键词分析
wordFlag = jieba.analyse.extract_tags(comStr)
print('\n开始制作词云……')  # 提示当前状态
wc = WordCloud(
    font_path='C:/Windows/Fonts/SimHei.ttf',  # 设置字体（这里选择“仿宋”）
    background_color='white',  # 背景颜色
    # mask=mask,  # 文字颜色+形状（有mask参数再设定宽高是无效的）
    # max_font_size=150  # 最大字号
)
wc.generate(' '.join(wordFlag))  # 从字典生成词云
plt.imshow(wc)  # 处理词云
plt.axis('off')
plt.show(block=True)