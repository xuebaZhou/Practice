# 在 scipy.stats 模块中，伽马分布的概率密度函数的调用格式为
# gamma.pdf(x,a,loc=0,scale=1)
# from pylab import plot,legend,xlabel,ylabel,savefig,show,rc
# from scipy.stats import gamma
# from numpy import linspace
# x=linspace(0,15,100)#;rc=('font',size=15)
# plot(x,gamma.pdf(x,4,0,2),'r*-',label="$\\alpha=4,\\beta=2$")
# plot(x,gamma.pdf(x,4,0,1),'bp-',label="$\\alpha=4,\\beta=1$")
# plot(x,gamma.pdf(x,4,0,0.5),'.k-',label="$\\alpha=4,\\beta=0.5$")
# plot(x,gamma.pdf(x,2,0,0.5),'>g-',label="$\\alpha=2,\\beta=0.5$")
# 这句代码是用于绘制一个以x为横坐标，以gamma分布函数为纵坐标的图像。
# gamma分布函数的参数为alpha=2和beta=0.5。">g-"表示使用绿色的箭头线来绘制图像。
# "$\\alpha=2,\\beta=0.5$"是图例标签，用于说明绘制的曲线所代表的含义。

# legend();xlabel('$x$');ylabel("$f(x)$",rotation=9)
# savefig("figure2_46.png",dpi=500);show()


#  把四个不同正态分布的密度函数画在4个子窗口中
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import norm
# mu0=[-1,0];s0=[0.5,1]
# x=np.linspace(-7,7,100)#;plt.rc('font',size=15)
# #plt.rc('text',usetex=True);plt.rc('axes',unicode_minus=False)
# f,ax=plt.subplots(len(mu0),len(s0),sharex=True,sharey=True)
# # 这段代码是使用Matplotlib库创建一个图形，其中包含多个子图，每个子图都代表一个不同的数据集。
# # 具体来说，代码中的`f`代表整个图形，`ax`代表每个子图。
# # `plt.subplots`函数用于创建一个网格，其中`len(mu0)`和`len(s0)`分别代表每个子图所需的数据点的数量。
# # `sharex=True`和`sharey=True`表示所有子图共享X轴和Y轴，即它们共享相同的坐标轴。
# # 这个代码片段通常用于在同一个图形中展示多个数据集的拟合结果，以便进行比较和评估。
# for i in range(2):
#     for j in range(2):
#         mu=mu0[i];s=s0[j]
#         y=norm(mu,s).pdf(x)
#         ax[i,j].plot(x,y)
#         ax[i,j].plot(1,0,label='$\\mu$={:3.2f}\n$\\sigma$={:3.2f}'.format(mu,s))
#         ax[i,j].legend(fontsize=12)
# ax[1,1].set_xlabel("$x$")
# ax[0,0].set_ylabel("pdf($x$)")
# plt.savefig('figure2_47.png');plt.show()


# 二项分布b(5,0.4)的分布图
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

n, p = 5, 0.4
x = np.arange(6);
y = binom.pmf(x, n, p)
#  n 和 p 是二项分布中的参数，即n表示试验次数，p表示每次试验成功的概率。
# 因此，通过计算x中每个元素的概率值，可以得到二项分布中每个成功次数的概率。
plt.subplot(1, 2, 1);
plt.plot(x, y, 'ro')
plt.vlines(x, 0, y, 'k', lw=3, alpha=0.5)
#  vlines(x,ymin,ymax)画竖线图
#  lw设置线宽度，alpha设置图的透明度
plt.subplot(1, 2, 2);
plt.stem(x, y, use_line_collection=True)
# 这段代码是使用matplotlib库中的stem函数绘制离散数据的图形。
# stem函数的输入参数x和y分别表示离散数据点的横坐标和纵坐标，
# use_line_collection=True表示使用LineCollection对象来绘制线条。
# 具体的绘制效果会将每个离散数据点用垂直的线段连接起来，
# 并且在每个数据点上方绘制一个小箭头，以便于更好地展示数据的变化情况。
plt.savefig("figure2_48.png", dpi=500);
plt.show()
