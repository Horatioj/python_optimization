import numpy as np
from scipy.linalg import solve
I = np.eye(3)
U = np.array([[-0.91,0.37,-0.18],
             [0.19,0.78,0.59],
             [0.36,0.50,-0.78]])
V = np.array([[0.25, -0.73,-0.62],
             [-0.74,-0.56,0.35],
             [-0.61,0.37,-0.69]])
Sigma = np.array([[3,0,0],[0,2,0],[0,0,1]])
A = U * Sigma * V
b = np.array([-0.29, -2.09, -0.98])
At = np.transpose(A)
Ai = np.linalg.inv(At * A)
x = 1
nabla = At*A*x - At*b
nabla_1 = np.linalg.norm(At*A*x - At*b, ord=1)
beta = np.linalg.norm(At*A, ord = 2)
t = 1
print(nabla_1)
y = (1-((At*A)/beta)) * x + (At * A)/beta
print(y)
print(np.linalg.norm(At*A*x - At*b, ord=1))
'''
while(nabla > 1):
    x = (I-(At*A)/beta) * x + (At * A)/beta
    t = t + 1
print(x)'''

o = np.array([[1.04442925],
            [0.61473373],
            [-0.01459383]])

print("*~~~*~~~*~~~*~~~*~~~*~~~*~~~")
print(o)