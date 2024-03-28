import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

plt.style.use('ggplot')

values1 = [7.11, 4.89, 3.11, 12, 6.67, 10.22, 4.44, 4, 16.44, 2.22, 0, 2.22, 3.11, 5.33, 2.22, 6.67, 4.89, 2.22, 1.33,
           0.44,
           0.44, 0]
feature = ['制造业', '建筑业', '物流交通', '教育培训', '互联网', '计算机/软件', '批发零售', '住宿餐饮业', '金融业',
           '房地产', '出租业', '法律咨询服务', '科学研究', '生活服务', '医疗卫生/社会保障', '文化娱乐', '政府事业单位',
           '农林牧鱼业', '水利环境公共设施管理', '采矿业', '电力燃气', '国际组织']

angles = np.linspace(0, 2 * np.pi, len(feature), endpoint=False)
angles = np.concatenate((angles, [angles[0]]))

fig = plt.figure()

# Move the creation of subplot (ax) outside the loop
ax = fig.add_subplot(111, polar=True)

# Set the background color of the polar plot
ax.set_facecolor('lightgray')

for values in [values1]:
    values = np.concatenate((values, [values[0]]))
ax.plot(angles, values, 'o-', linewidth=2, color='skyBlue', label='所占百分比')
ax.fill(angles, values, alpha=0.5, color='lightblue')

ax.set_thetagrids(angles[:-1] * 180 / np.pi, feature)
ax.set_ylim(0, 17)

plt.title('调查人员行业占比图(%)')
ax.grid(True)

# Add legend with specified labels
ax.legend()

plt.show()
