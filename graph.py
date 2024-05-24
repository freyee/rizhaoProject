import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 假设您的Excel文件包含列名'Column1', 'Column2', 'Column3'等
column_names = ['硝态氮5/31','硝态氮6/2','硝态氮6/7','硝态氮6/9','硝态氮6/14','硝态氮6/16']  # 替换为您的列名列表

# 读取Excel文件
df = pd.read_excel('C:/Users/15267/Desktop/paper/rizhao/newdocument/原始数据.xlsx', sheet_name='Sheet1')  # 替换为您的文件路径和工作表名

# 初始化一个列表来存储每列的均值和标准差
means_stds = []
# print((f'{df[column_names[0]].values}'))

# 计算每列的均值和标准差
# for column in column_names:
#     data_column = df[column].values
    # assert len(data_column-1) % 3 == 0, f"The length of {column} is not a multiple of 3."

group_size = 3
# num_groups = len(data_column) // group_size

# means = []
# stds = []


list1=['S1K0N3', 'S1K1N3','S1K2N3', 'S1K3N3', 'S1K4N3', 'S2K2N3', 'S1K1N2', 'S1K2N2', 'S1K4N2', 'S1K3N0', 'S1K3N1', 'S1K3N2', 'S1K3N4']
chuli={0,1,2,3,4,5,6,7,8,9,10,11,12}

for i in chuli:
    means = []
    stds = []


    for column in column_names:
        num=3
        if column == '硝态氮6/21':
            num=2
        if column == '硝态氮6/23':
            num = 2


        data_column = df[column].values
        group = data_column[i*3:i*3 + num]
        means.append(np.mean(group))
        stds.append(np.std(group))
    means_stds.append({'Means': means, 'Stds': stds})

# 设置图的宽度和高度
plt.figure(figsize=(10, 8))

# 初始化x轴的位置
x_pos = np.arange(len(means_stds[0]['Means']))
print(f'{len(means_stds)}')

# 绘制柱状图和误差线
bar_width = 0.05  # 柱状图的宽度


#S1K0N3 S1K1N3 S1K2N3 S1K3N3 S1K4N3 S2K2N3 S1K1N2 S1K2N2 S1K4N2 S1K3N0 S1K3N1 S1K3N2 S1K3N4
#   1     2      3      4      5      6      7      8      9      10     11     12     13



for i, (data, column) in enumerate(zip(means_stds, chuli)):
    # 调整x轴位置以便柱状图不重叠
    curr_x_pos = x_pos + i * bar_width

    # 绘制柱状图
    bars=plt.bar(curr_x_pos, data['Means'], bar_width, label=list1[column])
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}',  # 显示两位小数
                 ha='center', va='bottom', fontsize=7)  # 水平和垂直对齐，字体大小
    # 绘制误差线
    errorbars=plt.errorbar(curr_x_pos, data['Means'], yerr=data['Stds'], fmt='none', ecolor='red', capsize=5)
    for i, (mean, std) in enumerate(zip(data['Means'], data['Stds'])):
        bottom_text_y = mean + std +0.5
        # 你可以设置一个最小y值，以防止标签与轴重叠
        min_y = min(data['Means']) + 0.05 * (max(data['Means']) - min(data['Means']))
        if bottom_text_y > min_y:  # 避免与轴重叠
            plt.text(curr_x_pos[i], bottom_text_y, f'-{std:.2f}', ha='center', va='top', fontsize=7, color='red')





# 设置图表的标题和轴标签
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']  # 如果需要显示中文标题和标签，可以取消注释

plt.title('Grouped Bar Chart with Error Bars')
plt.xlabel('Group')
plt.ylabel('Value')
plt.xticks(x_pos + (len(column_names) +4) * bar_width, [f'{column}' for column in column_names])
plt.legend(loc='upper right')

# 显示图表
plt.tight_layout()
plt.show()