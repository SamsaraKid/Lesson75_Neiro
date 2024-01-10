import numpy as np
import plotly.graph_objs as go

arr = np.arange(-10, 10, 0.1)

fn = 1 / (1 + np.exp(-arr))  # сигма распределение
w1 = 0.2
w2 = 0.7
w3 = 2
fig = go.Figure()
o1 = 'w=0.2'
o2 = 'w=0.7'
o3 = 'w=2'
graf1 = go.Scatter(x=arr, y=fn, name='sigma', mode='lines')
fig.add_trace(graf1)

mas = [(w1, o1), (w2, o2), (w3, o3)]
for m in mas:
    fn = 1 / (1 + np.exp(-arr*m[0]))
    graf1 = go.Scatter(x=arr, y=fn, name=m[1], mode='markers')
    fig.add_trace(graf1)
fig.show()