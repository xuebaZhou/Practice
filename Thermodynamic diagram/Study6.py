import numpy as np
import matplotlib.pyplot as plt

# 这是用来设置中文字体的
plt.rcParams['font.family'] = ['SimHei']

# 灰色预测函数
def grey_model(x0):
    x1 = np.cumsum(x0)  # 累加生成序列
    z1 = (x1[:-1] + x1[1:]) / 2.0  # 紧邻均值生成序列
    B = np.vstack((-z1, np.ones_like(z1))).T  # 建立数据矩阵B
    Y = x0[1:].reshape((len(x0)-1, 1))  # 数据向量Y
    [[a], [b]] = np.dot(np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Y)  # 计算参数
    Xn = (x0[0]-b/a) * np.exp(-a * np.arange(1, len(x0)+1))  # 模型计算
    return Xn

# 手动输入数据
input_str = input("请输入数据，以空格分隔: ")
x0 = np.array(list(map(float, input_str.split())))

# 预测未来5个时间点的数据
prediction_length = 5
xn = grey_model(x0)
prediction = grey_model(np.hstack((x0, xn[-1])))[-prediction_length:]

# 绘制折线图
plt.plot(np.arange(len(x0)), x0, 'bo-', label='原始数据')  # 绘制历史观测值
plt.plot(np.arange(len(x0), len(x0)+prediction_length), prediction, 'ro--', label='预测数据')  # 绘制预测结果
plt.legend(loc='best')
plt.xlabel('时间')
plt.ylabel('数据值')
plt.show()
