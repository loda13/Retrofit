"""
Author: TangYue
"""
'''
使用pandas等数据处理的包，对文件（豆瓣电影）进行处理
要求
    合并文件：异常值，缺失值
    进行数据统计、生成新特征、输出图形化分析结果
    储存分析结果
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# 读取csv文件
# data1 = pd.read_csv('source/2009.csv')
# data2 = pd.read_csv('data/2010.csv')
# data3 = pd.read_csv('data/2011.csv')
# data4 = pd.read_csv('data/2012.csv')
# data5 = pd.read_csv('data/2013.csv')
# data6 = pd.read_csv('data/2014.csv')

# 设置源文件夹、合并文件路径及文件名
current_path = r'.'
source_path = r'source'
result_path = r'result'
file_name = r'result.csv'
# os.chdir(source_path)
# print(os.curdir)
file_list = os.listdir(source_path)
print(file_list[0])

# dataframe
df = pd.read_csv(source_path + '/' + file_list[0], encoding='utf_8_sig')
df = df.sort_index(axis=1)
# print(df.columns)
# print(df.shape)

# df1 = pd.read_csv(source_path + '\\' + file_list[1], encoding='utf_8_sig')
# df1 = df1.sort_index(axis=1)
# print(df1.columns)
# print(df1.shape)
#
# df = df0.append(df1)
# print(df.columns)
# print(df.shape)
# df.to_csv(result_path + '\\' + file_name, encoding='utf_8_sig', index=False)

# 追加
for i in range(1, len(file_list)):
    df1 = pd.read_csv(source_path + '/' + file_list[i], encoding='utf_8_sig')
    df1 = df1.sort_index(axis=1)
    df = df.append(df1)

    # df.to_csv(result_path + '\\' + file_name, index=False,
    # encoding='utf_8_sig', header=False, mode='a+') print(i) print(
    # df.columns)
    # print(df.shape)
# df = pd.read_csv(result_path + '\\' + file_name, error_bad_lines=False,
# warn_bad_lines=False)
# df = pd.read_csv(result_path + '\\' + file_name, delimiter="\t")
# df = pd.read_csv(result_path + '\\' + file_name)


# 数据概览
# print(df.info())

# #
# print(df.shape[0])
# print(result.shape)
# print(df.columns)
# print(data1.columns)
# print(df.head(9))
#
# # #数据预分析
# print(df.isnull().sum())
#
# #分析
# cate_group = df.groupby(by='短片').size()
# print(cate_group)
# print(df)
# print(df.sort_values(by='all').tail(5))
# print(df.sort_values(by='award').tail(5))
# print(df.sort_values(by='movies').tail(5))
# print(df.iloc[0].at['award'])
# print(list(df.columns)[1])
# print(len(df.columns))

# for i in range(0, len(df.columns)):
#     pai = df.iloc[j].at[list(df.columns)[i]]
#     print(pai)
# print(df.groupby('award').size().head(5))
# award
# 0.0    27750
# 0.5      889
# 1.0      654
# 1.5      320
# 2.0      262
# dtype: int64

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(6, 9))  # 调节图形大小
labels = [u'0.0', u'0.5', u'1.0', u'1.5']  # 定义标签
sizes = [27750, 889, 654, 320]  # 每块值
colors = ['lightskyblue', 'yellowgreen', 'red', 'yellow']  # 每块颜色定义
explode = (0, 0, 0, 0)  # 将某一块分割出来，值越大分割出的间隙越大
patches, text1, text2 = plt.pie(sizes,
                                explode=explode,
                                labels=labels,
                                colors=colors,
                                autopct='%3.2f%%',  # 数值保留固定小数位
                                shadow=False,  # 无阴影设置
                                startangle=90,  # 逆时针起始角度设置
                                pctdistance=0.6)  # 数值距圆心半径倍数距离
# patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.title('获奖情况分布award')
os.chdir(current_path)
plt.savefig('bing.png')
plt.show()


df.to_csv(result_path + '/' + file_name, index=False, encoding='utf_8_sig',
          header=False, mode='a+')
