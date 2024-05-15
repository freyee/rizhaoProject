import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel文件
excel_file = 'C:/Users/15267/Desktop/paper/rizhao/newdocument/原始数据24-5-15-12-30.xlsx'  # 替换为你的Excel文件名
sheet_name = 'Sheet1'  # 替换为你的工作表名
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# 假设你的数据列名为'Data'
column_name = '硝态氮5/31'
data_column = df[column_name].values

# 确保数据的长度是3的倍数，这里总共有13组，每组3个数据
# assert len(data_column) == 13 * 3, "The length of data is not a multiple of 3 with 13 groups."

# 初始化均值和标准差列表
means = []
stds = []

# 每3个数据为一组，计算均值和标准差
for i in range(0, len(data_column), 3):
    group = data_column[i:i + 3]
    means.append(np.mean(group))
    stds.append(np.std(group))

# 将均值和标准差列表转换为pandas Series，方便后续操作
means_series = pd.Series(means, name='Mean')
stds_series = pd.Series(stds, name='Std Dev')

# 绘制柱状图，并添加误差线（标准差的一半作为误差）
index = np.arange(len(means))
width = 0.35  # 柱状图的宽度

fig, ax = plt.subplots()
rects1 = ax.bar(index, means_series, width, color='b', label='Mean')

# 添加误差线
ax.errorbar(index, means_series, yerr=stds_series / 2, fmt='none', ecolor='red', capsize=5)


# 添加数据标签
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)

# 设置图表标题和坐标轴标签
ax.set_xlabel('Group')
ax.set_ylabel('Value')
ax.set_title('Bar Chart with Error Bars')
ax.set_xticks(index)
ax.set_xticklabels(['Group {}'.format(i + 1) for i in index])
ax.legend()

# 显示图表
plt.tight_layout()
plt.show()