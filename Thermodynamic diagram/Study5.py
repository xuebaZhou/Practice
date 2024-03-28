
import numpy as np
import matplotlib.pyplot as plt

# Point properties
num_of_points = 6
row_of_points = 4

# Random data
P = np.random.rand(row_of_points, num_of_points)

# Scale points by a factor
P[:, 1] = P[:, 1] * 2
P[:, 2] = P[:, 2] * 3
P[:, 3] = P[:, 3] * 4
P[:, 4] = P[:, 4] * 5

# Make random values negative
P[0:3, 2] = P[0:3, 2] * -1
P[:, 4] = P[:, 4] * -1

# Create generic labels
P_labels = []
for i in range(num_of_points):
    P_labels.append('Label {}'.format(i+1))

# Figure properties
plt.figure(figsize=(10, 6))

# Spider plot
angles = np.linspace(0, 2 * np.pi, num_of_points, endpoint=False).tolist()
angles += angles[:1]
for i in range(row_of_points):
    values = P[i].tolist()
    values += values[:1]
    plt.polar(angles, values, marker='o', linestyle='-', linewidth=2, markersize=5)

# Title properties
plt.title('Sample Spider Plot', fontweight='bold', fontsize=12)

# Legend properties
plt.legend(P_labels, loc='lower center')

# Show the plot
plt.show()