#coding: utf-8

# 代价函数
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2021) # set a constant seed to get samerandom matrixs
A = np.random.rand(500, 100)
x_ = np.zeros([100, 1])
x_[:5, 0] += np.array([i+1 for i in range(5)]) # x_ denotes expected x
b = np.matmul(A, x_) +np.random.randn(500, 1) *0.1#add a noise to b
epsilion = 0.0000001
lam = 10# try some different values in {0.1, 1, 10}
#print(A)
#print(b)
def vnorm2(x): #矩阵二范数
    return np.linalg.norm(x,ord=2)
def vnorm1(x):
    return np.linalg.norm(x,ord=1)
def f(x,lam = lam):
    result = 1/2*vnorm2(np.dot(A,x)-b)+vnorm1(x)
    return result
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

data = np.array([[ -2.95507616,  10.94533252],
       [ -0.44226119,   2.96705822],
       [ -2.13294087,   6.57336839],
       [  1.84990823,   5.44244467],
       [  0.35139795,   2.83533936],
       [ -1.77443098,   5.6800407 ],
       [ -1.8657203 ,   6.34470814],
       [  1.61526823,   4.77833358],
       [ -2.38043687,   8.51887713],
       [ -1.40513866,   4.18262786]])
m = data.shape[0]  # 样本大小
X = data[:, 0].reshape(-1, 1)  # 将array转换成矩阵
y = data[:, 1].reshape(-1, 1)

def L_theta(theta, X_x0, y, lamb):
    """
    lamb: lambda, the parameter of regularization
    theta: (n+1)·1 matrix, contains the parameter of x0=1
    X_x0: m·(n+1) matrix, plus x0
    """
    h = np.dot(X_x0, theta)  # np.dot 表示矩阵乘法
    theta_without_t0 = theta[1:]
    L_theta = 0.5 * mean_squared_error(h, y) + 0.5 * lamb * np.sum(np.square(theta_without_t0))
    return L_theta

# 梯度下降
def GD(lamb, X_x0, theta, y, alpha):
    """
    lamb: lambda, the parameter of regularization
    alpha: learning rate
    X_x0: m·(n+1), plus x0
    theta: (n+1)·1 matrix, contains the parameter of x0=1
    """
    for i in range(T):
        h = np.dot(X_x0, theta)
        theta_with_t0_0 = np.r_[np.zeros([1, 1]), theta[1:]]  # set theta[0] = 0
        theta -= (alpha * 1/m * np.dot(X_x0.T, h - y) + lamb*(theta_with_t0_0))  # add the gradient of regularization term
        if i%50000==0:
            print(L_theta(theta, X_x0, y, lamb))
    return theta

T = 3000  # 迭代次数
degree = 11
theta = np.ones((degree + 1, 1))  # 参数的初始化，degree = 11，一个12个参数
alpha = 0.0000000006 # 学习率
# alpha = 0.003  # 学习率
lamb = 0.0001
# lamb = 0
poly_features_d = PolynomialFeatures(degree=degree, include_bias=False)
X_poly_d = poly_features_d.fit_transform(X)
X_x0 = np.c_[np.ones((m, 1)), X_poly_d]  # ADD X0 = 1 to each instance
theta = GD(lamb=lamb, X_x0=X_x0, theta=theta, y=y, alpha=alpha)

X_plot = np.linspace(-2.99, 1.9, 1000).reshape(-1, 1)
poly_features_d_with_bias = PolynomialFeatures(degree=degree, include_bias=True)
X_plot_poly = poly_features_d_with_bias.fit_transform(X_plot)
y_plot = np.dot(X_plot_poly, theta)
plt.plot(X_plot, y_plot, 'r-')
plt.plot(X, y, 'b.')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
