# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")

app.layout = dbc.Container([
    html.Div([
        html.H1('Choose Graph CSS-Transform Scale', id='title'),
        html.H2(id='subtitle'),
        dcc.Slider(
            id='my-slider',
            min=0.8,
            max=1.2,
            step=0.05,
            value=0.8,
        )
    ], id='header'),
    html.Div([
        dcc.Graph(figure=fig, id='chart')
        ], id='content')
    ], id='page', className="p-5"
)

@app.callback(
    [dash.dependencies.Output('content', 'style'), dash.dependencies.Output('subtitle', 'children')],
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return {'transform': 'scale({})'.format(value), 'transform-origin': 'top left'},\
        'Current: transform: scale({})'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)