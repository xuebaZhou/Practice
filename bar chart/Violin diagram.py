import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 随机生成一些数据
data = np.random.normal(size=(100, 6), loc=0, scale=1)

# 绘制小提琴图
fig, ax = plt.subplots()
sns.violinplot(data=data, split=True, inner="quart", linewidth=1.5, ax=ax, density_norm='count', width=0.8)

# 设置图表标题、坐标轴标签等属性
ax.set_title('Violin Plot with Closer Distance')
ax.set_xlabel('Data')
ax.set_ylabel('Value')

plt.show()
