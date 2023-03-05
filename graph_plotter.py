# graph plotter project
# installing matplotlib

import matplotlib.pyplot as plt

x = [2, 4, 5, 1, 5]
y = [2, 3, 6, 5, 8]

plt.plot(x, y, label = 'line 1')

x2 = [4, 6, 7, 8]
y2= [3, 7, 2, 9]

plt.xlabel('X axis')

plt.ylabel('Y axis')

plt.title('Demo graph')

plt.show()