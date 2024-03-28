# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
#
# # 绘制 4x4 的宫格子图
# fig = plt.figure(figsize=(16, 16))
# fig.suptitle('4x4 Subplots of 3D Scatter Plots')
#
# # 绘制 4x4 的宫格子图
# for i in range(16):
#     data = np.random.rand(100, 3)  # 为每个子图生成不同的随机数据
#     ax = fig.add_subplot(4, 4, i+1, projection='3d')
#     ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=data[:, 0] + data[:, 1] + data[:, 2])  # 使用数据的和作为颜色
#     # ax.set_title('Subplot {}'.format(i+1))
#     ax.set_zlabel('Subplot {}'.format(i + 1))  # 设置左边标题
#
# # 添加背景格子
# background_ax = fig.add_subplot(4, 4, 17, frame_on=False)
# background_ax.axis('off')
#
# plt.show()


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 创建 4x4 的子图
# fig, axs = plt.subplots(4, 4, figsize=(16, 16), subplot_kw={'projection': '3d'})
fig, axs = plt.subplots(4, 4, figsize=(16, 16), subplot_kw={'projection': '3d'}, gridspec_kw={'width_ratios': [1, 1, 1, 1], 'height_ratios': [1, 1, 1, 1]})
fig.suptitle('4x4 Subplots of 3D Scatter Plots')

# 绘制每个子图
for i in range(4):
    for j in range(4):
        data = np.random.rand(100, 3)  # 为每个子图生成不同的随机数据
        axs[i, j].scatter(data[:, 0], data[:, 1], data[:, 2], c=data[:, 0] + data[:, 1] + data[:, 2])  # 使用数据的和作为颜色
        axs[i, j].set_title('Subplot {}'.format(i*4 + j + 1))  # 设置标题
        axs[i, j].set_facecolor('gray')  # 设置子图背景颜色为灰色
# 调整子图间距
plt.tight_layout()

# 添加背景格子
background_ax = fig.add_subplot(111, frame_on=False)
background_ax.axis('off')
background_ax.text(0.5, 0.5, 'Background', ha='center', va='center', fontsize=20, color='gray')

plt.show()
