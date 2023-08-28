# now that I have installed matplotlib with pip install matplotlib
# , I can import it

import matplotlib.pyplot as plt # very common to import as plt

# create a list of x values
x_values = list(range(20))
# y will be squares of x
y_values = [n**2 for n in x_values]

# plot the points
plt.plot(x_values, y_values)

# there are many many options such as title, axis labels, etc.
# see https://matplotlib.org/stable/tutorials/index
# different plots
# https://matplotlib.org/stable/gallery/index.html
plt.title("Square Numbers", fontsize=24)
# show the plot
# show grid
plt.grid(True)
# set axis labels
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.show() # shows interactive plot

# there are many other plotting libraries such as Plotly, Bokeh, Seaborn, etc.