# Importing Libraries
import plotly.graph_objs as go
import numpy as np

np.random.seed(3)

# generating numbers ranging from 0 to 18 on X-axis
x = list(range(0,20,2))

# generating random numbers on y-axis
y = np.random.randn(10)

z = np.random.randn(10)

# plotting scatter plot on x and y data with
# 'lines' as mode
fig = go.Figure(data=go.Scatter3d(x=x, y=y, z=z))

# setting the y-axis range from -3 to 3
fig.update_layout(yaxis_range=[-10,10])

# to display the figure in the output screen
fig.show()