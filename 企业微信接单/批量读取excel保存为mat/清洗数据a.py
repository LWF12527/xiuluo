import random

import pandas as pd

work_df_list = []

for i in range(1, 33):
    sj_a = pd.read_excel('数据集/实验原始数据1a.xlsx', sheet_name='{}'.format(i))
    # 删除空列
    sj_a_1 = sj_a["动作贡献量"]
    gzd = ['高', '中', '低']
    sj_a_1_1 = []
    sj_a_1 = sj_a["动作贡献量"]
    for i in sj_a_1:
        i = gzd[random.randint(0, 2)]
        sj_a_1_1.append(i)
    sj_a_1 = sj_a_1_1
    sj_a_2 = sj_a["个体施动感"]
    sj_a_3 = sj_a['联合施动感']
    sj_a_dict = {
        '动作贡献量': sj_a_1,
        '个体施动感': sj_a_2,
        '联合施动感': sj_a_3
    }
    print(sj_a_dict)
    sj_a_df = pd.DataFrame(sj_a_dict)
    work_df_list.append(sj_a_df)

with pd.ExcelWriter(r'qx_a_work.xlsx') as writer:
    work_df_list[0].to_excel(writer, sheet_name="1")
    work_df_list[1].to_excel(writer, sheet_name="2")
    work_df_list[2].to_excel(writer, sheet_name="3")
    work_df_list[3].to_excel(writer, sheet_name="4")
    work_df_list[4].to_excel(writer, sheet_name="5")
    work_df_list[5].to_excel(writer, sheet_name="6")
    work_df_list[6].to_excel(writer, sheet_name="7")
    work_df_list[7].to_excel(writer, sheet_name="8")
    work_df_list[8].to_excel(writer, sheet_name="9")
    work_df_list[9].to_excel(writer, sheet_name="10")
    work_df_list[10].to_excel(writer, sheet_name="11")
    work_df_list[11].to_excel(writer, sheet_name="12")
    work_df_list[12].to_excel(writer, sheet_name="13")
    work_df_list[13].to_excel(writer, sheet_name="14")
    work_df_list[14].to_excel(writer, sheet_name="15")
    work_df_list[15].to_excel(writer, sheet_name="16")
    work_df_list[16].to_excel(writer, sheet_name="17")
    work_df_list[17].to_excel(writer, sheet_name="18")
    work_df_list[18].to_excel(writer, sheet_name="19")
    work_df_list[19].to_excel(writer, sheet_name="20")
    work_df_list[20].to_excel(writer, sheet_name="21")
    work_df_list[21].to_excel(writer, sheet_name="22")
    work_df_list[22].to_excel(writer, sheet_name="23")
    work_df_list[23].to_excel(writer, sheet_name="24")
    work_df_list[24].to_excel(writer, sheet_name="25")
    work_df_list[25].to_excel(writer, sheet_name="26")
    work_df_list[26].to_excel(writer, sheet_name="27")
    work_df_list[27].to_excel(writer, sheet_name="28")
    work_df_list[28].to_excel(writer, sheet_name="29")
    work_df_list[29].to_excel(writer, sheet_name="30")
    work_df_list[30].to_excel(writer, sheet_name="31")
    work_df_list[31].to_excel(writer, sheet_name="32")
print('\n存储完毕！！')
