# 打开文件
#   文件对象名 = open(文件名[,打开方式[，缓冲区])


#  文件对象属性操作
f = open("Pdata2_21.txt", "w")
print("Name of the file:", f.name)
print("Closed or not:", f.closed)
print("Opening mode:", f.mode)
f.close()
print("Closed or not:", f.closed)

# 文本文件读写操作
f = open("Pdata2_25.txt", "r")
s = f.read()
print(s)  # 显示文件内容
n = 0;
m = 0
for c in s:
    m += 1
    if c in "aeiouAEIOU": n += 1
print("元音的个数为:%d,字母总个数为:%d" % (n, m))

f1 = open("Pdata2_26.txt", "w")
str1 = ["Hello", ' ', 'World!'];
str2 = ['Hello', 'World!']
f1.writelines(str1);
f1.write('\n')
f1.writelines(str2);
f1.close()
f2 = open('Pdata2_26.txt')
a = f2.read();
print(a)

# import numpy as np
# a=[] ; b=[] ; c=[]
# with open("Pdata2_21.txt") as file:
#     for(i,line) in enumerate(file):
#         elements=line.strip().split()
#         if i<6:
#             a.append(list(map(float,elements[:8])))
#             b.append((float(elements[-1].rstrip('kg'))))
#         else:
#             c=[float(x) for x in elements]
# a=np.array(a);b=np.array(b);c=np.array(c)
# print(a,'\n',b,'\n',c)
