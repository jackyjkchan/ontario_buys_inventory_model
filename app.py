import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

graph = dcc.Graph(id='histogram_1')

app.layout = html.Div([
    dcc.Input(id='my-id', value=4, type='number'),
    graph
])

@app.callback(
    Output(component_id='histogram_1', component_property='figure'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    print(input_value)
    x = np.random.poisson(input_value, 10000)
    return go.Figure(
        data=[
            go.Histogram(
                x=x,
                histnorm='probability',
                opacity=0.5)
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=True)
