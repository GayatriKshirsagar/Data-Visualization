import csv

# Plotting dates
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	# This returns the next line in the file
	header_row = next(reader)

	# The enumerate function allows you to loop over something (like list) and have an automatic counter,
	#  so you don't have to manually increment a counter inside the loop.
	for index, column_header in enumerate(header_row):
		print(index, column_header)

	# Get dates and high temperatures from this file

	dates, highs = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		dates.append(current_date)
		highs.append(high)

	print(highs)

	# Plot the high temperatures.
	plt.style.use('seaborn-v0_8')
	fig, ax = plt.subplots()
	ax.plot(dates, highs, c = 'red')

	# Format plot
	plt.title("Daily high temperatures, July 2018, fontsize = 24")
	plt.xlabel('', fontsize = 16)
	# Draws the date labels diagonally to prevent overlapping
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize = 16)
	plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

	plt.savefig('sitka_highs_plot.png', bbox_inches = 'tight')