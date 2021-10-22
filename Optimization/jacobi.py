# coding: utf-8
import numpy as np

# Jacobi迭代法，输入系数矩阵A、值矩阵b、迭代次数n、误差c
def Jacobi(A, b, n, c):
    if len(A) == len(b):  # 若A和b长度相等则开始迭代 否则方程无解
        x = []
        count = 0  # 迭代次数计数
        for i in range(len(b)):
            x.append([0])   # 初始化为全0矩阵
        while count < n:
            nx = []  # 保存单次迭代后的值
            for i in range(len(x)):
                nxi = 0
                for j in range(len(A[i])):
                    if i != j:
                        nxi += A[i][j] * x[j][0]
                nxi = (b[i] - nxi) / A[i][i]
                nx.append([nxi])  # 迭代计算得到的下一个xi值
            lc = []  # 存储误差
            for i in range(len(x)):
                lc.append(abs(x[i][0] - nx[i][0]))
            if max(lc) < c:
                return nx  # 当误差满足要求时,返回计算结果
            x = nx
            count = count + 1
        return False
    else:
        return False

# Gauss-Seidel迭代法
def Gauss_Seidel(A, b, c):
    x = np.array([0.0, 0, 0])
    x0 = np.array([0.0, 0, 0])
    count = 0  # 迭代次数计数
    while True:
        for i in range(3):
            nx = 0
            for j in range(3):
                if i < j:
                    nx += x0[j] * A[i][j]
                elif i > j:
                    nx += x[j] * A[i][j]
            x[i] = (b[i] - nx) / A[i][i]
        error = max(abs(x - x0))
        if error < c:
            break
        else:
            x0 = x.copy()
        count += 1
    print(x)

# 示例
A1 = np.array([[1.0, 2, 1], [3, 8, 1], [0, 4, 1]])
b1 = np.array([2.0, 12, 2])
print(Jacobi(A1, b1, 10, 0.001))
Gauss_Seidel(A1, b1, 0.001)

A2 = np.array([[8.0, -3, 2], [4, 11, -1], [2, 1, 4]])
b2 = np.array([20.0, 33, 12])
print(Jacobi(A2, b2, 10, 0.001))
Gauss_Seidel(A2, b2, 0.001)

