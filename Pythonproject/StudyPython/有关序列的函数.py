
#   几个序列操作函数


#  Python  支持定义单行函数，称为lambda函数（也叫匿名函数）

f=lambda x,y:abs(x)+y**3
print("f(-3,2)=",f(-3,2))

#  map()  函数
#  调用格式  map(func,*iterables)
#  接收一个函数func和一个列表，把函数func依次作用在列表的每个元素上，得到一个新的列表

a=map(pow,range(6),[2 for b in range(6)])
print(list(a))



#  reduce()  函数
# 调用格式： reduce(function,sequence[,initial])
#  function 有两个参数的函数，sequence是元组、列表、字典和字符串等可迭代的对象，initial是可选的初始值
from functools import reduce  #  加载模块functools中的函数reduce


print(reduce(lambda x,y:x*y,range(1,6)))  #  计算5！

print(reduce(lambda x,y:x+y,range(1,7)))  #  计算1+2+3+4+5+6



#  filter() 函数
#  调用格式：  filter(function or None,iterable)
#  通过function对iterable中的元素进行过滤，并返回一个迭代器(iterator),function返回Ture的元素
#  如果function传入None，则返回所有本身可以判断为True的元素
#   iterator对象无法显示，输出时用list进行转换
print(list(filter(lambda n:n%3==0,range(1,21))))





#    zip()函数
#    zip(列表1,列表2,...);将多个列表或元组对应位置的元素组合为元组，并返回包含这些元组的zip对象
a=range(1,5)
b=range(5,9)
c=zip(a,b)
print(list(c))
#  *操作符将元组分为了两个独立的参数进行传递。
print(list(zip(*zip(a,b))))




#   enumerate()  函数\
#  https://blog.csdn.net/windmyself/article/details/119413613    enumerate函数详解
a=[(1,5),(2,6),(3,7)]
for b in enumerate(a):print(b)

print([value[0] for (ind ,value ) in enumerate(a)])
#这条语句的意思是，给定列表a，将其中每个元素的第一个字符提取出来并组成一个新的列表。具体解析如下：

# 使用enumerate()函数对列表a进行枚举，得到每个元素的索引（ind）和对应的值（value）。
# 遍历枚举结果，使用列表生成式将每个value的第一个字符提取出来。
# 最终得到的结果是由每个value的第一个字符组成的新列表。
print([value[1] for (ind ,value ) in enumerate(a)])

# 列表推导式    例如： B=[[0]*6 for i in range(4)]
#  https://zhuanlan.zhihu.com/p/343440107
#  使用列表推导式实现嵌套列表的平铺
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[d for c in a for d in c]
print(b)
# 这段代码的作用是将二维列表a中的元素提取出来，并以一维列表b的形式存储。
# 具体实现是通过使用列表推导式，将每个子列表c中的元素d逐个添加到列表b中。最后打印输出列表b。
# 执行结果将会是[1, 2, 3, 4, 5, 6, 7, 8, 9]。

# num=[i*i if i%3==0 else i for i in range(1,101)]
# print(num)

#  过滤不符合条件的元素
a=[-1,-2,6,8,-10,3]
b=[i for i in a if i>0]
print(b)
b.sort()         #  升序排列
print(b)

#  使用多个循环，结合条件语句
c=[(x,y) for x in range(5) if x%2==0 for y in range(5) if y%2==1]
print(c)

#   元组生成器推导式
#  结果是一个生成器对象，使用生成器对象的元素的时候，需要将其转化为列表或元组

g1=((i+1)**2 for i in range(6))
g2=tuple(g1)
print(g2)










