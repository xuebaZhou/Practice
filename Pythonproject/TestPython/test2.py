

# print(pi)

#   https://blog.csdn.net/qq_46018836/article/details/105199040   input 函数的用法

#  语法：  print("项目"%(参数行))
# %s 字符串    %d  输出整数    %f  输出浮点数
# name="张三";age=20
# print("%s的年龄为%d"%(name,age))
#
# # 用format()进行格式化输出
# print("{}的年龄为{}".format(name,age))


# a=input()
#
# # 无论我们输入的值是int，float还是sring，最后input（）函数返回的这个数据的类型均为string型。
# print(a,type(a))
# b=input()
# print(b,type(b))
# print(a+b)   # 这里会对两个字符串进行组合而不是算术运算
# a=int(input())
# b=float(input())
# print(type(a),type(b),type(a+b),a+b)

# name=input("请输入您的名字：")
# print("您的名字是："+name)





# if 语句实例:
# a,b=eval(input("请输入a,b两个数："))
# if a>=b: print("the max is:",a)
# else: print("the max is:",b)



#  for语句实例:  一个简单的求和方法的代码
# sum=0;number=int(input("please input a number:"))
# print("range from min to max is:")
# for i in range(1,number+1):
#     sum+=i
#     print("%d"%(i),end='')
#     if i<number: print("+",end='')
#     else: print("=",end='')
# print("%d"%(sum))
# sum=0
# print("range form max to min is:")
# for i in range(number,0,-1):
#     sum+=i
#     print("%d"%(i),end='')
#     if i>1: print('+',end='')
#     else : print('=',end='')
# print("%d"%(sum))


# while 循环
# from math import *
# n=0 ; x1=float(input('请输入角度：'))
# x=radians(x1)
# s=a=x
# while abs(a)>=1e-6:
#     a*=-x*x/(2*n+3)/(2*n+2)  #  用泰勒公式计算正弦值
#     n+=1;s+=a
# print("x={},s5in(x)={}".format(x1,s))

#  while循环中的语句至少执行一次
# sum=0;number=1
# while True:
#     if number==0:break
#     number=int(input("数字0结束程序，请输入数字："))
#     sum+=number
# print("目前累加的结果为：%d"%(sum))








