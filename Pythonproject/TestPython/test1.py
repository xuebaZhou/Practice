import math

#  + 加/正号   -  减/负号    // 整除      %  求余数     **  乘幂

a=2**3**2
print(a)  # 结果为512     多个乘幂运算符顺序出现，则先做右边的乘幂

c=1.8e308
print(c)    # inf  表示正无穷    浮点数溢出
d=12345678901234567890.0
print(d)        #    1.2345678901234567e+19    解释器会自动选择合适的方式

aa=1.2**20
print(aa)       #  38.33759992447472
bb=12**20/10**20
print(bb)       #  38.33759992447475   浮点数的精度有限，在反复计算中需要不断舍入，导致误差会变大


f=(1+2j)**10   #表示复数
ff=(1+2J)**100
print(f)
print(ff)

aaa=12**30
aab=12.0**30.0
print(aaa)      #  整数计算将得到任意大的准确结果
print(aab)      #  浮点数计算得到有限精度的近似结果


a=type(100.0)  #   这种方法可以得到字面量的数据类型
print(a)
print(type(100+0j))     #  <class 'complex'>  复数的类型名
print(2.7*3)        #  8.100000000000001



a=int(2.37**5.6)*4   # 强制类型转换
print(a)


#   用类型名complex构造复数
a=complex(12**20,1.25**20)
print(a)


a=max(12,1.36,136.5,26,-6)   # max函数可以传入任意多个实参
print(a)
a=min(12,1.36,136.5,26,-6)
print(a)

#  round函数  两种用法：
#  round(number)  给出由浮点数number舍入得到的整数
a=round(1.27**10)
print(a)

#  增加第二个指定舍入精度的整数参数,说明小数点后面保留的位数,最多15位
a=round(1.27**10,15)
print(a)


#  pow函数    pow(a,b)相当于 a**b
#  pow(a,b,c)  相当于计算  a**b%c   这个函数更加高效
a=pow(5,3)
print(a)
a=pow(5,3,3)
print(a)


##  数学函数包
from math import *  #  这个命令要求把math包的全部功能导入
from math import sin,cos  # 选择性的导入数学包math里定义的函数sin和cos
#  可以根据需要导入一个或多个函数，多个函数的名字之间用逗号分隔。
print(cos(3.14))
print(sin(3.14))
print(exp(0))  # 计算自然常数e的n次幂
print(log(2.718281828459045))   # log(x)  计算x的自然对数值   e近似为2.718281828459045
print(log2(8))  #  对数以2为底
print(log10(1000))  #   对数以10为底
print(3.0,2)  #   计算3.0的以2为底的对数值
print(sqrt(10000))


#   在Python中，使用标准的数学库（math）计算三角函数时，输入的角度是用弧度来表示的，而不是角度。
#   所以当你输入tan(45)时，它实际上是计算 tan(45 radians) 而不是 tan(45 degrees)。
#   这就解释了为什么输出结果接近于0.999999999999999999而不是1。
print(tan(radians(45)))  #   结果为    0.9999999999999999


print(pi**e)  #  pi 代表圆周率     e  代表自然常数
print(e**pi)

from cmath import exp   #  cmath   处理对象是  复数
print(exp(1.0j*pi)+1)    #   欧拉公式，，这里做的近似计算，结果接近  0

print(type("dfsf"))
print('wdwdasdszsczc'[3])  #  通过编号取得字符串里对应的字符
print("University"[-3])     # 允许用负整数作为下标提取字符串里的字符，下标-1表示取最后一个字符

a='Peking'+'  '+"University"
print(a)

print('OK'*3)
print(3*'OK')  #  输出完全一样


#     字符串切片:
#   s[m:n]   得到由字符s[m]到s[n-1]构成的字符串。如果m>=n就得到一个空字符串
#   s[m:n:d]  得到由s[m]到s[n-1],下标的步进值为d选出字符做成的字符串，
#    如果d是正数且m>=n,或者d是负数且n>=m，得到空字符串。

a='University is collage!'
print(a[2:6])
print(a[2:13:2])   #  iest s  理解语法规则后就可以了
print(a[::2])     #     Uiest sclae   省略n时表示len(a),d省略时表示1


print(str(101)+str(2.3**4))   #  数值转换为字符串有些是自动完成的

print(int('-1234'))
print(int('0001234'))  #  开头的0自动忽略
print(float('0001234'))



___=536+554
print(___)



print("abc",'uuu','oop')
#  同时打印多个字符串的时候，每个字符串都会自动默认以空格作为每个字符串之间的间隔

print('abc','uuu','oop',sep="")
#   如果在多个字符串的最后加上sep =，那么就可以改变间隔，比如这里我们改变为无任何间隔

print('abc','bcd','cde',sep='\n')
#  如果用\n也是和一般情况一样自动换行。





#   在print（）如果没有end=‘ ’，每次print语句都会自动换行，
#   而有了这个语句，数据就不会自动换行，而是在输出的数据后面加上空格（空格数取决于引号里面的空格数）。
#   通过一个例子来说明：
a , b=0 , 1
while a < 1000 :
    print( a , end = " ")
    a , b = b , a + b








