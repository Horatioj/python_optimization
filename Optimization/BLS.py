import numpy as np

alpha = beta = k = 0
s0 = 100

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

nabla =