import numpy as np
import matplotlib.pyplot as plt

# 这是用来设置中文字体的
plt.rcParams['font.family'] = ['SimHei']

# 创建数据
theta = np.linspace(0, 2*np.pi, 100)
r = 2 + np.cos(theta)

# 创建极坐标图
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# 绘制极坐标曲线
ax.plot(theta, r)

# 设置极坐标角度刻度
ax.set_xticks(np.arange(0, 2*np.pi, np.pi/4))
ax.set_xticklabels(['0', '$\pi/4$', '$\pi/2$', '$3\pi/4$', '$\pi$', '$5\pi/4$', '$3\pi/2$', '$7\pi/4$'])

# 添加标题
ax.set_title('极坐标图')

# 显示图形
plt.show()
