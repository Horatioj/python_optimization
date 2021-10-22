# coding utf-8

import numpy as np

"""
class Jacobi():
    def __init__(self, A, X, b):
        self.A = A
        self.X = X
        self.b = b
        self._X = np.zeros(X.shape[0])

    def function(self):
        n = self.A.shape[0]
        for i in range(n):
            self.X[i] = self._X[i]
        for i in range(n):
            self._X[i] = self.b[i]
            for j in range(n):
                if j != i:
                    self._X[i] -= self.A[i][j] * self.X[j]
            self._X[i] /= self.A[i][i]

    def start(self, error):
        self.function()
        while abs(np.max(self.X) - np.max(self._X)) > error:
            self.function()


if __name__ == '__main__':
    A = np.array(input().split(" "))
    b = np.array(input().split(" "))
    X = np.array(input().split(" "))
    A = A.astype(np.float64)
    b = b.astype(np.float64)
    X = X.astype(np.float64)
    n = X.shape[0]
    A = A.reshape((n, n))
    jacobi = Jacobi(A, X, b)
    jacobi.start(1e-5)
    ANS = np.round(jacobi._X, 5)
    print("x:")
    for i in range(ANS.shape[0]):
        print(ANS[i])
class GaussSeidel(object):
    def __init__(self, A, X, b):
        self.A = A
        self.X = X
        self.b = b
        self._X = np.zeros(X.shape[0])

    def function(self):
        n = self.A.shape[0]
        for i in range(n):
            self.X[i] = self._X[i]
        for i in range(n):
            self._X[i] = self.b[i]
            for j in range(0, i):
                self._X[i] -= self.A[i][j] * self._X[j]
            for j in range(i+1, n):
                self._X[i] -= self.A[i][j] * self.X[j]
            self._X[i] /= self.A[i][i]

    def start(self, error):
        self.function()
        while abs(np.max(self.X) - np.max(self._X)) > error:
            self.function()

if __name__ == '__main__':
    A = np.array(input().split(" "))
    b = np.array(input().split(" "))
    X = np.array(input().split(" "))
    A = A.astype(np.float64)
    b = b.astype(np.float64)
    X = X.astype(np.float64)
    n = X.shape[0]
    A = A.reshape((n, n))
    gs = GaussSeidel(A, X, b)
    gs.start(1e-5)
    ANS = np.round(gs._X, 5)
    ANS = ANS.astype(str)
    print("x:")
    for i in range(ANS.shape[0]):
        while len(ANS[i]) < 7:
            ANS[i] += "0"
        print(ANS[i])"""

# coding: utf-8

A = np.array([[1.0, 2, 1], [3, 8, 1], [0, 4, 1]])
B = np.array([2.0, 12, 2])
x0 = np.array([0.0, 0, 0])
x = np.array([0.0, 0, 0])
print(x[0])
times = 0

'''
while True:
    for i in range(3):
        temp = 0
        for j in range(3):
            if i != j:
                temp += x0[j] * A[i][j]
        x[i] = (B[i] - temp) / A[i][i]

    calTemp = max(abs(x - x0))
    times += 1
    if calTemp < 1e-6:
        break
    else:
        x0 = x.copy()

print(times)
print(x)'''

while True:
    for i in range(3):
        temp = 0
        for j in range(3):
            if i < j:
                temp += x0[j] * A[i][j]
            elif i > j:
                temp += x[j] * A[i][j]
        x[i] = (B[i] - temp) / A[i][i]
    calTemp = max(abs(x - x0))
    times += 1
    if calTemp < 1e-6:
        break
    else:
        x0 = x.copy()

print(times)
print(x)






