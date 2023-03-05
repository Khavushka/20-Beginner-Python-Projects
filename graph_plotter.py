# graph plotter project
# installing matplotlib

import matplotlib.pyplot as plt

left = [1, 2, 3, 4, 5]
height = [10, 11, 13, 15, 4]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label = tick_label, width = 0.8, color=['red', 'yellow'])

# plt.plot(left, height, color = 'blue', linestyle = 'dashed', linewidth = 2, marker = 'o', markerfacecolor = 'green', markersize = 12)
# plt.ylim(x, y)
# plt.ylim(1, 8)
# plt.xlim(1, 8)


# plt.plot(x, y, label = 'line 1')

# x2 = [4, 6, 7, 8]
# y2 = [3, 7, 2, 9]

# plt.plot(x2, y2, label ='line 2')

plt.xlabel('X axis')

plt.ylabel('Y axis')

# plt.title('Demo graph - Two lines')
plt.title('Demo graph - Bar Chart')

# plt.legend()

plt.show()