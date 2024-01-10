import numpy as np
import plotly.express as px


arr = np.arange(-10, 10, 0.1)

fn = 1 / (1 + np.exp(-arr))  # сигма распределение
fig = px.line(x=arr, y=fn, title='Sigma')
fig.show()

fn1 = 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * arr**2)  # распределние по гауссу
fig1 = px.line(x=arr, y=fn1, title='Gauss')
fig1.show()