import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

# Making a count of all earthquakes
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Extracting Magnitudes & location data (latitude, longitude)
mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	title = eq_dict['properties']['title']

	mags.append(mag)
	lons.append(lon)
	lats.append(lat)
	hover_texts.append(title)

print(mags[:10])
print(lons[:5])
print(lats[:5])

# Map the earthquakes
# Create Scattergeo object inside this list
# data = [Scattergeo(lon=lons, lat=lats)]
data = [Scattergeo(
	lon = lons,
	lat = lats,
	text = hover_texts,
	marker = dict(
		# we want the size to correspond to magnitude of an earthquake
		size=[5 * mag for mag in mags],
		color = mags,
		colorscale = 'Viridis',
		reversescale = True,
		colorbar = dict(title = 'Magnitude')
	),
)]
my_layout = Layout(title = 'Global Earthquakes')

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename = 'global_earthquakes.html')

readable_file = 'data/readable_eq_data.json'

# Open the new file and write in it. We call it f.
with open(readable_file, 'w') as f:
	json.dump(all_eq_data, f, indent = 4)