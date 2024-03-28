# 数组的创建
import numpy as np

a = np.array([2, 4, 8, 20, 16, 30])  # 单个列表创建一维数组
#  嵌套元组创建二维数组
b = np.array(((1, 2, 3, 4, 5), (6, 7, 8, 9, 10),
              (10, 9, 1, 2, 3), (4, 5, 6, 8, 9.0)))
print("一维数组为：", a)
print("二维数组为：\n", b)  # 输出的数组元素都转化为相同的浮点型

#  利用arange,empty,linspace等函数生成数组
import numpy as np

a = np.arange(4, dtype=float);
print(a)  # 创建浮点型数组
b = np.arange(0, 10, 2, dtype=int);
print(b)  # 创建整型数组
c = np.empty((2, 3), int);
print(c)  # 创建2×3的整形空矩阵
d = np.linspace(-1, 2, 5);
print(d)  # 创建数组
e = np.random.randint(0, 3, (2, 3));
print(e)  # 生成[0,3)上的2行3列的随机整数数组

# 使用虚数单位'j'生成数组
import numpy as np

a = np.linspace(0, 2, 5)
b = np.mgrid[0:2:5j]  # 等价于 np.linspace(0,2,5)
x, y = np.mgrid[0:2:4j, 10:20:5j]
print("x={}\ny={}".format(x, y))

#  2.数组的属性
import numpy as np

a = np.random.randint(1, 11, (3, 5))  # 生成[1,10]区间上3行5列的随机整数数组
print("维数：", a.ndim)
print("维度：", a.shape)
print("元素总数：", a.size)
print("类型：", a.dtype)
print("每个元素字节数：", a.itemsize)

#  生成数学上一维向量的三种模式。
import numpy as np

a = np.array([1, 2, 3])
print("维度为：", a.shape)  # (3,)   这个既可以看成行向量，也可以看成列向量，其转置不变
b = np.array([[1, 2, 3]])
print("维度为：", b.shape)  # (1,3)
c = np.array([[1], [2], [3]])
print("维度为：", c.shape)  # (3,1)

#  数组元素的索引
#  1、一般索引
import numpy as np

a = np.array([2, 4, 8, 20, 16, 30])
b = np.array(((1, 2, 3, 4, 5), (6, 7, 8, 9, 10),
              (10, 9, 1, 2, 3), (4, 5, 6, 8, 9.0)))
print(a[[2, 3, 5]])  # [ 8 20 30]
print(a[[-1, -2, -3]])  # [30 16 20]
print(b[1, 2])  # 输出第二行第三列的元素
print(b[2])  # 输出第三行元素
print(b[2, :])  # 输出第三行元素
print(b[:, 1])  # 输出第二列所有的元素
print(b[[2, 3], 1:4])  # 输出第3、4行，第2、3、4列的元素
print(b[1:3, 1:3])  # 输出第2、3行，第2,3列的元素

#  2、布尔索引
from numpy import array, nan, isnan

a = array([[1, nan, 2], [4, nan, 3]])
b = a[~isnan(a)]  # 提取a中非Nan的数
print('b=', b)
print("b中大于2的元素有：", b[b > 2])

#  3、花式索引    https://zhuanlan.zhihu.com/p/123858781
#  索引值是一个数组,
#  当索引值为两个维度相同的一维数组组成的二维数组时，以两个维度作为横纵坐标索引出单值后组合成新的一维数组
import numpy as np

x = array([[1, 2], [3, 4], [5, 6]])
print("前两行元素为：\n", x[[0, 1]])  # [[1 2][3 4]]
print(x[[0, 1]][:, [0, 1]])  # [[1 2][3 4]]
print("x[0][0]和x[1][1]为：", x[[0, 1], [1, 0]])  # x[0][0]和x[1][1]为： [2 3]
print(x[0:2, 0:2])  # [[1 2][3 4]]
print(x[[0, 0], [1, 1]])  # [2 2]

#   数组的修改
#   https://zhuanlan.zhihu.com/p/432981099   axis函数的相关性质
#  这里axis=0表示行，axis=1表示列
import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
x[2, 0] = -1;
print(x)  # 修改第三行、第一列的元素为-1
y = np.delete(x, 2, axis=0);
print(y)  # 删除数组的第三行
z = np.delete(y, 0, axis=1);
print(z)  # 删除数组的第一列
t1 = np.append(x, [[7, 8]], axis=0);
print(t1)  # 增加一行
t2 = np.append(x, [[9], [10], [11]], axis=1);
print(t2)  # 增加一列

#  数组的变形

import numpy as np

a = np.arange(4).reshape(2, 2)  # 生成数组[[0,1],[2,3]]
b = np.arange(4).reshape(2, 2)
print(a.reshape(4, ), '\n', a)  # [0 1 2 3] [[0 1][2 3]]
print(b.resize(4, ), '\n', b)  # None  [0 1 2 3]
# reshape  返回的是视图，数组本身不变
# resize   没有返回，改变数组本身


