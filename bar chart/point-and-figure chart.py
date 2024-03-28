import plotly.graph_objects as go

# 数据
data = [20, 40, 60, 80, 100, 120]

# 创建图形对象
fig = go.Figure()

# 添加点线图
fig.add_trace(go.Scatter(x=list(range(1, len(data)+1)), y=data, mode='lines+markers'))

# 设置坐标轴标签和标题
fig.update_layout(xaxis_title='X', yaxis_title='Y', title='Point Line Chart')

# 显示图形
fig.show()
