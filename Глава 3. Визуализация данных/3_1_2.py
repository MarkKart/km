import matplotlib.pyplot as plt
import numpy as np

x_data = np.arange(0, 10, 0.01)
y_data = np.cos(x_data)

fig = plt.figure(figsize=(10, 5))
ax = plt.axes()
plt.scatter(x_data, y_data, color = 'b', marker = 'o',
        label = 'cos(x)')
leg = ax.legend()
ax.grid(color = 'grey', linewidth = 0.8, linestyle = '--')
figsize =(10,5)
plt.xlabel('x_data')
plt.ylabel('y_data')
plt.title('function cos(x)')
plt.show()