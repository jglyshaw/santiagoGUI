import plotly.graph_objects as go
import numpy as np
from MLEngine import MLEngine

# Helix equation


mlEngine = MLEngine()
neuron = mlEngine.createNeuron(182, 't')
nodes = mlEngine.nodesDictionary(neuron)
edges = mlEngine.edgesList(neuron, nodes)
fig = go.Figure()

# t = np.linspace(0, 10, 50)
# x, y, z = np.cos(t), np.sin(t), t
# fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode="markers", showlegend=False, marker=dict(size=3), opacity=0.8))


x = []
y = []
z = []
for id in nodes:
    x1, y1, z1, area1 = nodes[id]
    x.append(x1)
    y.append(y1)
    z.append(z1)
fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode="markers", showlegend=False, marker=dict(size=3), opacity=0.8))
print("done1")
for line in edges:
    a = line[0]
    b = line[1]
    fig.add_trace(go.Scatter3d(x=[a[0],b[0]], y=[a[1],b[1]], z=[a[2],b[2]], mode="lines", showlegend=False, line=dict(color="#0000ff")))

surface = mlEngine.eng.GetSurface(neuron)
x = np.asarray(surface[0][0])
y = np.asarray(surface[0][1])
z = np.asarray(surface[0][2])
i = 0
for segment in surface:
    if i == 0:
        i += 1
        continue
    x = np.concatenate((x, segment[0]))
    y = np.concatenate((y, segment[1]))
    z = np.concatenate((z, segment[2]))
fig.add_trace(go.Surface(x=x, y=y, z=z, opacity=0.1))

fig.show()
