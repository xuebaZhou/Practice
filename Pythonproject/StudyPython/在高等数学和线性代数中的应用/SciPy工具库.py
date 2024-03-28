
# https://blog.csdn.net/RosebudTT/article/details/105979939#:~:text=python%E4%B9%8Bscipy%E5%BA%93%E8%AF%A6%E8%A7%A3%201%201.%E6%8F%92%E5%80%BC%20%E6%A0%B7%E6%9D%A1%E6%8F%92%E5%80%BC%E6%B3%95%E6%98%AF%E4%B8%80%E7%A7%8D%E4%BB%A5%E5%8F%AF%E5%8F%98%E6%A0%B7%E6%9D%A1%E6%9D%A5%E4%BD%9C%E5%87%BA%E4%B8%80%E6%9D%A1%E7%BB%8F%E8%BF%87%E4%B8%80%E7%B3%BB%E5%88%97%E7%82%B9%E7%9A%84%E5%85%89%E6%BB%91%E6%9B%B2%E7%BA%BF%E7%9A%84%E6%95%B0%E5%AD%A6%E6%96%B9%E6%B3%95%20from%20scipy.interpolate%20import%20interp1d,...%205%205.%E7%A7%AF%E5%88%86%20%EF%BC%881%EF%BC%89%E7%AC%A6%E5%8F%B7%E7%A7%AF%E5%88%86%20%E7%AC%A6%E5%8F%B7%E8%BF%90%E7%AE%97%E5%8F%AF%E4%BB%A5%E7%94%A8%20sympy%20%E6%A8%A1%E5%9D%97%E5%AE%8C%E6%88%90%E3%80%82%20


#  1、二维曲线画图
#  plot(表达式,变量取值范围,属性=属性值)
#  多重绘制的使用格式为
#  plot(表达式1,表达式2,变量取值范围,属性=属性值)
#  或者 plot((表达式1,变量取值范围1),(表达式2,变量取值范围2))

# from sympy.plotting import plot
# from sympy.abc import x,pi
# from sympy.functions import sin,cos
# plot((2*sin(x),(x,-6,6)),(cos(x+pi/4),(x,-5,5)),(sin(x**2),(x,-4,4)))



#  三维曲面画图
# from pylab import rc
# from sympy.plotting import plot3d
# from sympy.abc import x,y
# from sympy.functions import sin,sqrt
# # rc('font',size=16);rc('text',usetex=True)
# plot3d(sin(sqrt(x**2+y**2)),(x,-10,10),(y,-10,10),xlabel='$x$',ylabel="$y$")





#  3、隐函数画图    (x-1)^2+(y-2)^3-4=0

# from pylab import  rc
# from sympy import plot_implicit as pt,Eq
# from sympy.abc import x,y
# pt(Eq((x-1)**2+(y-2)**3,4),(x,-6,6),(y,-2,4),xlabel='$x$',
#    ylabel='$y$')


#  使用匿名函数设计
from sympy import plot_implicit as pt
from sympy.abc import x,y
ezplot=lambda  expr:pt(expr)
#这段代码中 `ezplot=lambda expr:pt(expr)` 是一个 lambda 函数，用于生成一个基于点集的散点图。
#该函数接受一个表达式 `expr` 作为输入，并使用 `pt()` 函数将其转换为点集。
# `pt()` 函数是 Matplotlib 库中的一个函数，用于绘制散点图。
#因此，这段代码的作用是将给定的表达式转换为散点图，并将其显示在图形界面上。
ezplot((x-1)**2+(y-2)**3-4)









