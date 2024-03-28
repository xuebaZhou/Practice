import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# 生成随机高度数据
data = np.random.rand(10, 10)

# 创建坐标网格
x = np.arange(0, 10, 1)
y = np.arange(0, 10, 1)
X, Y = np.meshgrid(x, y)

# 创建3D图形对象
fig = plt.figure()
ax = plt.axes(projection='3d')

# 绘制三维地形图，增加rstride和cstride参数
ax.plot_surface(X, Y, data, cmap='viridis', rstride=1, cstride=1)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
