import matplotlib.pyplot as plt
import random

#X = [-]
#Y = [-]
#Z = [-]

x_data = [random.randint(0, 100) for x in range(100)]

fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3)


ax1.hist(x_data, bins = 10, color = 'r')
ax2.hist(x_data, bins = 30, color = 'g')
ax3.hist(x_data, bins = 50, color = 'b')

plt.show()