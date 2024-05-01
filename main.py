from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    X = [12.46, 0.25, 5.22, 11.3, 6.81, 4.59, 0.66, 14.53, 15.49, 14.43,
         2.19, 1.35, 10.02, 12.93, 5.93, 2.92, 12.81, 4.88, 13.11, 5.8]
    Y = [29.01, 4.7, 22.33, 24.99, 18.85, 14.89, 10.58, 36.84, 42.36, 39.73,
         11.92, 7.45, 22.9, 36.62, 16.04, 16.56, 31.55, 20.04, 35.26, 23.59]

    # 转换成numpy的ndarray数据格式，n行1列,LinearRegression需要列格式数据，如下：
    X_train = np.array(X).reshape((len(X), 1))
    Y_train = np.array(Y).reshape((len(Y), 1))
    # 转换后数据格式如下
    # X_train = [[12.46], [0.25], [5.22], [11.3], [6.81], [4.59], [0.66], [14.53], [15.49], [14.43], [2.19], [1.35],
    #            [10.02], [12.93], [5.93], [2.92], [12.81], [4.88], [13.11], [5.8]]
    # Y_train = [[29.01], [4.7], [22.33], [24.99], [18.85], [14.89], [10.58], [36.84], [42.36], [39.73], [11.92], [7.45],
    #            [22.9], [36.62], [16.04], [16.56], [31.55], [20.04], [35.26], [23.59]]

    # 新建一个线性回归模型，并把数据放进去对模型进行训练
    lineModel = LinearRegression()
    lineModel.fit(X_train, Y_train)

    # 用训练后的模型，进行预测
    Y_predict = lineModel.predict(X_train)

    # coef_是系数，intercept_是截距
    a1 = lineModel.coef_[0][0]
    b = lineModel.intercept_[0]
    print("y=%.4f*x+%.4f" % (a1, b))

    # 对回归模型进行评分，这里简单使用训练集进行评分，实际很多时候用其他的测试集进行评分
    print("得分", lineModel.score(X_train, Y_train))

    # 简单画图显示
    plt.scatter(X, Y, c="blue")
    plt.plot(X_train, Y_predict, c="red")
    plt.show()