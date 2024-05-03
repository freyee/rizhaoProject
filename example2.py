import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# 假设 X 是特征矩阵，y 是目标变量
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])  # 两个特征
y = np.array([3, 4, 5, 5.5, 6.5, 7])  # 目标变量

# 创建一个多项式特征生成器，这里假设我们想要一个二次多项式
poly_features = PolynomialFeatures(degree=2, include_bias=False)

# 创建一个线性回归模型
lin_reg = LinearRegression()

# 使用管道来组合多项式特征生成器和线性回归模型
poly_reg = make_pipeline(poly_features, lin_reg)

# 拟合模型
poly_reg.fit(X, y)

# 创建一个网格来评估模型
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

# 将网格点展平
X_grid = np.c_[xx.ravel(), yy.ravel()]

# 预测网格点上的值
y_grid = poly_reg.predict(X_grid)

# 将预测值重新塑形为网格形状
y_grid = y_grid.reshape(xx.shape)

# 绘制原始数据点
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k')

# 创建一个3D图来可视化结果
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制拟合的多项式曲面
ax.plot_surface(xx, yy, y_grid, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

# 设置坐标轴标签和标题
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')
ax.set_title('Polynomial Regression with 2 features')

plt.show()