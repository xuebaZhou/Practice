


#  泰勒级数

# import numpy as np
# import matplotlib.pyplot as plt
# def fac(n): return (1 if n<1 else n*fac(n-1))
# def item(n,x):return (-1)**n*x**(2*n+1)/fac(2*n+1)
# def mysin(n,x):return (0 if n<0 else mysin(n-1,x)+item(n,x))
# x=np.linspace(-2*np.pi,2*np.pi,101)
# #   从-2π到2π之间取101个等距离的数值，然后用这些数值作为数组的元素值初始化x数组
# plt.plot(x,np.sin(x),'*-')
# #  '*-'：表示使用星号标记点并使用实线连接这些点，用于指定线条的样式。
# str=['v-','H--','-.']
# for n in [1,2,3]:plt.plot(x,mysin(2*n-1,x),str[n-1])
# plt.legend(['sin','n=1','n=3','n=5'])
# plt.savefig('figure3_16.png',dpi=500);plt.show()



#  甲乙丙丁4人初始位置为(-200,200),(200,200),(200,-200),(-200,-200),速率为1m/s，
#  甲始终朝向乙，乙朝向丙，丙朝向丁，丁朝向甲，绘制四人的近似轨迹
# import numpy as np,numpy.linalg as ng
# import matplotlib.pyplot as plt
# N=4;v=1.0;d=200.0;time=400.0;divs=201
# xy=np.array([[-d,d],[d,d],[d,-d],[-d,-d]])  #  记录四个人初始的区域
# T=np.linspace(0,time,divs)  #得到一个名为T的一维数组，其中包含了从0到time的等间隔的数据点，总共有divs个数据点
# dt=T[1]-T[0]   #  在前面时，T数组中的数据分的很细，在该时间段内可以近似为速度方向是不变的
# xyn=np.empty((4,2))# 得到一个名为xyn的空数组，它由4行2列组成
# Txy=xy
# for n in range(1,len(T)):
#     for i in [0,1,2,3]:
#         j=(i+1)%4 # 表示前一个位置变成了后一个位置，例如：甲指向乙，值模4表示最后一个指向第一个
#         dxy=xy[j]-xy[i] # 得到向量的方向
#         dd=dxy/ng.norm(dxy)  # 计算向量dxy的单位向量，np.norm()函数来计算向量dxy的范数（即向量的长度）
#         xyn[i]=xy[i]+v*dt*dd;# 计算下一步的位置，增加的方向就是单位向量dd的方向
#     Txy=np.c_[Txy,xyn];xy=xyn.copy()
#     #将变量 xyn 按列连接到变量 Txy 中，并将变量 xyn 的值复制给变量 xy。
# for i in range(N):plt.plot(Txy[i,::2],Txy[i,1::2])
# plt.savefig("figure3_17.png",dpi=500);plt.show()


#  一重积分  数值积分——梯形公式和Simpson公式
#  https://blog.csdn.net/weixin_45812669/article/details/116719598#:~:text=%E6%A2%AF%E5%BD%A2%E5%85%AC%E5%BC%8F%EF%BC%9A%20I%20%28f%29%20%3D%20%E2%88%AB%20ab%20f%20%28x%29dx,%2A%20f%28a%29%20%2B%20%281%2F2%29%20%2A%20f%28b%29%29%20return%20y

import numpy as np
from scipy.integrate import quad
def trapezoid(f,n,a,b):  # 定义梯形公式的函数
    xi=np.linspace(a,b,n);h=(b-a)/(n-1)
    return h*(np.sum(f(xi))-(f(a)+f(b))/2)
def simpson(f,n,a,b):   # 定义辛普森公式的函数，先推导出数学公式，再转换为代码形式
    xi,h=np.linspace(a,b,2*n+1),(b-a)/(2.0*n)
    xe=[f(xi[i]) for i in range(len(xi)) if i%2==0]
    xo = [f(xi[i]) for i in range(len(xi)) if i % 2 != 0]
    return h*(2*np.sum(xe)+4*np.sum(xo)-f(a)-f(b))/3.0
a=0;b=1;n=1000
f=lambda x:np.sin(np.sqrt(np.cos(x)+x**2))
print("梯形积分I1=",trapezoid(f,n,a,b))
print("辛普森积分I2=",simpson(f,n,a,b))
print("SciPy积分I3=",quad(f,a,b))




