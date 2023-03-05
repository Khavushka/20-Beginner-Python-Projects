# graph plotter project
# installing matplotlib

import matplotlib.pyplot as plt

x = [2, 4, 5, 1, 5]
y = [2, 3, 6, 5, 8]

plt.plot(x, y, color = 'blue', linestyle = 'dashed', linewidth = 2, marker = 'o', markerfacecolor = 'green', markersize = 12)
# plt.ylim(x, y)
plt.ylim(1, 8)
plt.xlim(1, 8)


# plt.plot(x, y, label = 'line 1')

# x2 = [4, 6, 7, 8]
# y2 = [3, 7, 2, 9]

# plt.plot(x2, y2, label ='line 2')

plt.xlabel('X axis')

plt.ylabel('Y axis')

plt.title('Demo graph - Two lines')

plt.legend()

plt.show()