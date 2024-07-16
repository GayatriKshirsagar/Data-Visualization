import csv

# Plotting dates
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	# This returns the next line in the file
	header_row = next(reader)

	# The enumerate function allows you to loop over something (like list) and have an automatic counter,
	#  so you don't have to manually increment a counter inside the loop.
	for index, column_header in enumerate(header_row):
		print(index, column_header)

	# Get dates and high temperatures from this file

	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		# try, except and else block to show error if any value is missing ''
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)


	# Plot the high temperatures.
	plt.style.use('seaborn-v0_8')
	fig, ax = plt.subplots()
	# alpha argument controls a color's transparency, 0 is completely transparent
	ax.plot(dates, highs, c = 'red', alpha = 0.5)
	ax.plot(dates, lows, c = 'red', alpha = 0.5)
	plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

	# Format plot
	plt.title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize = 22)
	plt.xlabel('', fontsize = 16)
	# Draws the date labels diagonally to prevent overlapping
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize = 16)
	plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

	plt.savefig('death_valley_highs_lows_plot.png', bbox_inches = 'tight')