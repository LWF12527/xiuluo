import re

import pandas as pd

df4 = pd.read_excel('a.xlsx', header=None)
list= df4[0].tolist()

result_list =[]
for i in list:
    list_spilt = re.findall(r'[\u4e00-\u9fa5]', i)
    result_list.append("".join(list_spilt))
print(result_list)
df = pd.DataFrame(result_list)
df.to_excel('提取中文.xlsx', header=None)
