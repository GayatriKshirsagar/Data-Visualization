# To make histogram of frequencies

# Plotly charts come with built-in zoom controls when you hover over the chart.
from plotly.graph_objs import Bar, Layout

# allows you to generate Plotly graphs and charts directly within your Python scripts, Jupyter notebooks,
# without needing to connect to the Plotly cloud service or the internet.
from plotly import offline

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1):
	# Count how many times each number appears
	frequency = results.count(value)
	frequencies.append(frequency)

# print(frequencies)

# Visualize the results.
# Plotly does not accept results of the range, so we need to convert them to a list
x_values = list(range(1, die.num_sides+1))

# The plotly class Bar() represents a data set that will be formatted as a bar chart
# It tells Plotly to display both the x-axis (result) and y-axis (frequency) values 
# when you hover over each bar in the chart.
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title= 'Results of rolling one D6 1000 times',
		xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data' : data, 'layout' : my_layout}, filename = 'd6.html')