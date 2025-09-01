import numpy as np
import pandas as pd

sj_b_df_list = []

for i in range(1, 29):
    sj_b = pd.read_excel('数据集/实验原始数据1b.xlsx', sheet_name='被试{}'.format(i))
    sj_b = sj_b.dropna(axis=0, how='all', subset=None, inplace=False)
    sj_b = sj_b.drop(index=3)
    sj_b_arr = np.array(sj_b)

    sj_b_arr1 = list(sj_b_arr[0])
    del sj_b_arr1[0:2]
    sj_b_arr2 = list(sj_b_arr[1])
    del sj_b_arr2[0:2]
    sj_b_arr3 = list(sj_b_arr[2])
    del sj_b_arr3[0:2]
    sj_b_arr4 = list(sj_b_arr[3])
    del sj_b_arr4[0:2]

    sj_b_dict = {
        "领导者-"+sj_b_arr[0][0]: sj_b_arr1,
        "领导者-"+sj_b_arr[1][0]: sj_b_arr2,
        "跟随者-"+sj_b_arr[2][0]: sj_b_arr3,
        "跟随者-"+sj_b_arr[3][0]: sj_b_arr4
    }
    print(sj_b_dict)
    sj_b_df = pd.DataFrame(sj_b_dict)
    sj_b_df_list.append(sj_b_df)

with pd.ExcelWriter(r'qx_b_work.xlsx') as writer:
    sj_b_df_list[0].to_excel(writer, sheet_name="1")
    sj_b_df_list[1].to_excel(writer, sheet_name="2")
    sj_b_df_list[2].to_excel(writer, sheet_name="3")
    sj_b_df_list[3].to_excel(writer, sheet_name="4")
    sj_b_df_list[4].to_excel(writer, sheet_name="5")
    sj_b_df_list[5].to_excel(writer, sheet_name="6")
    sj_b_df_list[6].to_excel(writer, sheet_name="7")
    sj_b_df_list[7].to_excel(writer, sheet_name="8")
    sj_b_df_list[8].to_excel(writer, sheet_name="9")
    sj_b_df_list[9].to_excel(writer, sheet_name="10")
    sj_b_df_list[10].to_excel(writer, sheet_name="11")
    sj_b_df_list[11].to_excel(writer, sheet_name="12")
    sj_b_df_list[12].to_excel(writer, sheet_name="13")
    sj_b_df_list[13].to_excel(writer, sheet_name="14")
    sj_b_df_list[14].to_excel(writer, sheet_name="15")
    sj_b_df_list[15].to_excel(writer, sheet_name="16")
    sj_b_df_list[16].to_excel(writer, sheet_name="17")
    sj_b_df_list[17].to_excel(writer, sheet_name="18")
    sj_b_df_list[18].to_excel(writer, sheet_name="19")
    sj_b_df_list[19].to_excel(writer, sheet_name="20")
    sj_b_df_list[20].to_excel(writer, sheet_name="21")
    sj_b_df_list[21].to_excel(writer, sheet_name="22")
    sj_b_df_list[22].to_excel(writer, sheet_name="23")
    sj_b_df_list[23].to_excel(writer, sheet_name="24")
    sj_b_df_list[24].to_excel(writer, sheet_name="25")
    sj_b_df_list[25].to_excel(writer, sheet_name="26")
    sj_b_df_list[26].to_excel(writer, sheet_name="27")
    sj_b_df_list[27].to_excel(writer, sheet_name="28")
print('\n存储完毕！！')
