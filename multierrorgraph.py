import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 假设您的Excel文件包含列名'Column1', 'Column2', 'Column3'等
column_names = ['硝态氮5/31', '硝态氮6/2', '硝态氮6/7','硝态氮6/9']  # 替换为您的列名列表

# 读取Excel文件
df = pd.read_excel('C:/Users/15267/Desktop/paper/rizhao/newdocument/原始数据24-5-15-12-30.xlsx', sheet_name='Sheet1')  # 替换为您的文件路径和工作表名

# 初始化一个列表来存储每列的均值和标准差
means_stds = []

# 计算每列的均值和标准差
for column in column_names:
    data_column = df[column].values
    # assert len(data_column-1) % 3 == 0, f"The length of {column} is not a multiple of 3."

    group_size = 3
    num_groups = len(data_column) // group_size

    means = []
    stds = []
    for i in range(0, len(data_column), group_size):
        group = data_column[i:i + group_size]
        means.append(np.mean(group))
        stds.append(np.std(group))

    means_stds.append({'Means': means, 'Stds': stds})

# 设置图的宽度和高度
plt.figure(figsize=(10, 6))

# 初始化x轴的位置
x_pos = np.arange(len(means_stds[0]['Means']))

# 绘制柱状图和误差线
bar_width = 0.25  # 柱状图的宽度
for i, (column, data) in enumerate(zip(column_names, means_stds)):
    # 调整x轴位置以便柱状图不重叠
    curr_x_pos = x_pos + i * bar_width

    # 绘制柱状图
    plt.bar(curr_x_pos, data['Means'], bar_width, label=column)

    # 绘制误差线
    plt.errorbar(curr_x_pos, data['Means'], yerr=data['Stds'], fmt='none', ecolor='red', capsize=5)

# 设置图表的标题和轴标签
plt.title('Grouped Bar Chart with Error Bars')
plt.xlabel('Group')
plt.ylabel('Value')
plt.xticks(x_pos + (len(column_names) - 1) * bar_width / 2, ['Group {}'.format(i + 1) for i in range(len(x_pos))])
plt.legend()

# 显示图表
plt.tight_layout()
plt.show()