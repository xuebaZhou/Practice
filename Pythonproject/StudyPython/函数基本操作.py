

#   自定义函数
#  语法如下：
# def functionName(formalParameters):
#     functionBody
#     (1) functionName是函数名，可以是任何有效的Python标识符.
#     (2) formalParameters是形参列表，圆括号和冒号是不能少的
#     (3) functionBody 是函数体，多个语句的函数体要注意缩进
#  函数体的内容不能为空，可以用pass来表示空语句       函数定义要放在函数的调用前面

# def factorial(n):
#     r=1
#     while n>1:r*=n;n-=1
#     return r
# a=int(input("please input a number:"))
# #input就是个万能输入，不过input输入的元素都是以str形式保存的，如果要他作为一个整数的话，就需要进行数据类型转换。
# print(factorial(a))

#  Python自定义函数的四种参数
#  1、位置参数：采用按位置匹配的方式，实参的数目应与形参完全匹配
def greet(name,age):
    print(f"Hello {name}! You are {age} years old.")
# f是Python 3.6引入的一种格式化字符串的方式。
# f表示使用f-string（格式化字符串字面值），它允许在字符串中插入变量或表达式的值，而无需使用其他字符串拼接的方式。
# 在字符串前面添加f，然后在字符串中使用大括号{}包裹变量或表达式即可。

# 调用参数并传递位置参数
greet("Kobe",42)

#  2、默认参数
#  在构造自定义函数时已经给某些参数赋予了各自的初值 ，默认参数必须指向不变对象
#  计算1到n的p次方和
def square_sum(n,p=2):
    result=sum([i**p for i in range(1,n+1)])  # sum是内置函数
    return (n,p,result)
print(f"1到%d的%d次方和为%d"%square_sum(10))
print(f"1到%d的%d次方和为%d"%square_sum(10,3))

#  3、可变参数
#  不确定该给自定义函数传入多少个参数值时，需要Python提供可变参数
def add(a,b):s=sum([a,b]);return(a,b,s)
print(f"%d加%d的和为%d"%add(10,13))

#  要求任意个数的和，必须使用可变参数，可变参数允许传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个元组
def add(*args): print(args,end=" ");s=sum(args);return(s)
print(f"的和为%d"%add(10,12,6,8))
#   在参数args前面加了一个星号*，这样的参数就是可变参数，该参数可以接纳任意多个实参的。
#  该参数类型将输入的实参进行了捆绑，并且组装到元组中


#  4、关键字参数
#   把带参数名的参数值组装到一个字典中，键就是具体的实参名，值就是传入的参数值
def person(name,age,**kw):
#   name和 age是位置参数，kw为关键字参数、
# 调用函数时，name和age两个参数必须要传入对应的值，而其他的参数都是用户任意填写的，
# 而且关键字参数会把这些任意填写的信息组装为字典
    print('name:',name,'age:',age,'other:',kw)
person('Michale',30)
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')



#  参数传递
#  1、传值调用： 在函数中对参数值所做的任何修改都不会影响原来的自变量值
#   传递的数据是不可变的对象时在传递参数时，会先复制一份再进行传递
def fun(a,b):
    a,b=b,a;
    print("函数内交换数值后:a=%d,\tb=%d"%(a,b))
a=10;b=15
print("调用函数前的数值:a=%d,\tb=%d"%(a,b))
print('-------------------------------')
fun(a,b)  #调用函数
print("调用函数后的数值:a=%d,\tb=%d"%(a,b))
print('-------------------------------')


#  2、传址调用：  所传递函数的参数值是变量的内存地址，参数值的变动连带着也会影响原来的自变量值
#  因为占用了同一个地址，所以会连带影响函数外部的值
def change(data):
    data[0],data[1]=data[1],data[0]
#  在函数内部，通过对data列表进行索引操作，将索引为0和1的元素进行交换。
    print("函数内交换位置后:",end='')
    for i in range(2):print("data[%d]=%2d"%(i,data[i]),end='\t')
