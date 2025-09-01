'''
1、读取csv，
2、读取test的数据，选取两三个计算，分别算出时间，然后乘以带宽累加
3、根据公式写一个求一行数据结果的函数
4、将结果返回比较大小的函数
5、对每个csv重复操作，返回列表：每个表最大的行
'''
import re
import numpy as np
import pandas as pd

MAP_PENALTY = 7.0
DELAY_PENALTY = 2.0
ENERGY_PENALTY = 1.0


def read_file(file_name, file_name2):
    # 计算data
    global dq
    dq = 0
    data = pd.read_csv(file_name, header=None)
    video_frame_size_list = data[2]
    video_frame_map_list = data[3]
    video_frame_infertime_list = data[4]

    # 计算test
    data2 = pd.read_csv(file_name2, header=None)
    time_list = []
    bandwidth_list = []
    continue_time_list = []  # 计算持续时间,最后一行加0
    for i in data2[0]:
        cf = i.split()
        time, bandwidth = cf[0], cf[1]
        time_list.append(float(time))
        bandwidth_list.append(float(bandwidth))
    for i in range(1, len(time_list)):
        continue_time = time_list[i] - time_list[i - 1]
        continue_time_list.append(continue_time)
    continue_time_list.append(1.0)
    # print(continue_time_list)

    # 比较每行大小
    config = re.split('[_.]', file_name)[2]
    config = int(config)
    delay, energy, throughout = 0, 0, 0
    reward_list = []  # 保存每行结果
    sy_xiazai = 0  # 每行下载后剩余下载量
    for i in range(0, len(data[2])):
        if config <= 3:
            delay = video_frame_infertime_list[i]
            # energy += video_frame_size_list[i] / pow(10, 5)
            energy += video_frame_size_list[i] / pow(10, 6)
        else:
            xiazai = 0
            throughout = 0  # 每行下载时间
            xiazai = xiazai + sy_xiazai
            for c in range(dq, len(continue_time_list)):
                xiazai = xiazai + bandwidth_list[c] * continue_time_list[c]
                throughout = throughout + continue_time_list[c]
                if xiazai * pow(10, 6) / 8 >= video_frame_size_list[i]:
                    dq = c
                    xiazai = xiazai * pow(10, 6) / 8
                    throughout = throughout - continue_time_list[c]
                    xiazai = xiazai - bandwidth_list[c] * continue_time_list[c]
                    sy_xiazai = xiazai - video_frame_size_list[i]
                    # 换算有问题
                    next_time = (video_frame_size_list[i] - xiazai) / (bandwidth_list[c] * pow(10, 6) / 8)  # 换算为kb
                    throughout = throughout + next_time
                    break

            print("{}第{}行下载区间：{}, 所需时间{}".format(file_name, i, dq, throughout))
            throughout = throughout * pow(10, 6) / 8  # 换算单位
            delay1 = video_frame_size_list[i] / 100 / throughout  #
            delay = video_frame_infertime_list[i] + delay1 * 1000  # 计算推断时间
            energy = 0.5 * pow(10, -5) * 8 * video_frame_size_list[i]
        reward = MAP_PENALTY * video_frame_map_list[i] * 100 - DELAY_PENALTY * delay - ENERGY_PENALTY * energy * 100
        reward_list.append(reward)
    return reward_list


if __name__ == '__main__':
    reward_list_list = []  # reward的矩阵
    data_file_name = r'数据/data/video_size_{}.csv'  # 数据表遍历
    test_file_name = r'数据/test/norway_bus_1'  # test表
    try:
        for x in range(0, 14):
            reward_li = read_file(file_name=data_file_name.format(x), file_name2=test_file_name)
            # 得到全部的reward，然后比较reward，确定下标，然后分别输出
            reward_list_list.append(reward_li)
    except:
        print("出错的表", 'video_size_{}.csv'.format(x))

    # 遍历矩阵，比较各行，得到最大行所在表，和reward
    reward_df = pd.DataFrame(reward_list_list)
    max_index_list = []  # 每张表最大值下标
    max_value_list = []  # 保存各行最大值
    for i in range(0, 29):
        df_x_list = list(reward_df[i])  # 列 列表
        max_value = max(df_x_list)
        max_value_list.append(max_value)
        max_index_list.append(df_x_list.index(max_value))
    print("行最大所在页面： ", max_index_list)
    # print('各行最大value值：', max_value_list)

    # 再次遍历， 根据索引找多最大值的行，值
    max_line_list = []
    x = 0
    try:
        for j in max_index_list:
            data_e = pd.read_csv(data_file_name.format(j), header=None)
            max_line = np.array(data_e).tolist()[x]  # 返回最大值的行
            max_line2 = ['第{}行, video_size_{}.csv, 值为{}'.format(x + 1, j, max_value_list[x]), max_line]
            max_line_list.append(max_line2)
            x = x + 1
    except:
        print("出错的表", 'video_size_{}.csv'.format(x))

    # 保存csv/excel
    max_line_list_df = pd.DataFrame(max_line_list)
    max_line_list_df.to_excel("result.xlsx")
    print("test表为：", test_file_name)
    print("结果为：", max_line_list_df)
