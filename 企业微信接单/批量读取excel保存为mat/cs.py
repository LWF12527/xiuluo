import random

import pandas as pd

# for i in range(1, 33):
from numpy.random import rand

sj_a = pd.read_excel('数据集/实验原始数据1a.xlsx', sheet_name='1')
# 删除空列
gzd = ['高', '中', '低']
sj_a_1 = sj_a["动作贡献量"]

sj_a_1[30] = gzd[random.randint(0, 2)]
print(sj_a_1[30])
