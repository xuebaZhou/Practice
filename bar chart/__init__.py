import matplotlib.pyplot as plt
import numpy as np

# 生成模拟数据
days = np.arange(1, 31)
rates1 = np.random.normal(loc=0, scale=0.5, size=30).cumsum()
rates2 = np.random.normal(loc=0, scale=0.3, size=30).cumsum()
rates3 = np.random.normal(loc=0, scale=0.7, size=30).cumsum()

# 创建新的图形
plt.figure(figsize=(10, 6))

# 绘制第一个汇率波动曲线
plt.plot(days, rates1, label='Exchange Rate 1', color='blue')

# 绘制第二个汇率波动曲线
plt.plot(days, rates2, label='Exchange Rate 2', color='green')

# 绘制第三个汇率波动曲线
plt.plot(days, rates3, label='Exchange Rate 3', color='red')

# 添加标题和标签
plt.title('Exchange Rate Fluctuations')
plt.xlabel('Days')
plt.ylabel('Rate')

# 添加图例
plt.legend()

# 显示图形
plt.show()
