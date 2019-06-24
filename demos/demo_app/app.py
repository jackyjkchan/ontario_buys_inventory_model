import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import demos.demo_app.components as components
import demos.demo_app.graphs as graphs

app = dash.Dash('example')

app.layout = html.Div([
    *components.demand_selection,
    *components.demand_histogram,
    *components.simple_random_walk
])


@app.callback(
   Output(component_id='set_poisson_mean', component_property='style'),
   [Input(component_id='demand_selection', component_property='value')])
def show_poisson_inputs(selection):
    return {'display': 'block'} if selection == 'poisson' else {'display': 'none'}


@app.callback(
   [Output(component_id='set_binomial_n', component_property='style'),
    Output(component_id='set_binomial_p', component_property='style')],
   [Input(component_id='demand_selection', component_property='value')])
def show_nb_inputs(selection):
    on = [{'display': 'block'}]*2
    off = [{'display': 'none'}]*2
    return on if selection == 'binomial' else off


@app.callback(
   Output(component_id='demand_histogram', component_property='figure'),
   [Input(component_id='demand_selection', component_property='value'),
    Input(component_id='set_poisson_mean', component_property='value'),
    Input(component_id='set_binomial_n', component_property='value'),
    Input(component_id='set_binomial_p', component_property='value')])
def show_demand_histogram(family, poisson_mean, binom_n, binom_p):
    if family == "poisson":
        r = graphs.poisson_graph(poisson_mean)
        return graphs.poisson_graph(poisson_mean)
    elif family == "binomial":
        return graphs.binomial_graph(binom_n, binom_p)
    else:
        return graphs.binomial_graph(binom_n, binom_p)


@app.callback(
   Output(component_id='simulation_trace', component_property='figure'),
   [Input(component_id='run_button', component_property='n_clicks'),
    Input(component_id='init_inventory', component_property='value')],
   [State(component_id='demand_selection', component_property='value'),
    State(component_id='set_poisson_mean', component_property='value'),
    State(component_id='set_binomial_n', component_property='value'),
    State(component_id='set_binomial_p', component_property='value')])
def update_simulation_trace(n_clicks, init_value, family, poisson_mean, binom_n, binom_p):
    n = poisson_mean if family=="poisson" else binom_n
    return graphs.simple_random_walk(None, None, None, None, n=n, init=int(init_value), seed=n_clicks)


if __name__ == '__main__':
    app.run_server(debug=True)
