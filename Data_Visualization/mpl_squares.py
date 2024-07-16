import matplotlib.pyplot as plt 
# x-axis values
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Use style from predefined styles for plotting
plt.style.use('seaborn-v0_8')

# fig is entire figure, i.e. collection of plots & ax is single plot in figure
# subplots() generate one or more plots in the same figure
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

# Set chart title and lebel axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set size of tick labels.
ax.tick_params(axis = 'both', labelsize = 14)

# Opens matplotlib viewer and displays the plot
# plt.show()

# second argument trims extra whitespace from the plot
plt.savefig('mpl_squares_plot.png', bbox_inches = 'tight')