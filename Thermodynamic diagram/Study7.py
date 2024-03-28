import matplotlib.pyplot as plt

# 这是用来设置中文字体的
plt.rcParams['font.family'] = ['SimHei']
# 神经元的坐标
x1 = [1, 1, 1, 1, 1]
y1 = [0, 2, 4, 6, 8]

x2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
y2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x3 = [3, 3, 3, 3, 3, 3, 3, 3]
y3 = [0, 1.5, 3, 4.5, 6, 7.5, 9, 10.5]

# 绘制连线
for i in range(5):
    for j in range(11):
        plt.plot([x1[i], x2[j]], [y1[i], y2[j]], 'k')

for i in range(11):
    for j in range(8):
        plt.plot([x2[i], x3[j]], [y2[i], y3[j]], 'k')

# 绘制神经元
plt.scatter(x1, y1, s=200, color='k', facecolor='r')
plt.scatter(x2, y2, s=200, color='k', facecolor='y')
plt.scatter(x3, y3, s=200, color='k', facecolor='k')

# 绘制分隔线
plt.plot([1.5, 1.5], [0, 11], 'k--')
plt.plot([2.5, 2.5], [0, 11], 'k--')

# 关闭坐标轴
plt.axis('off')

# 添加文本
plt.text(1.5, 11.75, '输入层')
plt.text(2, 11.75, '隐藏层')
plt.text(2.5, 11.75, '输出层')

plt.show()
