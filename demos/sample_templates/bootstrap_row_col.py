import dash_bootstrap_components as dbc
import dash_html_components as html
import dash

layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]
        ),
    ]
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)
