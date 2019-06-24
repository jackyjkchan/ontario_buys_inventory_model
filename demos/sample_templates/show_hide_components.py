import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash('example1')

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown-to-show_or_hide-element',
        options=[
            {'label': 'Show element', 'value': 'on'},
            {'label': 'Hide element', 'value': 'off'}
        ],
        value='on'
    ),
    dcc.Input(
        id='element-to-hide',
        placeholder='something',
        value='Can you see me?'
        ),
    html.Div([html.P("Some text"),
              dcc.Input(
                  id="input1",
                  value="testing"
              )],
             id="block1"
             )
    ])


@app.callback(
   Output(component_id='block1', component_property='style'),
   [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')])
def show_hide_element(visibility_state):
    if visibility_state == 'on':
        return {'display': 'block'}
    if visibility_state == 'off':
        return {'display': 'none'}


@app.callback(
   Output(component_id='element-to-hide', component_property='style'),
   [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')])
def show_hide_html_element(visibility_state):
    if visibility_state == 'on':
        return {'display': 'block'}
    if visibility_state == 'off':
        return {'display': 'none'}


if __name__ == '__main__':
    app.run_server(debug=True)
