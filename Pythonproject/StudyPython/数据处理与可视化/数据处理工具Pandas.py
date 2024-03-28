#  序列构建  在终端输入 pip install pandas 进行下载 pandas安装包
import pandas as pd
import numpy as np

s1 = pd.Series(np.array([10.5, 20.5, 30.5]))  # 由数组构造序列
s2 = pd.Series({"北京": 10.5, "上海": 20.5, "广东": 30.5})  # 由字典构造序列
s3 = pd.Series([10.5, 20.5, 30.5], index=['b', 'c', 'd'])  # 给出行标签命名
print(s1);
print("-----------");
print(s2)
print("----------");
print(s3)

import pandas as pd
import numpy as np

s = pd.Series([10.5, 20.5, 98], index=['a', 'b', 'c'])
a = s['b'];
print(a)  # 取出序列的第二个元素
b1 = np.mean(s);
print(b1)
b2 = s.mean();
print(b2)  # 通过数列方法求均值

#  数据框的创建方法如下：
#  DataFrame(data=二维数据[,index=行索引[,columns=列索引[,dtype=数据类型]]])

import pandas as pd
import numpy as np

a = np.arange(1, 7).reshape(3, 2)
df1 = pd.DataFrame(a)
df2 = pd.DataFrame(a, index=['a', 'b', 'c'], columns=['x1', 'x2'])
df3 = pd.DataFrame({'x1': a[:, 0], 'x2': a[:, 1]})
print(df1);
print("-------");
print(df2)
print("-------");
print(df3)

# # 读取Excel文件
# import pandas as pd
# a=pd.read_excel("Pdata2_33.xlsx",engine="openpyxl")
# b=a.values
# c=a.describe()
# print(c)
