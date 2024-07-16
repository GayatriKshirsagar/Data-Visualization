# To make histogram of frequencies

# Plotly charts come with built-in zoom controls when you hover over the chart.
from plotly.graph_objs import Bar, Layout

# allows you to generate Plotly graphs and charts directly within your Python scripts, Jupyter notebooks,
# without needing to connect to the Plotly cloud service or the internet.
from plotly import offline

from die import Die

# Create two D6 dice.
die_1 = Die()
# die_2 = Die()
# If we want to roll two different sidede dice
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# for value in range(1, die.num_sides + 1):
for value in range(2, max_result + 1):
	# Count how many times each number appears
	frequency = results.count(value)
	frequencies.append(frequency)

# print(frequencies)

# Visualize the results.
# Plotly does not accept results of the range, so we need to convert them to a list
# x_values = list(range(1, die.num_sides+1))

x_values = list(range(2, max_result+1))

# The plotly class Bar() represents a data set that will be formatted as a bar chart
# It tells Plotly to display both the x-axis (result) and y-axis (frequency) values 
# when you hover over each bar in the chart.
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick' : 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title= 'Results of rolling a D6 and a D10 dice 50000 times',
		xaxis = x_axis_config, yaxis = y_axis_config)
# offline.plot({'data' : data, 'layout' : my_layout}, filename = 'd6.html')
offline.plot({'data' : data, 'layout' : my_layout}, filename = 'd6_d10.html')