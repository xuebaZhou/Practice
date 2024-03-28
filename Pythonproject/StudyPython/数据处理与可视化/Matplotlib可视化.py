

# import numpy as np,pandas as pd
# from matplotlib.pyplot import *
# a=np.genfromtxt("Pdata2_21.txt",max_rows=6,usecols=range(8))
# c=np.array([1,2,3]);width=0.2
# rc('font',size=16);bar(ind,c,width);ylabel("成绩分布")
# xticks(ind,['A','B','C'],rotation=20)
# rcParams['font.sans-serif']=['SimHei']
# savefig('figure2_36.png',dip=500)
# show()

#  散点图
# import numpy as np
# from matplotlib.pyplot import *
# x=np.array(range(8))
# y='27.0 26.8 26.5 26.3 26.1 25.7 25.3 24.8'
# y=",".join(y.split())  # 把空格替换成逗号
# y=np.array(eval(y))    # 数据之间加逗号太麻烦，用程序转换
# scatter(x,y)
# savefig('figure2_23.png',dpi=500) # 保存图片为文件，像素为500
# show()


#  多个图形显示在一个图形画面
# import numpy as np
# from matplotlib.pyplot import *
# x=np.linspace(0,2*np.pi,200)
# y1=np.sin(x);y2=np.cos(pow(x,2))
# #rc('font',size=16);rc('text',usetex=True)      #  调用tex字库
# # 要使用LaTeX格式需要安装LaTeX的两个宏包basic-miktex-2.9.7021x64和gs926aw64.否则把这段语句注释掉
# plot(x,y1,'r',label='$sin(x)$',linewidth=2)
# #  'r'代表红色，'b--'代表蓝色加上虚线  label添加折线图的标签  linewidth指定折线的宽度
# plot(x,y2,'b--',label='$cos(x^2)$')
# xlabel('$x$');ylabel('$y$',rotation=0)  #  横坐标显示x，纵坐标显示y，并且y旋转0度
# savefig('figure2_38.png',dpi=500)
# legend()
# show()



#  多个图形单独显示
# import numpy as np
# from matplotlib.pyplot import *
# x=np.linspace(0,2*np.pi,200)
# y1=np.sin(x);y2=np.cos(x);y3=np.sin(x*x)
# ax1=subplot(2,2,1)  # 新建左上1号子窗口
# ax1=plot(x,y1,'r',label='$sin(x)$');legend() # 添加图例
# ax2=subplot(2,2,2)  # 新建右上2号子窗口
# ax2=plot(x,y2,'b--',label='$cos(x)$');legend()
# ax3=subplot(2,1,2)  # 新建2行、1列的下面子窗口
# ax3=plot(x,y3,'k--',label='$sin(x^2)$');legend()
# savefig('figure2_39.png',dpi=500);show()


#   三维空间的曲线
#  画出三维曲线 x=tsint,y=tcost,z=t(t取值范围为[0,100])的图形
# from mpl_toolkits import mplot3d
# import matplotlib.pyplot as plt
# import numpy as np
# ax=plt.axes(projection='3d')  # 设置三维图形模式
# z=np.linspace(0,100,1000)
# x=np.sin(z)*z;y=np.cos(z)*z
# ax.plot3D(x,y,z,'k')
# plt.savefig('figure2_40.png',dpi=500);plt.show()



#   https://zhuanlan.zhihu.com/p/66306575   用Python的Matplotlib模块绘制3D图像
# from mpl_toolkits import mplot3d
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(-6,6,30)
# y=np.linspace(-6,6,30)
# X,Y=np.meshgrid(x,y)
# Z=np.sin(np.sqrt(X**2+Y**2))
# ax1=plt.subplot(1,2,1,projection='3d')
# ax1.plot_surface(X,Y,Z,cmap='viridis')
# ax1.set_xlabel('x');ax1.set_ylabel('y');ax1.set_zlabel('z')
# ax2=plt.subplot(1,2,2,projection='3d')
# ax2.plot_wireframe(X,Y,Z,color='c')
# ax2.set_xlabel('x');ax2.set_ylabel('y');ax2.set_zlabel('z')
# plt.savefig('figure2_41.png',dpi=500);plt.show()


#   等高线图





#   向量图
# import matplotlib.pyplot as plt
# from numpy import *
# x=linspace(0,15,11);y=linspace(0,10,12)
# x,y=meshgrid(x,y)   #  生成网格数据
# v1=y*cos(x);v2=y*sin(x)
# plt.quiver(x,y,v1,v2)
# plt.savefig('figure2_43.png',dpi=500);plt.show()




# import numpy as np
# from matplotlib.pyplot import *
# x=np.linspace(0,2*np.pi,200)
# #这是一个使用NumPy库生成一个包含200个点的等间隔线形数组的例子。该数组的取值范围从0到2π，步长为0.01。
# #这个数组可以用来表示一个在[0, 2π]区间内周期为2π的函数。
# y1=np.sin(x);y2=np.cos(x);y3=np.sin(x*x);y4=x*np.sin(x)
# ax1=subplot(2,3,1)  #  新建左上1号子窗口
# #  create a subplot with two rows and three columns,
# #  and the first subplot is created in the first row and the first column.
# ax1.plot(x,y1,'r',label='$sin(x)$');legend()
# ax2=subplot(2,3,2)  #  新建2号子窗口
# ax2.plot(x,y2,'y--',label='$cos(x)$');legend()
# ax3=subplot(2,3,(3,6))  #  3，6子窗口合并
# ax3.plot(x,y3,'k-.',label='$sin(x^2)$');legend()
# ax4=subplot(2,3,(4,5))  #  4,5号子窗口合并
# ax4.plot(x,y4,'c--',label='$sin(x)$');legend()
# savefig('figure2_44.png',dpi=500);show()









