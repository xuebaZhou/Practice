import matplotlib.pyplot as plt
import numpy as np
# 堆叠面积图
x = np.arange(10)
y1 = np.random.uniform(0, 1, 10)
y2 = np.random.uniform(0, 1, 10)
y3 = np.random.uniform(0, 1, 10)

fig, ax = plt.subplots()

ax.fill_between(x, y1, color="skyblue", alpha=0.4, label='Data1')
ax.fill_between(x, y2, color="lightgreen", alpha=0.5, label='Data2')
ax.fill_between(x, y3, color="salmon", alpha=0.6, label='Data3')

ax.plot(x, y1, color="Slateblue", alpha=0.6, linewidth=2)
ax.plot(x, y2, color="olive", alpha=0.6, linewidth=2)
ax.plot(x, y3, color="indianred", alpha=0.6, linewidth=2)

ax.set_title('Stacked Area Plot with Undulations')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.legend()

plt.show()
