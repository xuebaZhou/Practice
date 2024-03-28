
#
# #  在符号矩阵运算中  *表示矩阵的乘积  **表示矩阵的幂运算
#
# import sympy as sp
# A=sp.Matrix([[1],[2],[3]])  # 列向量,即3×1矩阵
# B=sp.Matrix([[4],[5],[6]])
# print("A的模为：",A.norm())
# print("A的模的浮点数为：",A.norm().evalf())
# print("A的转置矩阵为：",A.T)
# print("A and B 的点乘为：",A.dot(B))
# print("A and B 的叉乘为：",A.cross(B))
#
# # 看SymPy库中矩阵操作的一些方法或函数使用如下帮助：
# # from sympy import Matrix
# # help(Matrix)
#
# import sympy as sp
# import numpy as np
# A=sp.Matrix(np.arange(1,17).reshape(4,4))
# B=sp.eye(4) # 生成四阶单位矩阵
# print("A的行列式为：",sp.det(A))
# print("A的秩为：",A.rank())
# print("A的转置矩阵为：",A.transpose()) # 等价于A.T
# print("所求的逆阵为：",(A+10*B).inv())  # inv  计算方阵(A+10*B)的逆
# print("A的平方为：",A**2)
# print("A,B的乘积为：",A*B)
# print("横连矩阵为：",A.row_join(B))
# print("纵连矩阵为：",A.col_join(B))
# print("A1为：",A[0:2,0:2])  # 提出A的左上角子块构成的矩阵
# A2=A.copy();A2.row_del(3)  # 删除A的第四行得到的矩阵
# print("A2为：",A2)
#
#
# import sympy as sp
# A=sp.Matrix([[2,1,-5,1],[1,-3,0,-6],[0,2,-1,2],[1,4,-7,6]])
# b=sp.Matrix([8,6,-2,2]);b.transpose()
# print("系数矩阵A的秩为：",A.rank())
# print("线性方程组的唯一解为：",A.inv()*b)
#
#
#
# import sympy as sp
# A=sp.Matrix([[1,-5,2,-3],[5,3,6,-1],[2,4,2,1]])
# print("A的零空间(基础解系)为：",A.nullspace())
#
#
#
# import sympy as sp
# A=sp.Matrix([[1,1,-3,-1],[3,-1,-3,4],[1,5,-9,-8]])
# b=sp.Matrix([1,4,0]);b.transpose()     # 等价于 b=sp.Matrix([[1],[4],[0]])
# C=A.row_join(b)
# print("增广矩阵的行最简形为：\n",C.rref())   # rref()把增广矩阵化成行最简形
#
#
# import sympy as sp
# A=sp.Matrix([[0,-2,2],[-2,-3,4],[2,4,-3]])
# print("A的特征值为：",A.eigenvals())
# #  A的特征值为： {-8: 1, 1: 2} 代表-8是一重根，1是二重根
# print("A的特征向量为：",A.eigenvects())
#
#
#
#
# from sympy import Matrix,diag
# A=Matrix([[0,-2,2],[-2,-3,4],[2,4,-3]])
# if A.is_diagonalizable():print("A的对角化矩阵为：\n",A.diagonalize())
# else:print("A不能相似对角化")
#
#
#
# from numpy import arange,cross,inner
# from numpy.linalg import norm
# a=arange(1,4);b=arange(4,7)  # 创建数组
# print("a的二范数为：",norm(a)) # 1范数 ：所有元素绝对值的和。 2范数 ：所有元素平方和的开方。
# print("a点乘b=",a.dot(b))  # 行向量a乘以列向量b
# print("a,b的内积=",inner(a,b))  # is equal to   dot(a,b)
# print("a叉乘b=",cross(a,b))


#  求解超定线性方程组
# import numpy as np
# import numpy.linalg as LA
# from matplotlib.pyplot import plot,rc,legend,show,savefig
# x=np.array([0,1,2,3])
# y=np.array([-1,0.2,0.9,2.1])
# A=np.c_[x,np.ones_like(x)]
# m,c=LA.lstsq(A,y,rcond=None)[0]
# #  使用 LA.lstsq 函数进行最小二乘拟合，得到拟合直线的斜率和截距 m 和 c
# print(m,c);rc("font",size=16)
# plot(x,y,'o',label="原始数据",markersize=5)
# plot(x,m*x+c,'r',label='拟合直线')
# rc('font',family="SimHei")  # 用来正常显示中文标签
# rc('axes',unicode_minus=False)  #  用来正常显示负号
# legend();savefig("figure3_41.png",dpi=500);show()


import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
t=np.arange(8)
y=np.array([27.0,26.8,26.5,26.3,26.1,25.7,25.3,24.8])
A=np.c_[t,np.ones_like(t)]
#  A 是一个由两个数组 t 和 np.ones_like(t) 按列合并而成的矩阵
ab=LA.lstsq(A,y,rcond=None)[0] #  返回值为向量
# rcond 参数的值为 None，表示使用默认的条件
print(ab);plt.rc('font',size=16) # 设置字体的大小为 16
plt.plot(t,y,'o',label='Original data',markersize=5)
#  使用 plt.plot 方法绘制原始数据，数据点以圆圈形式显示，并标注为 “Original data”，数据点的大小为 5
plt.plot(t,A.dot(ab),'r',label='Fitted line')
#  使用 plt.plot 方法绘制拟合的直线，颜色为红色，并标注为 “Fitted line”
#  拟合的直线是通过计算 A 矩阵与 ab 向量的乘积来得到的
plt.legend();plt.savefig("figure3_42.png",dpi=500);
plt.show()















