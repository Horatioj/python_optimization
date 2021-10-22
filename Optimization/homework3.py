#coding:utf-8

import numpy as np
"""
矩阵运算过分复杂，因此使用numpy现成的矩阵进行基本运算操作
"""
#下面是一些必要函数
def f(x,U,Theta,V):
    ##f(x)函数的实现
    return 1/2*abs(vnorm2(U*Theta*V*x-b))**2

def vnorm2(x):
    """
    返回numpy数组的二范数
    """
    a=x.T*x
    return a.tolist()[0][0]**(1/2)

def btls(U,Theta,V,b,epsilon,x,s0,alpha,beta):
    """
    backtracking line search,返回st
    """
    k=0
    s=s0
    gradfx=V.T*Theta*Theta*V*x-V.T*Theta*U.T*b
    while f(x-s*gradfx,U,Theta,V)>f(x,U,Theta,V)-alpha*s*(vnorm2(gradfx)**2) :
        s=beta*s
        k=k+1
    return s

def GD(U,Theta,V,b,epsilon,x0,isbtls):
    """
    梯度下降法计算，
    如果isbtls==1, 则使用btls函数进行回退法搜索合适的st,
    否则使用beta函数
    """
    t=0
    tmax=10**30
    print("设定可以容忍的最大迭代次数:",tmax)
    A=U*Theta*V
    betabeta=max(np.linalg.eig(A.T*A)[0])
    """
    beta方法的beta,是矩阵类型
    """
    s0=100
    st=s0
    print("默认s0是:",s0)
    alpha=0.5
    beta=0.5
    if isbtls==1:
        print("默认回退法的α是：",alpha)
        print("默认回退法的β是：",beta)
    xt=x0
    gradfx=V.T*Theta*Theta*V*xt-V.T*Theta*U.T*b
    chazhi_xt=abs(st*vnorm2(gradfx))
    chazhi_fx=abs(alpha*st*vnorm2(gradfx)**2)
    while t<tmax and chazhi_xt>=epsilon and chazhi_fx>epsilon and vnorm2(gradfx)>epsilon:
        if isbtls==1:
            st=btls(U,Theta,V,b,epsilon,xt,s0,alpha,beta)
        else:
            st=1/betabeta
        xt1=xt-st*gradfx
        chazhi_xt=abs(vnorm2(st*gradfx))
        chazhi_fx=abs(f(xt1,U,Theta,V)-f(xt,U,Theta,V))
        gradfx=V.T*Theta*Theta*V*xt1-V.T*Theta*U.T*b
        xt=xt1
        t=t+1
    print("结果是：")
    print(xt)
    r=Rr(U,Theta,V,b,xt)
    return {"迭代次数":t,"相对残差:":r}

def Rr(U,Theta,V,b,x):
    """
    计算最后结果的相对残差：norm(b-A*x)/norm(b)
    """
    A=U*Theta*V
    Rr=vnorm2(b-A*x)/vnorm2(b)
    return Rr

#这是一系列初始化过程
U=np.mat("-0.91,0.37,-0.18;0.19,0.78,0.59;0.36,0.50,-0.78")
Theta=np.mat([[3,0,0],[0,2,0],[0,0,1]])
V=np.mat([[0.25,-0.73,-0.62],[-0.74,-0.56,0.35],[-0.61,0.37,-0.69]])
b=np.mat([-0.29,-2.09,-0.98]).T
epsilon=10**(-7)
print("误差选取：",epsilon)
x0=np.mat([0,0,0]).T
print("初值选取：",x0)

"""
误差选取： 1e-07
初值选取： [[0]
           [0]
           [0]]
"""
"""
import timeit
"""
#利用time函数来进行计时
"""
print("这是使用回退法求解第一种情况：")
%time print("回退法相对残差、迭代次数及时间:",GD(U,Theta,V,b,epsilon,x0,1))
print("这是使用β法求解第一种情况：")
%time print("β法结相对残差、迭代次数及时间：",GD(U,Theta,V,b,epsilon,x0,0))
Theta1=np.mat([[3,0,0],[0,2,0],[0,0,10**(-2)]])
Theta2=np.mat([[3,0,0],[0,2,0],[0,0,10**(-6)]])
print("这是使用回退法求解第二种情况：")
%time print("回退法相对残差、迭代次数及时间:",GD(U,Theta1,V,b,epsilon,x0,1))
print("这是使用β法求解第二种情况：")
%time print("β法结相对残差、迭代次数及时间：",GD(U,Theta1,V,b,epsilon,x0,0))
print("这是使用回退法求解第三种情况：")
%time print("回退法相对残差、迭代次数及时间:",GD(U,Theta2,V,b,epsilon,x0,1))
print("这是使用β法求解第三种情况：")
%time print("β法相对残差、迭代次数及时间：",GD(U,Theta2,V,b,epsilon,x0,0))
"""