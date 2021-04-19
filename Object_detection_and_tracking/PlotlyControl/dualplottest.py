import dash
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np


app = dash.Dash(__name__)

X, Y, Z = np.random.random((3, 50))


app.layout = html.Div([
        dcc.Graph(
            id='main-figure',
            figure=go.Figure(data=go.Scatter3d(x=X, y=Y, z=Z))
            ),
        dcc.Graph(
            id='other-figure',
            figure=go.Figure(data=go.Scatter3d(x=X, y=Y, z=Z))
            ),

        ]
        )

#app.run_server(debug=False, port=8065)

def rotate_z(x, y, z, theta):
    w = x + 1j * y
    return np.real(np.exp(1j * theta) * w), np.imag(np.exp(1j * theta) * w), z

@app.callback(
    Output('other-figure', 'figure'),
    [Input('main-figure', 'relayoutData')])
def sync1(data):
    if data and 'scene.camera' in data:
        fig=go.Figure(data=go.Scatter3d(x=X, y=Y, z=Z))
        print(data['scene.camera']["eye"])
        #for t in np.arange(0, 6.26, 0.1):
        #    xe, ye, ze = rotate_z(1.6, 1.45, 0.2, -t)
        #data["scene.camera"]["eye"] = {"x": xe, "y": 1.45, "z":0.2}
        fig.update_layout(scene_camera=data['scene.camera'])
        return fig
    else:
        raise PreventUpdate


@app.callback(
    Output('main-figure', 'figure'),
    [Input('other-figure', 'relayoutData')])
def sync2(data):
    if data and 'scene.camera' in data:
        fig=go.Figure(data=go.Scatter3d(x=X, y=Y, z=Z))
        fig.update_layout(scene_camera=data['scene.camera'])
        return fig
    else:
        raise PreventUpdate


if __name__ == '__main__':
    app.run_server(debug=True, port=8065)