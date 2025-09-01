import re
import pandas as pd

df1 = pd.read_excel('clean-a.xls', header=None)
df2 = pd.read_excel('clean-b.xlsx', header=None)
# clean_a表
list1_df1 = df1[1].tolist()
list2_df1 = df1[2].tolist()
# 谷歌表
list0_df2 = df2[0].tolist()
list1_df2 = df2[1].tolist()
# 2个列表组成字典
dict_a = dict(zip(list1_df1, list2_df1))
dict_gg = dict(zip(list1_df2, list0_df2))
dict_a.update(dict_gg)

# 拆分，翻译拼接
df3 = pd.read_excel('数据库表和字段-待翻译.xlsx', sheet_name=0)  # 读取未去重之后数据库名
df4 = pd.read_excel('数据库表和字段-待翻译.xlsx', sheet_name=1)  # 读取去重之后的字段名
list1_df3 = df3['*表代码'].tolist()
list2_df3 = df4['*字段代码'].tolist()

# 翻译数据库名
fy_result_sjk = []
a = 0
for i in list1_df3:
    a = a + 1
    fy_result1 = []
    list_spilt = re.split("_", i)
    # print(list_spilt)
    for j in list_spilt:
        j = j.lower()
        fy_result1.append(dict_a[j])
        print(a, ': ', fy_result1)
    fy_result_sjk.append("".join(fy_result1))
print(fy_result_sjk, '\n', len(fy_result_sjk))  # len 150

# 翻译字段,
fy_result_zdm = []
a = 0
for i in list2_df3:
    a = a + 1
    fy_result1 = []
    list_spilt = re.split("_", i)
    if "" in list_spilt:
        del list_spilt[-1]

    print(list_spilt)
    for j in list_spilt:
        j = j.lower()
        fy_result1.append(dict_a[j])
    print(a, ': ', fy_result1)
    fy_result_zdm.append("".join(fy_result1))
print(fy_result_zdm, '\n', len(fy_result_zdm))

# 保存数据框名文件，去重
df_result_sjk = pd.DataFrame(fy_result_sjk, list1_df3)
df_result_sjk.drop_duplicates(subset=None, keep='first', inplace=True)  # 去重
print("去重后数据库名长度：", len(df_result_sjk))
df_result_sjk.to_excel('数据库翻译.xlsx', header=None)

# 保存字段名文件，去重
df_result_zdm = pd.DataFrame(fy_result_zdm, list2_df3)
df_result_zdm.drop_duplicates(subset=None, keep='first', inplace=True)  # 去重
print("去重后数据字段名长度：", len(fy_result_zdm))
df_result_zdm.to_excel('数据字段翻译.xlsx', header=None)

# 文件合起来，不去重
print(len(list1_df3), len(fy_result_sjk), len(list2_df3),  len(fy_result_zdm) )
# df_result_all = pd.DataFrame(list1_df3, fy_result_sjk, list2_df3, fy_result_zdm)
# df_result_all.to_excel('数据库+字段翻译不去重.xlsx', header=None)

