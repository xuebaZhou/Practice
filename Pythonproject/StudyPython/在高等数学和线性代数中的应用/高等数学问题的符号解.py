#
#
# #  1、求极限
# from sympy import *
# x=symbols('x')
# print(limit(sin(x)/x,x,0))
# print(limit(pow(1+1/x,x),x,oo))  # 这里的  oo  表示正无穷
#
# # 2、求导数
# from sympy import *
# x,y=symbols('x y')
# z=sin(x)+x**2*exp(y)
# # diff(func,x,n)
# # 其中，func是要求导的函数，x是要对其求导的变量，n是可选的，表示求n阶导数，默认为1阶导数。
# print("关于x的二阶偏导数为：",diff(z,x,2))
# print("关于y的一阶偏导数为：",diff(z,y))
# print("关于x的二阶偏导数,再关于y的二阶偏导数为：",diff(z,x,2,y,2))
#
#
#
#
# #  将导数带入具体的值求某一点处的导数
# from sympy import *
# def func(x):
#     return x**4
# x = symbols("x")
# print(diff(func(x),x).subs(x,2))   # 表示将x = 2，带入导函数4*x**3中
#
#
#
#
#
# # 3、级数的求和
# from sympy import *
# k,n=symbols('k n')
# print(summation(k**2,(k,1,n)))
# print(factor(summation(k**2,(k,1,n))))
# # 把计算结果因式分解
# print(summation(1/k**2,(k,1,oo)))
# # 这里是两个小“o”表示正无穷
#
#
# #  4、泰勒展开
# from pylab import rc
# from sympy import *
# from sympy.plotting import *
# # rc('font',size=16);rc('text',usetex=True)
# x=symbols('x');y=sin(x)
# # 定义了两个符号变量 x 和 y，其中 y 是一个三角函数的表达式。
# for k in range(3,8,2):
# # 使用 for 循环从 3 到 7（步长为 2）遍历每个整数 k。
#     print(y.series(x,0,k)) # 等价于print(series(y,x,0,k))
# # 在循环内部，使用 print 函数打印出 y 在给定的自变量 x 取值范围内的一系列近似表达式，直到取值达到 k。
# plot(y,series(y,x,0,3).removeO(),series(y,x,0,5).removeO(),
#      series(y,x,0,7).removeO(),(x,0,2),xlabel='$x$',ylabel="$y$")
# #使用 plot 函数绘制 y 的曲线，其中包括使用 series 函数计算的从 k=0 到 k=3、k=5 和 k=7 的近似表达式，
# # 以及在自变量 x 取值范围为 0 到 2 的区间内的数据点。
# # 使用 xlabel 和 ylabel 函数设置坐标轴标签。
#
#
# #  5、不定积分和定积分
# #  https://www.cnblogs.com/Yanjy-OnlyOne/p/11185582.html
# from sympy import integrate,symbols,sin,pi,oo
# x=symbols('x')
# print(integrate(sin(2*x),(x,0,pi)))
# print(integrate(sin(x)/x,(x,0,oo)))
#

#  6、 求解代数方程（组）的符号解
# x,y=symbols('x y')
# print(solve(x**3-1,x))  #  解出来的解有虚数解
# print(solve((x-2)**2*(x-1)**3,x))
# print(roots((x-2)**2*(x-1)**3,x)) # roots可以得到根的重数信息
#
#
#
# from sympy.abc import x,y
# from sympy import solve
# s=solve([x**2+y**2-1,x-y],[x,y])
# print("方程组的解为: ",s)
#
#
#
# #  求函数f(x)=2x^3-5x^2+x的驻点，并求函数在[0,1]上的最大值
# from sympy import *
# x=symbols('x');y=2*x**3-5*x**2+x
# x0=solve(diff(y,x),x) #求导后再求驻点
# print("驻点的精确解为：",x0)
# print("驻点的浮点数表示为：",[x0[i].n()for i in range(len(x0))])
# # 列表中的符号数无法整体转换为浮点数
# y0=[y.subs(x,0),y.subs(x,1),y.subs(x,x0[0]).n()]
# # 带入区间端点和一个驻点的值
# print("三个点的函数值分别为：",y0)
# from sympy import *
# x,y=symbols('x y')
# print(solve(x**3-1,x))  #  解出来的解有虚数解
# print(solve((x-2)**2*(x-1)**3,x))
# print(roots((x-2)**2*(x-1)**3,x)) # roots可以得到根的重数信息
#
#
#
# from sympy.abc import x,y
# from sympy import solve
# s=solve([x**2+y**2-1,x-y],[x,y])
# print("方程组的解为: ",s)
#
#
#
# #  求函数f(x)=2x^3-5x^2+x的驻点，并求函数在[0,1]上的最大值
# from sympy import *
# x=symbols('x');y=2*x**3-5*x**2+x
# x0=solve(diff(y,x),x) #求导后再求驻点
# print("驻点的精确解为：",x0)
# print("驻点的浮点数表示为：",[x0[i].n()for i in range(len(x0))])
# # 列表中的符号数无法整体转换为浮点数
# y0=[y.subs(x,0),y.subs(x,1),y.subs(x,x0[0]).n()]
# # 带入区间端点和一个驻点的值
# print("三个点的函数值分别为：",y0)


#  7、求微分方程（方程组）的符号解
# 在SymPy库中有dsolve函数求常微分方程的符号解
# 在声明时，可以使用Function()函数
# y=Function('y') 或者 y=symbols('y',cls=Function) 将符号变量声明为函数类型




# y"-5y'+6y=0;    y"-5y'+6y=xe^2x
from sympy import *
x=symbols('x');y=symbols('y',cls=Function)
eq1=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)
eq2=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)-x*exp(2*x)
print("齐次方程的解为：",dsolve(eq1,y(x)))
print("非齐次方程的解为：",dsolve(eq2,y(x)))





#  求下列微分方程的解
#  y"-5y'+6y=0  y(0)=1,y'(0)=0
#  y"-5y'+6y=xe^2x  y(0)=1,y(2)=0
from sympy import *
x=symbols('x');y=symbols('y',cls=Function)  # 将符号变量y声明为函数类型
eq1=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)
eq2=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)-x*exp(2*x)
print("初值问题的解为：{}".format(dsolve(eq1,y(x),ics={y(0):1,diff(y(x),x).subs(x,0):0})))
# 将初值条件y(0)=1和dy/dx|_(x=0)=0传递给了ics参数
y2=dsolve(eq2,y(x),ics={y(0):1,y(2):0})
print("边值问题的解为：{}".format(y2))



from sympy import *
x=symbols('x');y=symbols('y',cls=Function)
eq1=diff(y(x),x,3)-y(x);
print("符号解为：{}".format(dsolve(eq1,y(x))))


