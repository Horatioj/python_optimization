# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2021)  # set a constant seed to get samerandom matrixs
A = np.random.rand(500, 100)
x_ = np.zeros([100, 1])
x_[:5, 0] += np.array([i+1 for i in range(5)]) # x_ denotes expected x

b = np.matmul(A, x_) + np.random.randn(500, 1) * 0.1 #add a noise to b
epsilion = 0.0000001
lam = 10  # try some different values in {0.1, 1, 10}
#print(A)
#print(b)
step1 = 0.00002
step2 = 0.00005
step3 = 0.00001
step4 = 0.00008
def vnorm2(x): #矩阵二范数
    return np.linalg.norm(x, ord=2)
def vnorm1(x):
    return np.linalg.norm(x, ord=1)
def f_sub(x, lam = lam): #次梯度
    result = 1/2*vnorm2(np.dot(A,x)-b)+vnorm1(x)
    return result
def f_ridge(x):
    result = 1/2*vnorm2(np.dot(A,x)-b)+vnorm2(x)
    return result
def subgradient_descent(A,b,x,lam,epsilion, step, f_type):  #type=1, LASSO; type=2 Ridge
    t = 0 #计数器
    x0 = x
    plot_dic = {0:x0}
    current_error = epsilion*100#初始一个很大的误差项
    while t < 3000:
        if f_type == 1:
            xt = x0-step*(np.dot(A.T,(np.dot(A,x0)-b))+lam*np.sign(x0))
        elif f_type == 2:
            xt = x0 - step * (np.dot(A.T, (np.dot(A, x0) - b)) + 2 * lam * x0)
        else:
            return "错误！"
        if f_type == 1:
            f_min = min(f_sub(i) for i in plot_dic.values())
            for i in plot_dic.keys():
                current_error = abs(f_sub(plot_dic[i])-f_min)/f_min
                plot_dic[i] = current_error
            return{"结果":x0,"迭代步数":t,"次数-误差":plot_dic}
        elif f_type == 2:
            f_min = min(f_ridge(i) for i in plot_dic.values())
            for i in plot_dic.keys():
                current_error = abs(f_ridge(plot_dic[i]) - f_min) / f_min
                plot_dic[i] = current_error
            return {"结果": x0, "迭代步数": t, "次数-误差": plot_dic}
def prox_gd(A,b,x,lam,f_type):
    step = 0.000008
    t = 0
    x0 = x
    plot_dic = {0:x0}
    while t < 3000:
        if f_type == 1:
            temp = x0-step*(np.dot(A.T, (np.dot(A, x0)-b)))
            xt = np.maximum(np.maximum(temp,-temp)-step*lam, 0)*np.sign(temp)
        elif f_type == 2:
            temp = x0-step*(np.dot(A.T,(np.dot(A,x0)-b)))
            xt = np.maximum(np.maximum(temp,-temp)-step*lam,0)*temp
        else:
            return "错误！"
        x0 = xt
        t += 1
        plot_dic[t] = x0
    if f_type == 1:
        f_min = min(f_sub(i) for i in plot_dic.values())
        for i in plot_dic.keys():
            current_error = abs(f_sub(plot_dic[i])-f_min)/f_min
            plot_dic[i] = current_error
        return{"结果":x0,"迭代步数":t,"次数-误差":plot_dic}
    elif f_type == 2:
        f_min = min(f_ridge(i) for i in plot_dic.values())
        for i in plot_dic.keys():
            current_error = abs(f_ridge(plot_dic[i]) - f_min) / f_min
            plot_dic[i] = current_error
        return {"结果": x0, "迭代步数": t, "次数-误差": plot_dic}

def make_plot(result,title):
    plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False    # 解决Matplotlib坐标轴负号'-'显示为方块的问题
    x = result['次数-误差'].keys()
    y = result['次数-误差'].values()
    plt.plot(x, y, "r.-")
    plt.xlabel("迭代步数")
    plt.ylabel("f(xt)-f*")
    plt.title(title)
    plt.show()
#result1 = subgradient_descent(A,b,x_,lam,epsilion, step1)
#result2 = subgradient_descent(A,b,x_,lam,epsilion, step2)
#result3 = subgradient_descent(A,b,x_,lam,epsilion, step3)
#make_plot(result1)
#make_plot(result2)
#make_plot(result3)

result1 = subgradient_descent(A,b,x_,lam,epsilion,step4,f_type=1)
result2 = subgradient_descent(A,b,x_,lam,epsilion,step4,f_type=2)
result3 = prox_gd(A,b,x_,lam,f_type=1)
make_plot(result1,'subgradient_descent,LASSO,lambda='+str(lam))
make_plot(result2,'subgradient_descent,Ridge,lambda='+str(lam))
make_plot(result3,'proximal_gradient_descent,LASSO,lambda='+str(lam))

