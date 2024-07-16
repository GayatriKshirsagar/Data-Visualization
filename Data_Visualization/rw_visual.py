import matplotlib.pyplot as plt 

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
	# Make a random walk.

	rw = RandomWalk(50_000)
	rw.fill_walk()

	# Plot the points in the walk.
	plt.style.use('classic')

	#To make pltting window better fit your screen
	fig, ax = plt.subplots(figsize = (15, 9))

	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values,c = point_numbers, cmap = plt.cm.Blues,
	 edgecolors = 'none', s = 1)

	# Emphasize the first and last points.
	# starting point
	ax.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
	# Last point
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

	# Remove the axes.
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	# second argument trims extra whitespace from the plot
	plt.savefig('rw_visuals_plot.png', bbox_inches = 'tight')

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break