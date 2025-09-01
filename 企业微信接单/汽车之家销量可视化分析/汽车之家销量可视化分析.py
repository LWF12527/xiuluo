# encoding = 'utf-8'
# 导入所需要的库
import os.path
import re
from lxml import etree
import pandas as pd
import requests
import matplotlib.pyplot as plt
from matplotlib import font_manager


def requests_html(url, headers):
    HTML = requests.get(url, headers=headers).text
    return HTML


def data_save(html):
    # 解析网页
    tree = etree.HTML(html)
    salesB_list = tree.xpath('//div[@class="ranking-block ranking-block--sale"]/div[@class="ranking-block__list"]')
    brandB_list = tree.xpath('//div[@class="ranking-block ranking-block--brand"]/div[@class="ranking-block__list"]')
    # print(sales_list)
    # print(brand_list)
    # 提取数据
    for i in salesB_list:
        ranking_list = i.xpath('./div/a/div[1]/text()')  # 排行
        # print(ranking_list)
        carModel_list = i.xpath('./div/a/div[3]/p[1]/text()')  # 汽车型号
        # print(carModel_list)
        SalePrice_list = i.xpath('./div/a/div[3]/p[2]/text()')  # 销售价格区间
        # print(SalePrice_list)
        modelSaleNumber_list = i.xpath('./div/a/div[4]/p/text()')  # 型号销售数量
        # print(modelSaleNumber_list)
    # 型号销售数量数据清洗
    saleNumber_list = []
    for i in modelSaleNumber_list:
        saleNumber = re.findall(r'[\d+]', i)
        saleNumber = "".join(saleNumber)
        # print(saleNumber)
        saleNumber_list.append(saleNumber)
    modelSaleNumber_list = saleNumber_list
    # print(modelSaleNumber_list)

    for i in brandB_list:
        brand_list = i.xpath('./div/a/div[3]/p/text()')  # 品牌名
        # print(brand_list)
        brandSaleNumber_list = i.xpath('./div/a/div[4]/p/text()')  # 品牌销售数量
        # print(brandSaleNumber_list)
    # 品牌销售数量数据清洗
    saleNumber_list = []
    for i in brandSaleNumber_list:
        saleNumber = re.findall(r'[\d+]', i)
        saleNumber = "".join(saleNumber)
        saleNumber_list.append(saleNumber)
    brandSaleNumber_list = saleNumber_list
    # print(brandSaleNumber_list)

    # 保存排行榜数据
    modelSale_dict = {
        '排名': ranking_list,
        '汽车型号': carModel_list,
        '售价': SalePrice_list,
        '型号销售数量': modelSaleNumber_list
    }
    brandSale_dict = {
        '排名': ranking_list,
        '品牌名': brand_list,
        '品牌销售数量': brandSaleNumber_list
    }
    modelSale_df = pd.DataFrame(modelSale_dict)
    brandSale_df = pd.DataFrame(brandSale_dict)

    # 多工作表保存
    with pd.ExcelWriter(r'data/汽车之家销售排行榜.xlsx') as writer:
        modelSale_df.to_excel(writer, sheet_name="型号销售排行榜")
        brandSale_df.to_excel(writer, sheet_name="品牌销售排行榜")
    # 返回排行榜数据
    return modelSale_dict, brandSale_dict


def chart_view(data):
    # 提取数据
    carModel_list = data[0]['汽车型号']  # 汽车型号
    SalePrice_list = data[0]['售价']  # 售价
    modelSaleNumber_list = data[0]['型号销售数量']  # 型号销售数量
    brand_list = data[1]['品牌名']  # 品牌名
    brandSaleNumber_list = data[1]['品牌销售数量']  # 品牌销售数量
    # 画图
    pie_chart(carModel_list[:10], modelSaleNumber_list[:10], '型号销售量占比饼图')  # 型号销售量占比饼图
    pie_chart(brand_list[:10], brandSaleNumber_list[:10], '品牌销售量占比饼图')  # 品牌销售量占比饼图
    bar_chart(carModel_list, SalePrice_list, modelSaleNumber_list, '汽车型号销售柱状图', '汽车型号', '售价', '销售数量')  # 汽车型号销售柱状图
    bar_chart(brand_list, brandSaleNumber_list, modelSaleNumber_list, '汽车品牌、型号销售柱状图', '品牌名', '品牌销售数量', '型号销售数量')  # 汽车品牌销售柱状图


# 生成饼图的函数
def pie_chart(labels, quants, title):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(1, figsize=(10, 10))
    plt.axis('equal')
    expl = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1]
    colors = ["yellow", "red", "coral", "green", "yellow", "orange", "blue", "red", "coral", "green",
              "blue"]
    patches, l_text, p_text = plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%',
                                      pctdistance=0.8, shadow=False)
    # 图内字体大小
    for f in p_text:
        f.set_size(15)
    # 图外字体大小
    for f in l_text:
        f.set_size(20)
    plt.title(title, bbox={'facecolor': '0.8', 'pad': 5})
    plt.savefig(r"data/{}.png".format(title), dpi=1000, bbox_inches='tight')
    plt.show()
    plt.close()


# 柱状图组合图函数
def bar_chart(name, dataList1, dataList2, title, xname, yname1, yname2):
    my_font = font_manager.FontProperties()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fig, ax1 = plt.subplots()
    plt.bar(name, dataList1, color='red')  # 设置柱状图
    plt.title(title, fontproperties=my_font)  # 表标题
    ax1.tick_params(labelsize=6)
    plt.xlabel(xname)  # 横轴名
    plt.ylabel(yname1)  # 纵轴名
    plt.xticks(rotation=0, color='blue')  # 设置横坐标变量名旋转度数和颜色

    ax2 = ax1.twinx()
    ax2.plot(dataList2, color='cyan')  # 设置线粗细，节点样式
    plt.ylabel(yname2)

    plt.plot(1, label=yname1, color="red", linewidth=5.0)  # 图例
    plt.plot(1, label=yname2, color="cyan", linewidth=1.0, linestyle="-.")  # 图例
    plt.legend()

    plt.savefig(r'data/{}.png'.format(title), dpi=1000, bbox_inches='tight')  # 保存至本地
    plt.show()
    plt.close()


if __name__ == '__main__':
    urls = 'https://www.autohome.com.cn/guangzhou/'  # 网址
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54 '
    }
    # 创建文件夹保存数据
    if not os.path.exists('./data'):
        os.mkdir('./data')
    # 返回网页
    html_text = requests_html(urls, headers)
    # 爬取并保存数据,返回两个排行榜数据,字典类型
    data_info = data_save(html_text)
    # print(data_info[0]['排名'])
    # 生成图表
    chart_view(data_info)