#  数组降维
import numpy as np

a = np.arange(4).reshape(2, 2)
b = np.arange(4).reshape(2, 2)
c = np.arange(4).reshape(2, 2)
print(a.reshape(-1), '\n', a)
print(b.ravel(), '\n', b)
print(c.flatten(), '\n', c)
#   这三种原数组都没有修改，flatten()分配了新的内存，ravel()返回的是一个数组的视图，e=b.ravel()是可以的

#  数组组合
import numpy as np

a = np.arange(4).reshape(2, 2)
b = np.arange(4, 8).reshape(2, 2)
c1 = np.vstack([a, b]);
print(c1)  # 垂直方向组合
c2 = np.r_[a, b];
print(c2)  # 垂直方向组合
d1 = np.hstack([a, b]);
print(d1)  # 水平方向组合
d2 = np.c_[a, b];
print(d2)  # 水平方向组合

# 数组分割
import numpy as np

a = np.arange(4).reshape(2, 2)
b = np.hsplit(a, 2)  # 把a平均分成2个列数组
c = np.vsplit(a, 2)  # 把a平均分成2个行数组
print(b[0], '\n', b[1], '\n', c[0], '\n', c[1])

#  数组简单运算
# 余数 %  fmod    整除 //  modf   幂次  **  power
import numpy as np

a = np.arange(10, 15);
b = np.arange(5, 10)
c = a + b;
d = a * b;  # 对应元素相加和相乘
e1 = np.modf(a / b)[0]  # 对应元素相除的小数部分
e2 = np.modf(a / b)[1]  # 对应元素相除的整数部分
print(c, '\n', d, '\n', e1, '\n', e2)

# 比较运算
import numpy as np

a = np.array([[3, 4, 9], [12, 15, 1]])
b = np.array([[2, 6, 3], [7, 8, 12]])
print(a[a > b])  # 取出a大于b的所有元素
print(a[a > 10])  # 取出a大于10的所有元素
print(np.where(a > 10, -1, a))  # a中大于10的元素改为-1
print(np.where(a > 10, -1, 0))  # a中大于10的元素改为-1，否则为0
#  多维数组通过bool索引返回的都是一维数组；np.where返回的数组保持原来的形状


#  ufunc函数   通用函数
import numpy as np, time, math

x = [i * 0.01 for i in range(1000000)]
start = time.time()  # 1970纪元后经过的浮点秒数
for (i, t) in enumerate(x): x[i] = math.sin(t)
print("math.sin:", time.time() - start)
y = np.array([i * 0.01 for i in range(1000000)])
start = time.time()
y = np.sin(y)
print("numpy.sin:", time.time() - start)

#  ufunc函数的广播机制
#  https://blog.csdn.net/weixin_43912972/article/details/105207848
import numpy as np

a = np.arange(0, 20, 10).reshape(-1, 1)  # 变形为1列的数组，行数自动计算
b = np.arange(0, 3)
print(a + b)

#  savetxt()可以把一维和二维数组保存在文本文件中，loadtxt()可以把文本文件中的数据加载到一维和二维数组中
import numpy as np

a = np.arange(0, 3, 0.5).reshape(2, 3)  # 生成2×3的数组
np.savetxt('Pdata2_18_1.txt', a)
#  缺省按照'%.18e'格式保存数值，以空格分隔
b = np.loadtxt("Pdata2_18_1.txt")  # 返回浮点型数组
print("b=", b)
np.savetxt("Pdata2_18_1.txt", a, fmt="%d", delimiter=",")
#  保存为整型数据，以逗号分隔
c = np.loadtxt("Pdata2_18_1.txt", delimiter=",")
#  读入的时候也需要指定逗号分隔
print("c=", c)

#  程序文件相关的操作
import numpy as np

a = np.loadtxt('Pdata2_19.txt')  # 返回值a为浮点数类型
b = a[0:2, 1:4]  # 获取a的第1,2行，第2,3,4列
print("b=", b)

#  https://zhuanlan.zhihu.com/p/483924233
# import numpy as np
# a=np.loadtxt("Pdata2_20.txt",dtype=str,delimiter=",")
# b=a[1:,1:].astype(float)
# print("b=",b)


#  https://www.cnblogs.com/zeroing0/p/14590117.html  genformtxt函数的相关知识
#  usecols: 指定需要读入的列
import numpy as np

a = np.genfromtxt("Pdata2_21.txt", max_rows=6, usecols=range(8))
b = np.genfromtxt("Pdata2_21.txt", dtype=str, max_rows=6, usecols=[8])
#  读第九列数值数据
b = [float(v.rstrip('kg')) for (i, v) in enumerate(b)]
#  删除kg，并转换为浮点型数据
c = np.genfromtxt("Pdata2_21.txt", skip_header=6)  # 读最后一行数据
print(a, '\n', b, '\n', c)
