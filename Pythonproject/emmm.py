# import pandas as pd
# import matplotlib.pyplot as plt
#
# df=pd.read_excel('附件.xlsx');
# data=df.head()
# print("获取到的数据:\n{0}".format(data))

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import *

# 从Excel读取数据
data = pd.read_excel('附件.xlsx')
# 这行代码是用来设置中文字体的
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 创建数据透视表
pivot_table = data.pivot_table(index='纹饰', columns='类型', values='文物编号')

# 绘制热力图
sns.heatmap(pivot_table, cmap='YlOrRd', annot=True, fmt=".0f")

# 设置图形标题和坐标轴标签
plt.title('Heatmap of 文物编号')
plt.xlabel('类型')
plt.ylabel('纹饰')

# 显示热力图
plt.show()







