# import matplotlib.pyplot as plt
# import numpy as np
#
# # 创建数据
# x = np.random.rand(100)
# y = np.random.rand(100)
# categories = ['A', 'B', 'C', 'D']
# category_values = [20, 35, 15, 30]
# z = np.random.rand(10, 10)
#
# # 创建图形网格
# fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(8, 12))
#
# # 第一行：散点图
# axes[0].scatter(x, y)
# axes[0].set_title('Scatter Plot')
#
# # 第二行：条形图
# axes[1].bar(categories, category_values)
# axes[1].set_title('Bar Chart')
#
# # 第三行：饼状图
# axes[2].pie(category_values, labels=categories, autopct='%1.1f%%')
# axes[2].set_title('Pie Chart')
#
# # 第四行：等高线图
# axes[3].contourf(z)
# axes[3].set_title('Contour Plot')
#
# # 调整图形之间的间距
# plt.tight_layout()
#
# # 显示图形网格
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.random.rand(16)
y = np.random.rand(16)
sizes = np.random.randint(50, 200, 16)  # 随机生成数据点的大小
colors = np.linspace(0, 1, 16)  # 生成渐变的颜色

# 创建画布和子图
fig, ax = plt.subplots(figsize=(6, 6))

# 绘制散点图
scatter = ax.scatter(x, y, c=colors, s=sizes, cmap='cool', edgecolor='black')

# 设置颜色条
cbar = plt.colorbar(scatter)
cbar.set_label('Color Scale')

# 设置标题和坐标轴标签
ax.set_title('Scatter Plot with Varying Colors and Sizes')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# 显示图形
plt.show()
