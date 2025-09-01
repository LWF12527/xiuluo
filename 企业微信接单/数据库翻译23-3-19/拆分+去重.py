import re

import pandas as pd

df4 = pd.read_excel('数据库表和字段-待翻译.xlsx', sheet_name=1)
list2_df3 = df4['*字段代码'].tolist()[0:1600]

result_list = []
for i in list2_df3:
    list_siplt = re.split("_", i)
    for j in list_siplt:
        result_list.append(j)
# 保存文件
# 保存字段名文件，去重
df_result_zdm = pd.DataFrame(result_list)
df_result_zdm.drop_duplicates(subset=None, keep='first', inplace=True)  # 去重
print("去重后数据框名长度：", len(df_result_zdm))
df_result_zdm.to_excel('数据字段前1600拆分去重.xlsx', header=None)
