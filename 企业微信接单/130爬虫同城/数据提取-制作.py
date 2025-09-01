# -*- coding: utf-8 -*-

import json
import os
import jieba
import matplotlib.pyplot as plt
from collections import defaultdict

# 数据存储路径
data_dir = "data"  # 修改为您的数据文件夹路径
output_segmented_file = "segmented_comments.txt"

# 初始化存储变量
comments = []
yearly_visits = defaultdict(int)
yearly_ratings = defaultdict(lambda: {"good": 0, "mid": 0, "bad": 0})

# 遍历目录中的文件
for file_name in os.listdir(data_dir):
    if file_name.endswith(".json"):
        file_path = os.path.join(data_dir, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            dp_list = data.get("dpList", [])
            for dp in dp_list:
                # 提取评论内容
                dp_content = dp.get("dpContent", "")
                comments.append(dp_content)

                # 提取日期并统计年份数据
                dp_date = dp.get("dpDate", "")
                year = dp_date.split("-")[0]
                if year:
                    # 假设每条评论代表一次游客访问
                    yearly_visits[year] += 1

                    # 按评价类别统计
                    line_access = dp.get("lineAccess", "")
                    if line_access == "好评":
                        yearly_ratings[year]["good"] += 1
                    elif line_access == "中评":
                        yearly_ratings[year]["mid"] += 1
                    elif line_access == "差评":
                        yearly_ratings[year]["bad"] += 1

# 保存分词后的评论
with open(output_segmented_file, "w", encoding="utf-8") as f:
    for comment in comments:
        segmented = " ".join(jieba.cut(comment))
        f.write(segmented + "\n")

# 绘制游客数量折线图
years = sorted(yearly_visits.keys())
visit_counts = [yearly_visits[year] for year in years]

plt.figure(figsize=(10, 6))
plt.plot(years, visit_counts, marker="o")
plt.title("Yearly Visitor Count")
plt.xlabel("Year")
plt.ylabel("Visitor Count")
plt.grid()
plt.savefig("yearly_visits.png")
plt.show()

# 绘制好评、中评数量柱状图
good_counts = [yearly_ratings[year]["good"] for year in years]
mid_counts = [yearly_ratings[year]["mid"] for year in years]

x = range(len(years))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x, good_counts, width, label="Good Reviews")
plt.bar([i + width for i in x], mid_counts, width, label="Mid Reviews")
plt.xticks([i + width / 2 for i in x], years)
plt.title("Yearly Review Counts")
plt.xlabel("Year")
plt.ylabel("Review Count")
plt.legend()
plt.grid()
plt.savefig("yearly_reviews.png")
plt.show()