#   上面是函数的定义
#   在主程序中创建了一个名为data的列表，并初始化为[16, 25]。
data=[16,25]
print("原始数据为: ",end='')
for i in range(2):print("data[%d]=%2d"%(i,data[i]),end='\t')
print("\n--------------------------------------------------------")
change(data)
#    调用change函数，并传入data列表作为参数。此步骤将会修改data列表内的元素位置。
print("\n--------------------------------------------------------")
print("排序后的数据为: ",end='')
for i in range(2):print("data[%d]=%2d"%(i,data[i]),end='\t')


#  参数传递的复合数据解包
#   传递参数时，可以使用Python列表、元组、集合、字典以及其他可迭代对象作为实参，并在实参名称前加一个星号，
# Python解释器将自动进行解包，然后传递给多个单变量形参
def fun(a,b,c):print("三个数的和为:",a+b+c)
seq=[1,2,3]; fun(*seq)   #  列表解包
tup=(1,2,3); fun(*tup)   #  元组解包
dic={1:'a',2:'b',3:'c'}; fun(*dic)
dic2={'a':4,'b':5,'c':6}; fun(**dic2)   #  字典解包
set={1,2,3};fun(*set)

#  两个特殊函数

# 1、匿名函数：没有函数名的简单函数，只可以包含一个表达式。表达式的结果作为函数的返回值

f=lambda a,b=2,c=5:a-b+c  #  使用默认值参数
print("f=",f(10,20))
print("f=",f(10,20,30))
print("f=",f(c=20,a=10,b=30))    #  使用关键字实参


f=lambda n,m:sum([k**m for k in range(1,n+1)])
s=f(100,1)+f(50,2)+f(10,-1)
print("s=%10.4f"%(s))


#  2、递归函数：  分为直接递归和间接递归（会增加时间开销）

# 通过递归求n！
# n=int(input("请输入n的值："))
# def fac(n):
#     if n<=1:return 1
#     else:return n*fac(n-1)
# m=fac(n)
# print("%d!=%5d"%(n,m))


# x,n=eval(input("请输入x和n的值:"))
# def p(x,n):
#     if n==1:return x
#     else :return x*(1-p(x,n-1))
# v=p(x,n)
# print("p(%d,%d)=%d"%(x,n,v))


#  导入模块

#  要查看所有模块，可以使用命令   help("modules")
#  要查看math模块的帮助，可以使用命令  import math;help(math)
#  要查看math模块的所有函数，可以使用命令  import math ;print(dir(math))

#  1.import，模块名[as 别名]
#  使用时需要在对象之前加上模块名作为前缀 即"模块名.对象名"或者"别名.对象名"
import numpy as np  #  导入numpy库，相当于大模块，并设置别名np
import numpy.linalg as LA  # 导入numpy库下linalg（线性代数）模块，别名为LA
a=np.linspace(0,10,5)  # 产生0到10之间等间距的5个数
b=LA.norm(a)  #  求b的模，即向量a的长度
print("a的长度为:%7.4f"%b)

#  import time , random # 导入基础库中的time和random模块

#  2.from 模块名 import 对象名 [as 别名]
#  这种导入方式可以减少查询次数，提高访问速度，也可以减少输入的代码量
from numpy import random as rd  #从numpy库中导入模块random并设置别名为rd
from math import sin,cos   #导入模块中的正弦函数和余弦函数
from random import randint
a=rd.randint(0,10,(1,3))  # 产生[0,10)的三个元素的随机整数数组
b=randint(0,10)   # 产生[0,10]上的一个随机整数，不能产生向量
print("sin(b)=%6.4f"%sin(b))
print("cos(b)=%6.4f"%cos(b))
#  import random 是导入Python基础库的random模块，
# 而import numpy.random是导入NumPy库中的random模块（建议使用，因为可以对向量进行运算）


#   3.from 模块名 import *
# 一次导入库或模块中的所有对象（不建议使用）
from math import log ,exp,sin,pi
f=lambda n:(1+log(n)+sin(n))/(2*pi)
y=exp(2)
for n in range(1,101):y+=f(n)
print("y=%7.4f"%y)


#  自定义模块的导入
import FunctionSet as fs
print(fs.f(1),'\t',fs.g(2),'\t',fs.h(3))

from FunctionSet import f,g,h
print(f(1),'\t',g(2),'\t',h(3))














