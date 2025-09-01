
# -*- coding: utf-8 -*-
import json
import jieba
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

# 读取JSON文件
with open('红楼梦.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 提取章节内容
chapters = {item['id']: item['content'] for item in data}

# 将所有章节内容合并成一个列表
chapter_texts = [' '.join(chapter) for chapter in chapters.values()]


# 使用jieba进行分词
def preprocess(text):
    words = jieba.lcut(text)
    return ' '.join(words)


chapter_texts_processed = [preprocess(text) for text in chapter_texts]

# 构建词频矩阵
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(chapter_texts_processed)

# 转换为TF-IDF矩阵
tfidf_transformer = TfidfTransformer()
X_tfidf = tfidf_transformer.fit_transform(X)

# 计算余弦相似度
similarity_matrix = cosine_similarity(X_tfidf)

# 打印前几行相似度矩阵
print("Similarity Matrix (first few rows):")
print(similarity_matrix[:5, :5])

# 基于相似度矩阵进行聚类分析
n_clusters = 5  # 假设我们想要将章节分为5个簇
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
clusters = kmeans.fit_predict(X_tfidf)

# 将聚类结果添加到DataFrame中
df_chapters = pd.DataFrame({'Chapter': list(chapters.keys()), 'Cluster': clusters})

# 打印每个簇中的章节
for cluster_id in range(n_clusters):
    cluster_chapters = df_chapters[df_chapters['Cluster'] == cluster_id]['Chapter'].tolist()
    print(f"Cluster {cluster_id}: {cluster_chapters}")

# 生成词云图
all_text = ' '.join(chapter_texts_processed)
wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=400, background_color='white').generate(all_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Hongloumeng')
plt.show()

# 绘制词频柱状图
word_freq = X.sum(axis=0).A1
words = vectorizer.get_feature_names_out()

# 获取前20个高频词
top_n = 20
top_words_indices = word_freq.argsort()[-top_n:][::-1]
top_words = [words[i] for i in top_words_indices]
top_word_freq = [word_freq[i] for i in top_words_indices]

plt.figure(figsize=(12, 6))
plt.bar(top_words, top_word_freq, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 20 Words Frequency in Hongloumeng')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 绘制相似度热力图
plt.figure(figsize=(12, 10))
plt.imshow(similarity_matrix, cmap='viridis', aspect='auto')
plt.colorbar(label='Cosine Similarity')
plt.title('Similarity Heatmap of Hongloumeng Chapters')
plt.xlabel('Chapter ID')
plt.ylabel('Chapter ID')
plt.xticks(ticks=np.arange(len(chapters)), labels=list(chapters.keys()), rotation=90)
plt.yticks(ticks=np.arange(len(chapters)), labels=list(chapters.keys()))
plt.tight_layout()
plt.show()
