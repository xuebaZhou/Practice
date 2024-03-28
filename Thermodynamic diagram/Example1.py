import numpy as np
from numpy import fabs

# TODO：输入决策矩阵

decision_mat = np.array([[0.83, 326, 21, 3.2, 0.20, 0.15, 250, 0.23, 0.87],
                        [0.90, 295, 38, 2.4, 0.25, 0.20, 180, 0.15, 0.95],
                        [0.99, 340, 25, 2.2, 0.12, 0.14, 300, 0.27, 0.99],
                        [0.92, 287, 19, 2.0, 0.33, 0.09, 200, 0.30, 0.89],
                        [0.87, 310, 27, 0.9, 0.20, 0.15, 150, 0.18, 0.82] ,
                        [0.95, 303, 10, 1.7, 0.09, 0.17, 175, 0.26, 0.94]]).T

n, m = decision_mat.shape

# TODO：输入效益型属性下标
benefit_idx = [0, 4, 5, 6, 7, 8]

# TODO：输入成本型属性下标
cost_idx = [1, 2, 3]

# TODO：输入权重向量
weights = np.zeros(9)+(1/9)

# 标准0-1变换

max_values = np.max(decision_mat, axis=1)
min_values = np.min(decision_mat, axis=1)

for i in benefit_idx:
    decision_mat[i] = (decision_mat[i] - min_values[i]) / (max_values[i] - min_values[i])
for i in cost_idx:
    decision_mat[i] = (max_values[i] - decision_mat[i]) / (max_values[i] - min_values[i])

decision_mat = decision_mat.T

print(f"The preprocessed decision matrix is:\n{decision_mat}")

# 计算正理想解

ideal_pos = np.max(decision_mat, axis=0)

# 计算两级最大（小）差

min_diff = np.min(np.min(fabs(decision_mat-ideal_pos), axis=0))
max_diff = np.max(np.max(fabs(decision_mat-ideal_pos), axis=0))

# TODO：输入分辨系数
distinguish_coefficient = 0.5

# 计算灰色关联度

corr_mat = (min_diff + distinguish_coefficient*max_diff) / (fabs(decision_mat-ideal_pos) + distinguish_coefficient*max_diff)
corr_deg = np.sum(corr_mat*weights, axis=1)
print(f"The scores of DMUs are:\n{corr_deg}")
print(f"The DMUs are sorted by descending order as:\n{np.argsort(-corr_deg)}")