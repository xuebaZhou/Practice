
# python中九九乘法表的实现

# for i in range(1,10):     # i取值1到9
#     for j in range(1,i+1):      #j取值1到i
#         s="%d*%d=%d"%(j,i,i*j)      #赋值乘法公式
#         print(s.ljust(8),end='')    # 每个字符串占8个字符，左对齐，i不变时结尾不变行
#     print()     # i变时结尾处变行
#

# 函数的实现     可以通过用户的输入来进行乘法表的输出
def mult(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            s="%d*%d=%d"%(j,i,i*j)
            print(s.ljust(len(s)+2),end='')
        print()
n=int(input('Please input a number:'))
mult(n)