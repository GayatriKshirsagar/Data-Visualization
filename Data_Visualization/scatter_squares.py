# To plot single point (x,y) use scatter() method

import matplotlib.pyplot as plt 
# Ensures that the y-axis labels are formatted in plain style without scientific notation.
from matplotlib.ticker import ScalarFormatter

# To plot series of points using scatter, passing two lists
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# Using Loop instead of lists
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# s argument sets the size of the dot shown at point (2,4)
# ax.scatter(2,4, s = 200)

# Plot series of points, c for changing the colors of the points
# ax.scatter(x_values, y_values, c = 'blue', s = 10)

# This code colors th points with lower y-values light blue and 
# colors the points with higher y-values dark blue
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds, s = 10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set size of tick labels.
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

# Set the range for each axis, min x_axis value : 0, max x_axis value : 1100...similar for y axis
# ax.axis([0, 1100, 0, 1100000])
ax.set_xlim(0, 1100)
ax.set_ylim(0, 1100000)


# Set ScalarFormatter to format y-axis labels without scientific notation
ax.yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
ax.ticklabel_format(style='plain', axis='y')

# plt.show()

# Automatically save the plot to a file
# second argument trims extra whitespace from the plot
plt.savefig('scatter_squares_plot.png', bbox_inches = 'tight')