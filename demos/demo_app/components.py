import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

demand_selection = [
    html.Div(children='''
    Demand Distribution
    '''),
    dcc.Dropdown(
        id='demand_selection',
        options=[
            {'label': 'Poisson', 'value': 'poisson'},
            {'label': 'Binomial', 'value': 'binomial'}
        ],
        value='poisson'
    ),
    dcc.Input(
        id='set_poisson_mean',
        value=5,
        type="number"
    ),
    dcc.Input(
        id='set_binomial_n',
        value=3,
        type="number",
        min=1,
    ),
    dcc.Input(
        id='set_binomial_p',
        value=0.5,
        type="number",
        min=0,
        max=1,
        step=0.05
    )
]

demand_histogram = [dcc.Graph(id='demand_histogram')]

simple_random_walk = [html.Div(children='Initial Inventory'),
                      dcc.Input(
                            id='init_inventory',
                            value=10,
                            type="number"
                      ),
                      html.Button(id='run_button', n_clicks=0, children='Run'),
                      dcc.Graph(id='simulation_trace')]
