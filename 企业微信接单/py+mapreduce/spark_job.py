
import os
import findspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min, count, regexp_replace

findspark.init()

hadoop_url = 'hdfs://127.0.0.1:9000/{dir}/{file}'

spark = SparkSession.builder.appName("resume_analysis").getOrCreate()

# 加载应聘者数据
resume_data = spark.read.csv(hadoop_url.format(dir='jd/dataset', file='homework.csv'), header=True)
resume_data.show()

# 预处理海龄列 - 移除“年”后转换为浮点数
resume_data = resume_data.withColumn('海龄', regexp_replace(col('海龄'), '年', '').cast('float'))

# 1. 统计不同年龄的应聘者人数
age_count = resume_data.groupBy('年龄').count().sort('count', ascending=False)
age_count.show()
# 修改列名
age_count = age_count.withColumnRenamed('年龄', 'name').withColumnRenamed('count', 'value1')

# 删除已存在的输出路径
output_path = hadoop_url.format(dir='jd/output', file='age_count')
if os.system(f"hadoop fs -test -e {output_path}") == 0:
    os.system(f"hadoop fs -rm -r {output_path}")

# 保存到 HDFS
age_count.write.csv(output_path, header=True)

# 2. 统计各应聘职位的平均海龄、最大海龄和最小海龄
position_stats = resume_data.groupBy('应聘').agg(
    avg('海龄').alias('平均海龄'),
    max('海龄').alias('最大海龄'),
    min('海龄').alias('最小海龄')
).sort('平均海龄', ascending=False)
position_stats.show()

# 删除已存在的输出路径
output_path = hadoop_url.format(dir='jd/output', file='position_stats')
if os.system(f"hadoop fs -test -e {output_path}") == 0:
    os.system(f"hadoop fs -rm -r {output_path}")

# 保存到 HDFS
position_stats.write.csv(output_path, header=True)

spark.stop()

