"""
analysis average bike using time
"""


"""
    明确任务：比较共享单车每个季度的平均骑行时间
"""
import os
import numpy as np
import matplotlib.pyplot as plt

data_path = './bikeshare'
data_filenames = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
                  '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']


def collect_data():
    """
        Step 1: 数据收集
    """
    data_arr_list=[]
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        data_arr = np.loadtxt(data_file,delimiter=',',dtype='str',skiprows=1)
        data_arr_list.append(data_arr)
    return data_arr_list


def process_data(data_arr_list):
    """
        Step 2: 数据处理
    """
    pass


def analyze_data(data_arr_list):
    """
        Step 3: 数据分析
    """
    pass


def show_results(duration_mean_list):
    """
        Step 4: 结果展示
    """
    pass


def main():
    """
        主函数
    """
    # 数据获取
    data_arr_list = collect_data()

    # 数据处理
    process_data(data_arr_list)

    # 数据分析
    analyze_data()

    # 结果展示
    show_results()


if __name__ == '__main__':
    main()
