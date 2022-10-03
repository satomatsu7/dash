# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

df = px.data.gapminder()

markdown_text = '''
# Test Dash/Markdown

This is markdown!
Dash Tutorial web page is here (https://dash.plotly.com)!
'''

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash H1!!!', style={"color":"red"}),
    html.H2(children='Hello Dash H2!!!'),
    html.H3(children='Hello Dash H3!!!', style={"color":"blue"}),
    html.H4(children='Hello Dash H4!!!', style={"textAlign":"center"}),
    html.Div(children='Dash Application'),

    dcc.Graph(
        id='テスト用のグラフ',
        figure=px.scatter(df, x='gdpPercap', y='lifeExp', log_x=True, hover_name='continent'),
        style={}    
    ),

    dcc.Markdown(children=markdown_text)

])

if __name__ == '__main__':
    app.run_server(debug=True)
