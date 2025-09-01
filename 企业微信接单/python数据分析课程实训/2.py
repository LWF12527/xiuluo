import re

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
from datetime import datetime

# 读取文件
with open('新闻语料.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# 解析数据
news_items = []
pattern = r'(\w+)\t(.*?)\n'
matches = re.findall(pattern, data, re.DOTALL)

for category, content in matches:
    # 提取日期 (假设日期在内容的第一行)
    date_match = re.search(r'(\d{1,2}月\d{1,2}日)', content)
    date_str = date_match.group() if date_match else None

    # 如果有日期字符串，将其转换为datetime对象
    date = None
    if date_str:
        try:
            # 假设当前年份为2024年
            date = datetime.strptime(f"2024年{date_str}", '%Y年%m月%d日')
        except ValueError:
            print(f"Could not parse date: {date_str}")

    # 清洗内容，移除换行符等
    cleaned_content = re.sub(r'\s+', ' ', content).strip()

    news_items.append({
        'category': category,
        'date': date,
        'content': cleaned_content
    })

# 转换为DataFrame
df = pd.DataFrame(news_items)

# 1. 新闻主题的饼图可视化
category_counts = df['category'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('News Categories Distribution')
plt.show()

# 2. 各月份出现篇数的柱状图、折线图可视化
if not df['date'].isnull().all():
    # 解析日期并提取月份
    df['month'] = df['date'].dt.month
    month_counts = df['month'].value_counts().sort_index()

    # 柱状图
    plt.figure(figsize=(10, 6))
    plt.bar(month_counts.index, month_counts.values, color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Number of Articles')
    plt.title('Number of News Articles per Month (Bar)')
    plt.xticks(range(1, 13))
    plt.grid(axis='y')
    plt.show()

    # 折线图
    plt.figure(figsize=(10, 6))
    plt.plot(month_counts.index, month_counts.values, marker='o', linestyle='-', color='orange')
    plt.xlabel('Month')
    plt.ylabel('Number of Articles')
    plt.title('Number of News Articles per Month (Line)')
    plt.xticks(range(1, 13))
    plt.grid(True)
    plt.show()
else:
    print("No valid dates found to generate charts.")

# 3. 科技新闻内容的词云可视化
technology_news = df[df['category'] == '科技']
if not technology_news.empty:
    text = ' '.join(technology_news['content'])

    # 指定中文字体路径
    font_path = 'simhei.ttf'  # 确保这个路径指向你下载的字体文件

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path=font_path  # 使用指定的中文字体
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Technology News Content')
    plt.show()
else:
    print("No technology news found to generate a word cloud.")