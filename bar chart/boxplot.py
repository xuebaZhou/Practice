import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 随机生成一些数据
data = np.random.normal(size=(100, 4), loc=0, scale=1)

# 绘制带有颜色的箱线图
fig, ax = plt.subplots()
sns.boxplot(data=data, width=0.5, palette="pastel", ax=ax)

# 标注几个特定数据点
points_to_annotate = [10, 30, 70]
for i in points_to_annotate:
    ax.text(1, data[i, 1], f'Point {i}', horizontalalignment='left', size='medium', color='black', weight='semibold')

# 设置图表标题、坐标轴标签等属性
ax.set_title('Box Plot with Colored Boxes and Annotated Points')
ax.set_xlabel('Data')
ax.set_ylabel('Value')

plt.show()
