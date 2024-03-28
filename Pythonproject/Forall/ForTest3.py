# Python打印三角形，菱形
# 正三角形
for i in range(1,6):
    print("*"*i)


for i in range(1,6):
    print(("*"*i).rjust(5))

for i in range(1,6):
    print(('*'*(2*i-1)).center(9))

# 倒三角形

for i in range(5):
    print((" "*i).rjust(5,'*'))


for i in range(5):
    print((" "*i).ljust(5,'*'))


for i in range(1,6):
    print(('*'*(11-2*i)).center(9))



for i in range(-4,5):
    s="*"*(9-2*abs(i))  # abs(i)取绝对值
    print(s.center(9))




for i in range(-4,5):
    s=8-2*abs(i)
    m=(' '*s).ljust(s+1,'*').replace(' ','*',1)  # 空格左右加上  *
    print(m.center(9))  #  居中



# 语法  变量.ljust(长度,填充字符)
# ljust 左对齐。
# 长度（即15）
str = "hello world"

print(str.ljust(15, "-"))  # 结果：hello world----

print(str.ljust(8, "-"))  # 结果：hello world

# 结果：报错 The fill character must be exactly one character long
# 即  填充字符长度必须正好为一个字符
#     print(str.ljust(15, "**"))  这句话会报错的

#  ljust 左对齐。
# 长度（即 15）如果大于字符串（即str）总长度时，缺少的字符由填充字符（即 -）进行向右填充
# 长度如果小于字符串总长度时，输出原来的字符串，更不会进行填充。








