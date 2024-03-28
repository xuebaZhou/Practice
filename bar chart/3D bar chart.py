import matplotlib.pyplot as plt
import numpy as np
# 绘制3D条形图
# 创建一个10x10的随机矩阵
matrix = np.random.rand(10, 10)

# 设置颜色映射
# cmap = plt.get_cmap('rainbow')

# 创建绘图空间
# 创建了一个新的图形窗口，返回一个Figure对象 fig
fig = plt.figure()
# 参数(111)表示将整个图形窗口分割为1行1列的单个子图网格，
# 当前子图位于第1个位置。projection='3d'表示创建一个3D绘图对象。
ax = fig.add_subplot(111, projection='3d')

# 获取矩阵大小
x_size, y_size = matrix.shape

# 确定颜色映射范围
min_z, max_z = matrix.min(), matrix.max()
norm = plt.Normalize(min_z, max_z)
cmap = plt.get_cmap('rainbow')
# 遍历矩阵每个元素，绘制条形图
for x in range(x_size):
    for y in range(y_size):
        # 确定每个条形的位置和高度
        xpos = x
        ypos = y
        zpos = 0
        dx = dy = 1
        dz = matrix[x][y]

        # 随机选择颜色
        color = cmap(np.random.random())

        # 绘制条形图
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=color)

# 设置坐标轴标签
ax.set_xlabel('Hello')
ax.set_ylabel('NiHao')
ax.set_zlabel('Hi')

# 显示图形
plt.show()
