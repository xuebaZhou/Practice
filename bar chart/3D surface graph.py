import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# 这是绘制3D曲面图用的
# 生成数据
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
# 将x和y组合成网格坐标矩阵
X, Y = np.meshgrid(x, y)
Z = np.sin(4 * np.sqrt(X ** 2 + Y ** 2)) + np.sin(8 * np.sqrt(X ** 2 + Y ** 2))

# 创建3D投影
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面
surf = ax.plot_surface(X, Y, Z, cmap='rainbow', edgecolor='white')

# 添加颜色条(表示颜色条大小为原来的一半，宽高比为5)
fig.colorbar(surf, location='left',shrink=0.5, aspect=5)

# 设置轴标签
ax.set_xlabel('Current trend')
ax.set_ylabel('Voltage trend')
ax.set_zlabel('Changes in resistance')

# 显示图形
plt.show()