#  多重积分  使用SciPy库中的  dblquad,tplquad
#  dblquad(func,a,b,gfun,hfun,args=(),epsabs=1.49-08,epsrel=1.49e-08)
#  其中，被积函数func的格式为func(y,x),最外层x的积分区间为[a,b],内层y的积分区间为[dfun(x),hfun(x)]

# tplquad(func,a,b,gfun,hfun,qfun,rfun,args=(),epsabs=1.49e-08,epsrel=1.49e-08)
#  其中，被积函数func的格式为func(z,y,x),最外层x的积分区间为[a,b],中间层y的积分区间为[dfun(x),hfun(x)]，最内层z
#  的积分区间为[qfun(x,y),rfun(x,y)]


import numpy as np
from scipy.integrate import dblquad
f1=lambda y,x:x*y**2
print("I1:",dblquad(f1,0,2,0,1))
f2=lambda y,x:np.exp(-x**2/2)*np.sin(x**2+y)
bd=lambda x:np.sqrt(1-x**2)
print("I2:",dblquad(f2,-1,1,lambda x:-bd(x),bd))


import numpy as np
from scipy.integrate import tplquad
f=lambda z,y,x:z*np.sqrt(x**2+y**2+1)
ybd=lambda x:np.sqrt(2*x-x**2)
print("I=",tplquad(f,0,2,lambda x:-ybd(x),ybd,0,6))



#  求方程x^3+1.1x^2+0.9x-1.4=0的实根近似值，误差不超过10^-6
import numpy as np
from scipy.optimize import fsolve
def binary_search(f,eps,a,b): # 二分法函数
    c=(a+b)/2
    while np.abs(f(c))>eps:
        if  f(a)*f(c)<0:b=c
        else:a=c
        c=(a+b)/2
    return c
def newton_iter(f,eps,x0,dx=1E-8): # 牛顿迭代法函数
    #https://zhuanlan.zhihu.com/p/240077462
    def diff(f,dx=dx): # 求数值导数函数
        return lambda x:(f(x+dx)-f(x-dx))/(2*dx)
    df=diff(f,dx)
    x1=x0-f(x0)/df(x0)
    while np.abs(x1-x0)>=eps:
        x1,x0=x1-f(x1)/df(x1),x1
    return x1
f=lambda x:x**3+1.1*x**2+0.9*x-1.4
print("二分法求得的根为:",binary_search(f,1E-6,0,1))
print("牛顿迭代法求得的根为:",newton_iter(f,1E-6,0))
#  fsolve函数   https://zhuanlan.zhihu.com/p/136889381
print("直接调用SciPy求得的根为:",fsolve(f,0))




#  用fsolve函数求非线性方程组的数值解
#  5*x2+3=0
#  4*x1**2-2sin(x2*x3)=0
#  x2*x3-1.5=0
from numpy import sin
from scipy.optimize import fsolve
f=lambda x:[5*x[1]+3,4*x[0]**2-2*sin(x[1]*x[2]),x[1]*x[2]-1.5]
print("result=",fsolve(f,[1.0,1.0,1.0]))




from numpy import sin
from scipy.optimize import fsolve
def Pfun(x):
    x1,x2,x3=x.tolist()
    return 5*x2+3,4*x1**2-2*sin(x2*x3),x2*x3-1.5
print("result=",fsolve(Pfun,[1.0,1.0,1.0]))
# https://blog.csdn.net/weixin_41140174/article/details/108993828


# 一元函数的极值点
# 求函数f(x)=e^xcos(2x)在区间[0,3]上的极小点
from numpy import exp,cos
from scipy.optimize import fminbound
f=lambda x:exp(x)*cos(2*x)
x0=fminbound(f,0,3)
print("极小点为：{},极小值为：{}".format(x0,f(x0)))



#  求上述函数在0附近的一个极小值点
from numpy import exp,cos
from scipy.optimize import fmin
f=lambda x:exp(x)*cos(2*x)
x0=fmin(f,0)
print("极小点为：{},极小值为:{}".format(x0,f(x0)))



#  多元函数的极值点
#  minimize(fun,x0,args=(),method=None)
#  求函数f(x)=100(x2-x1^2)^2+(1-x1)^2的极小值
from scipy.optimize import minimize
f=lambda x: 100*(x[1]-x[0]**2)**2+(1-x[0])**2
x0=minimize(f,[2.0,2.0])
print("极小点为：{},极小值为:{}".format(x0.x,x0.fun))







