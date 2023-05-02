import matplotlib.pyplot as plt
import numpy as np

x_data = np.arange(0, 10, 0.01)
y_data = np.sin(x_data)

fig = plt.figure(figsize=(10, 5))
ax = plt.axes()
ax.plot(x_data, y_data, color = 'r', linewidth = 1.0,
        label = 'sin(x)')
leg = ax.legend()
ax.grid(color = 'grey', linewidth = 0.8, linestyle = '--')
figsize =(10,5)
plt.xlabel('x_data')
plt.ylabel('y_data')
plt.title('function sin(x)')
plt.show()