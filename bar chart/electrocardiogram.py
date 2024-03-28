import numpy as np
import matplotlib.pyplot as plt

# 心电图数据，这里使用随机生成的示例数据
time = np.linspace(0, 10, 1000)  # 时间轴
heart_rate = np.sin(time) + np.random.normal(0, 0.1, size=len(time))  # 心率数据

# 移动平均滤波器
window_size = 10
smoothed_heart_rate = np.convolve(heart_rate, np.ones(window_size)/window_size, mode='same')

# 创建画布和坐标轴
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制心电图波形
ax.plot(time, smoothed_heart_rate, 'b')

# 设置图形标题和坐标轴标签
ax.set_title('Heart Rate')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Heart Rate')

# 显示网格线
ax.grid(True)

# 显示图形
plt.show()
