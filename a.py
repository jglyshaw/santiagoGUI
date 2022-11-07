import plotly.express as px
import numpy as np
import pandas as pd

# Create a dataset
data = {
   'year':[2019,2020,2021,2022],
   'loss':[0,1,2,3],
   'gain':[90,91,92,93],
   'profit':[100,90,95,97]
}
df = pd.DataFrame(data)

# generate the line plot
fig = px.line_3d(df, x='year', y='loss',z='gain')

fig.show()