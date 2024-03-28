

# #  设 x~N(3,5^2)
# #  solve  P{2<X<6};
# #  确定c ,使得 P{-3c<X<2c}=0.6
# from scipy.stats import norm
# from scipy.optimize import fsolve
# print("p=",norm.cdf(6,3,5)-norm.cdf(2,3,5))
# #  norm.cdf()函数计算了一个正态分布在区间[2, 6]内的概率
# f=lambda c:norm.cdf(2*c,3,5)-norm.cdf(-3*c,3,5)-0.6
# # 方程的目标是找到一个c的值，使得正态分布在区间[-3c, 2c]内的概率减去0.6等于0
# print("c=",fsolve(f,0))
# # 使用fsolve()函数解这个方程，并打印出结果


# from scipy.stats import norm
# from pylab import plot,fill_between,show,text,savefig,rc
# from numpy import array,linspace,zeros
# alpha=array([0.001,0.005,0.01,0.025,0.05,0.10])
# za=norm.ppf(1-alpha,0,1)  #  求上alpha分位数
# print("上alpha分位数分别为",za)
# x=linspace(-4,4,100);y=norm.pdf(x,0,1)
# #  rc('font',size=16);rc('text',usetex=True)
# plot(x,y)   #  画标准正态分布密度曲线
# x2=linspace(za[-1],4,100);y2=norm.pdf(x2);
# y1=[0]*len(x2)
# fill_between(x2,y1,y2,color='r')   #  y1,y2对应的点之间填充
# plot([-4,4],[0,0])  #  画水平线
# text(1.9,0.07,"$\\leftarrow\\alpha\$=0.1")  #  标注
# savefig("figure4_2.png",dpi=500);show()


# # 计算二项分布 b(20,0.8) 的均值与方差
# from scipy.stats import binom
# n,p=20,0.8
# print("期望和方差分布为：",binom.stats(n,p))
#
#
# # 计算二项分布 b(20,0.8) 的均值和方差，偏度的峰度
# from scipy.stats import binom
# n,p=20,0.8
# print("所求的数字特征为：",binom.stats(n,p,moments='mvsk'))

from scipy.integrate import quad
from numpy import exp,sqrt,pi,abs
a=80;b=0.02;BD=a/b;mu=4000;s=100
y=lambda x:x*exp(-(x-mu)**2/(2*s**2))/sqrt(2*pi)/s
# 定义积分的被积函数
I=0;x1=0;x2=10000
while abs(I-BD)>1E-16:
    c=(x1+x2)/2
    I=quad(y,-10000,c)[0]
    #  由3sigma准则这里积分下限取-10000，取0效果一样
    if I>BD: x2=c
    else:x1=c
print("最佳更换周期为：",c)




