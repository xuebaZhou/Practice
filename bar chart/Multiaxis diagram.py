import  numpy as np
import matplotlib.pyplot as plt

# 创建数据
x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)
y3=np.tan(x)

# 创建图形和轴对象
fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax3=ax1.twinx()

# 绘制第一个轴的图形
ax1.plot(x,y1,'r-',label='sin')
ax1.set_ylabel('sin',color='red')
ax1.tick_params('y',colors='red')

# 绘制第二个轴的图形
ax2.plot(x,y2,'g-',label='cos')
ax2.set_ylabel('cos',color='green')
ax2.tick_params('y',colors='green')

# 绘制第三个轴的图形
ax3.plot(x,y3,'b-',label='tan')
ax3.set_ylabel('tan',color='blue')
ax3.tick_params('y',colors='blue')

# 添加图例
lines=[ax1.get_lines()[0],ax2.get_lines()[0],ax3.get_lines()[0]]
ax1.legend(lines,[line.get_label() for line in lines])

# 调整轴的位置
ax3.spines['right'].set_position(('outward',60))

# 显示图形
plt.show()