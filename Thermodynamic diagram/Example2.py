import matplotlib.pyplot as plt
import numpy as np

cdata = np.array([[1, 2, 3, 4, 5],
                  [5, 4, 3, 2, 1],
                  [1, 2, 3, 4, 5],
                  [5, 4, 3, 2, 1],
                  [1, 2, 3, 4, 5]])

xvalues = ['1x', '2x', '3x', '4x', '5x']
yvalues = ['1y', '2y', '3y', '4y', '5y']

fig, ax = plt.subplots()
heatmap = ax.imshow(cdata, cmap='hot')

# 设置x轴和y轴的刻度标签
ax.set_xticks(np.arange(len(xvalues)))
ax.set_yticks(np.arange(len(yvalues)))
ax.set_xticklabels(xvalues)
ax.set_yticklabels(yvalues)

# 在每个单元格中显示数值
for i in range(len(yvalues)):
    for j in range(len(xvalues)):
        text = ax.text(j, i, cdata[i, j], ha='center', va='center', color='black')

plt.colorbar(heatmap)  # 添加颜色条
plt.show()
