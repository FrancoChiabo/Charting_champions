#!/bin/python3
from pygal import Pie

# Create a chart
chart = Pie(title = 'GDP')

# Add data to the chart
with open("gdp.csv") as f:
    for line in f:
        #print(line)
        pieces = line.split(',') # Breaks the string into a list
        #print(pieces) # Print each list
        team = pieces[0]
        gdp = pieces[1]
        chart.add(team, float(gdp))  # Make medals a number

# Display the chart
chart.render()