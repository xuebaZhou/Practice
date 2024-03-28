#   linprog的基本调用格式为：
# from scipy.optimize import linprog
# res=linprog(c,A,b,Aeq,beq)   默认每个决策变量下界为0，上界为+oo
# res=linprog(c,A=None,b=None,Aeq=None,beq=None,bounds=None,method='simplex')
# print(res.fun)    显示目标函数最小值
# print(res.x)      显示最优解


#  求 min z=-x1+4x2
#   -3x1+x2<=6
#   x1+2x2<=4
#   x2>=-3
# from scipy.optimize import linprog
# c=[-1,4];A=[[-3,1],[1,2]]
# b=[6,4];bounds=((None,None),(-3,None))
# res=linprog(c,A,b,None,None,bounds)
# print("目标函数的最小值：",res.fun)
# print("最优解为：",res.x)

import numpy as np


def f(n, a, x):
    p = a[0]
    for i in range(1, n + 1):
        p += (a[i] * pow(x, i))
    return p


a = np.array([2, 3, 4, 6])
print(f(3, a, 2))
