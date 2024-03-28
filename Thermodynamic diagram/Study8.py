import matplotlib.pyplot as plt
import numpy as np

# 假设的数据
# 这里我们假设有3个开发地点，每个地点有3个因素：经济因素、自然灾害风险、交通便利性
locations = ['Location A', 'Location B', 'Location C']
economic_factors = [0.8, 0.6, 0.9]  # 经济因素，值越高越有利
natural_disaster_risks = [0.1, 0.2, 0.05]  # 自然灾害风险，值越低越有利
transportation_accessibility = [0.7, 0.9, 0.8]  # 交通便利性，值越高越有利

# 目标函数的简化版本，这里我们只考虑经济因素和自然灾害风险
def objective_function(economic_factor, natural_disaster_risk):
    return economic_factor - natural_disaster_risk

# 约束条件的简化版本
def constraint_function(economic_factor, natural_disaster_risk, transportation_accessibility):
    return economic_factor >= 0.5 and natural_disaster_risk <= 0.15 and (transportation_accessibility >= 0.7)

# 绘制决策边界
def plot_decision_boundary(economic_factors, natural_disaster_risks, transportation_accessibilities):
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)

    Z = objective_function(X, Y)

    # 绘制等高线
    plt.contour(X, Y, Z, levels=[0], colors='r', linestyles='dashed')

    # 绘制约束条件
    plt.scatter(economic_factors, natural_disaster_risks, c='b', label='Locations')
    plt.scatter(economic_factors, [0.15] * len(economic_factors), c='g', label='Constraint')
    plt.scatter([0.5] * len(economic_factors), natural_disaster_risks, c='g', label='Economic Threshold')
    plt.scatter(economic_factors, [0.15] * len(economic_factors), c='g', label='Natural Disaster Threshold')
    plt.scatter([0.7] * len(economic_factors), natural_disaster_risks, c='g', label='Transportation Threshold')

    # 添加图例
    plt.legend()

    # 设置图表标题和坐标轴标签
    plt.title('Real Estate Development Decision Boundary')
    plt.xlabel('Economic Factors')
    plt.ylabel('Natural Disaster Risks')
    plt.show()

# 调用函数绘制决策边界
plot_decision_boundary(economic_factors, natural_disaster_risks, transportation_accessibility)