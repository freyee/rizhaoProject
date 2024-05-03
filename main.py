import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

if __name__ == '__main__':
    df = pd.read_excel('data13.xlsx')
    x_AN = df['铵态氮'].values
    y_sum_yield = df['总产量'].values
    y_ave_num = df['平均个数'].values

    coefficients1 = np.polyfit(x_AN, y_sum_yield, 1)
    slope1 = coefficients1[0]
    intercept1 = coefficients1[1]

    coefficients2 = np.polyfit(x_AN, y_ave_num, 1)
    slope2 = coefficients2[0]
    intercept2 = coefficients2[1]
    r2_ave_num = r2_score(y_ave_num, slope2*x_AN + intercept2)

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用SimHei字体显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 确保负号也能正确显示

    axs[0].scatter(x_AN, y_sum_yield, label='原始数据')
    axs[0].plot(x_AN, slope1*x_AN + intercept1, 'r', label='拟合线')
    axs[0].set_xlabel('AN')
    axs[0].set_ylabel('sum_yield')
    axs[0].set_title('AN-sum_yield Graph (R² = {:.2f})'.format(r2_ave_num))
    axs[0].legend()

    axs[1].scatter(x_AN, y_ave_num, label='原始数据')
    axs[1].plot(x_AN, slope2*x_AN + intercept2, 'r', label='拟合线')
    axs[1].set_xlabel('AN')
    axs[1].set_ylabel('ave_num')
    axs[1].set_title('AN-ave_num Graph')
    axs[1].legend(prop={'family': 'SimHei', 'size': 12})

    # plt.savefig('my_plot1.png')

    plt.show()


