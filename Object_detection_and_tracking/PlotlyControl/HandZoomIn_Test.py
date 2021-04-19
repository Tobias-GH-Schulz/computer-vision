import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
import math
import numpy as np
import osascript

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import numpy as np



X = deque(maxlen = 20)
X.append(1)

Y = deque(maxlen = 20)
Y.append(1)

Z = deque(maxlen = 20)
Z.append(1)


"""
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                   mode='markers')])
"""
app = dash.Dash(__name__)
  
app.layout = html.Div(
    [
        dcc.Graph(id = 'live-graph', animate = True),
        dcc.Interval(
            id = 'graph-update',
            interval = 1000,
            n_intervals = 0
        ),
    ]
)
  
@app.callback(
    Output('live-graph', 'figure'),
    [ Input('graph-update', 'n_intervals') ]
)

  
def update_graph_scatter(n):
    """x_eye = random.uniform(0.1, 2.5)
    y_eye = random.uniform(0.1, 2.5)
    z_eye = 0.1"""

    X.append(X[-1]+X[-1] * random.uniform(-0.1,0.1))
    Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
    Z.append(Z[-1]+Z[-1] * random.uniform(-0.1,0.1))




    data = plotly.graph_objs.Scatter3d(
            x=list(X),
            y=list(Y),
            z=list(Z),
            name='Scatter',
            mode= 'markers'
    )
  
    return {'data': [data],
            'layout' : go.Layout(xaxis=dict(
                    range=[min(X),max(X)]),yaxis = 
                    dict(range = [min(Y),max(Y)])
                    )}
            

"""'layout' : go.Layout(scene_camera=dict(eye=dict(x=x_eye, y=y_eye, z=z_eye)))}"""

if __name__ == '__main__':
    app.run_server()