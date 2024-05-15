import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import datetime
import os


def fit_and_plot(df, x_column, y_column, ax, title_suffix=''):
    x_values = df[x_column].values
    y_values = df[y_column].values

    if x_column == y_column:
        return

    # 进行线性拟合
    coefficients = np.polyfit(x_values, y_values, 1)
    slope = coefficients[0]
    intercept = coefficients[1]
    r2 = r2_score(y_values, slope * x_values + intercept)
    color='black'

    if r2>=0.5:
        color='r'
    elif r2>=0.4:
        color='orange'
    elif r2>=0.3:
        color='yellow'

    # 绘制散点和拟合线
    ax.scatter(x_values, y_values, label='原始数据')
    ax.plot(x_values, slope * x_values + intercept, color, label='拟合线')
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(f'{x_column}-{y_column} (R平方 = {r2:.2f})' + title_suffix)
    ax.legend()


# 主函数
if __name__ == '__main__':
    df = pd.read_excel('data39.xlsx')

    # 定义需要拟合的列
    x_columns = ['铵态氮','速效钾','硝态氮','有效磷','总产量', '平均产量','平均个数','平均单株结果数','株高','茎粗','小区开花数','TOC','TON']
    y_columns = ['铵态氮','速效钾','硝态氮','有效磷','总产量', '平均产量','平均个数','平均单株结果数','株高','茎粗','小区开花数','TOC','TON']

    # 创建图形
    fig, axs = plt.subplots(nrows=len(x_columns), ncols=len(y_columns), figsize=(12 * len(y_columns), 48))

    # 设置字体以确保中文显示
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 如果需要显示中文标题和标签，可以取消注释

    # 使用循环处理每个列
    for i, x_column in enumerate(x_columns):
        for j, y_column in enumerate(y_columns):
            fit_and_plot(df, x_column, y_column, axs[i,j], title_suffix=f' ({i + 1})')


        # 显示图形
    plt.tight_layout()  # 调整子图参数，使之填充整个图像区域

    timestamp = datetime.datetime.now()
    formatted_timestamp = timestamp.strftime('%Y_%m_%d_%H-%M-%S').replace(':', '_')

    plt.savefig(os.path.join("graph",f'Curvefitting39_({formatted_timestamp}).png'))
    plt.show()