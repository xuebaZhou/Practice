import seaborn as sns
import plotly.graph_objects as go
from scipy import stats
import pandas as pd
import numpy as np
# 获取用户输入的数据
data = []
for i in range(2):
    row = []
    for j in range(2):
        value = int(input(f"Enter the count for row {i+1} and column {j+1}: "))
        row.append(value)
    data.append(row)
# 执行 Fisher 精确检验
odds_ratio, p_value = stats.fisher_exact(data)
# 设置标签和大小
labels = ["A=1,B=1", "A=1,B=2", "A=2,B=1", "A=2,B=2"]
sizes = [data[0][0], data[0][1], data[1][0], data[1][1]]
# 绘制饼状图
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.3)])
fig.update_layout(
    title_text="Fisher's exact test",
    annotations=[dict(text=f"Odds Ratio: {odds_ratio:.2f}", x=0.5, y=0.5, font_size=16, showarrow=False),
                 dict(text=f"p-value: {p_value:.4f}", x=0.5, y=0.4, font_size=16, showarrow=False)]
)
fig.show()
# 绘制堆叠柱状图
data_dict = {'A': [data[0][0], data[1][0]], 'B': [data[0][1], data[1][1]]}
df = pd.DataFrame(data_dict)
fig = go.Figure(data=[
    go.Bar(name='A', x=['1', '2'], y=df['A']),
    go.Bar(name='B', x=['1', '2'], y=df['B'])
])
fig.update_layout(barmode='stack', title_text='Stacked Bar Chart')
fig.show()

# 绘制热力图
df = pd.DataFrame(data)

fig = go.Figure(data=go.Heatmap(
    z=df,
    x=['1', '2'],
    y=['A', 'B'],
    colorscale='Viridis'
))
fig.update_layout(title_text='Heatmap')
fig.show()
