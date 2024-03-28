
#  使用 help("sympy")可以看到模块的名称



# from sympy import *
# x=symbols('x')    x是符号变量的名称，'x'是符号变量的值，用于显示
# y,z=symbols('y z')    构建多个符号变量时，中间以空格分隔




#  在符号计算中，使用evalf()或n()方法来获得任何对象的浮点近似值，
#  默认的精度是小数点后15位，可通过参数调整改成任何想要的精度
from sympy import *
x,y,z=symbols('x y z')
m0,m1,m2,m3=symbols('m0:4')  #创建多个符号变量
x=sin(1)
print("x=",x);print("x=",x.evalf())
print("x=",x.n(16))  # 显示小数点后16位数字
print("pi的两种显示格式:{},{}".format(pi,pi.evalf(3)))  # 这里不能使用n()函数
expr1=y*sin(y**2)  # 创建第一个符号表达式
expr2=y**2+sin(y)*cos(y)+sin(z)   # 创建第二个符号表达式
print("expr1=",expr1)
print("y=5时,expr1=",expr1.subs(y,5))  # 代入一个符号变量的值
print("y=2,z=3时，expr2=",expr2.subs({y:2,z:3}))
print("y=2,z=3时，expr2=",expr2.subs({y:2,z:3}).n())  # 以浮点数显示计算结果



#   处理有理数
#   计算有理数的加法，用到together函数，计算有理数的除法，用到apart函数
from sympy import *
x1,x2,x3,x4=symbols('m1:5');x=symbols('x')
print(x1/x2+x3/x4)
print(together(x1/x2+x3/x4))
print((2*x**2+3*x+4)/(x+1))
print(simplify((2*x**2+3*x+4)/(x+1))) # 化简没有效果
#  请注意，在进行 SymPy 表达式化简时，并不能保证每个表达式都能被完全化简。某些复杂或特殊的表达式可能无法进一步简化。
print(apart((2*x**2+3*x+4)/(x+1)))   #  相当于分式的化简

# 第一个 print 语句输出的是未化简的表达式，x1/x2 + x3/x4。
# 第二个 print 语句使用 together 函数进行有理化简，得到 (m1*m4*x + m2*m3*x + m2*m3)/(m2*m4*x)。它把分数项合并到一起。
# 第三个 print 语句输出的是未化简的表达式，(2*x**2 + 3*x + 4)/(x + 1)。
# 第四个 print 语句使用 simplify 函数对表达式进行化简，结果仍然是 (2*x**2 + 3*x + 4)/(x + 1)。这是因为 simplify 函数尝试对表达式进行简化，但不一定能够找到最简形式。
# 第五个 print 语句使用 apart 函数对表达式进行部分分式分解，得到 2 - 1/(x + 1)。
# 需要注意的是，对于非线性、复杂或特殊的表达式，化简的效果可能不如预期。在这种情况下，将表达式进行部分分式分解可能更加合适。



