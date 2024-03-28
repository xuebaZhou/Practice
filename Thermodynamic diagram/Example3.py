import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from pylab import *
mpl.rcParams["font.sans-serif"] = ["SimHei"]

# 定义点(x,y,z)
x = np.random.randn(50, 1)
xmax = np.max(x)
xmin = np.min(x)
y = np.random.randn(50, 1)
ymax = np.max(y)
ymin = np.min(y)
z = np.exp(np.sin(x**2)) + np.exp(np.cos(y**2))

N = 500  # 每个维度的数据点数

# 网格化x,y二维空间
X, Y = np.meshgrid(np.linspace(xmin, xmax, N), np.linspace(ymin, ymax, N))

# 采用插值法扩展数据，可用方法有'linear'(default)|'nearest'|'natural'|'cubic'
Z = griddata((x.flatten(), y.flatten()), z.flatten(), (X, Y), method='cubic')

# 等高线法
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, N, cmap='jet', linewidths='solid',fill=True)
plt.colorbar()
plt.axis('off')

# 添加边界线
ax = plt.gca()
ax.spines['top'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.spines['right'].set_visible(True)

plt.title('等高线法')
plt.show()


# 投影图法
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='jet', linewidth=0, antialiased=False)
ax.view_init(30, 120)  # 设置视角

# 添加边界线
ax.spines['top'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.spines['right'].set_visible(True)

plt.xlim([np.min(X), np.max(X)])
plt.ylim([np.min(Y), np.max(Y)])
plt.axis('off')
plt.title('投影图法')
plt.show()


# imagesc法
plt.figure(figsize=(8, 6))
plt.imshow(np.flipud(Z), cmap='jet')

# 添加边界线
ax = plt.gca()
ax.spines['top'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.spines['right'].set_visible(True)

plt.colorbar()
plt.axis('off')
plt.title('imagesc法')
plt.show()


# pcolor法
plt.figure(figsize=(8, 6))
plt.pcolor(X, Y, Z, cmap='jet', shading='auto', linewidth=0)

# 添加边界线
ax = plt.gca()
ax.spines['top'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.spines['right'].set_visible(True)

plt.colorbar()
plt.axis('off')
plt.title('pcolor法')
plt.show()
