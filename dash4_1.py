# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    html.H1('コールバック'),
    dcc.Input(id='input-text-id', value='initial value', type='text'),
    html.Div(id='output-div-id')
])

@app.callback(
    Output('output-div-id', 'children'),
    Input('input-text-id', 'value')
)
def update_output_div(input_value):
    return '入力は "{}"です。'.format(input_value)

if __name__ == '__main__':
    app.run_server()