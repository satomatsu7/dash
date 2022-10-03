# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_design_kit as ddk
import pandas as pd
import plotly.express as px

df = px.data.gapminder()

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
        # Dash: test core components
    '''),

    html.H2(children='Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': '東京', 'value': 'Tokyo'},
            {'label': '大阪', 'value': 'Osaka'},
            {'label': '北海道', 'value': 'Hokkaido'}
        ], value='MTL', multi=True
    ) ,

    html.H2(children='Slider'),
    html.Div(children='slider'),
    dcc.Slider(
        min=-10,
        max=10,
        step=1,
        value=0
    ) ,

    html.H2(children='Input Value'),
    dcc.Input(
        placeholder='ここに値を入れてね！',
        type='text',
        value=''
    ),

    html.H2(children='Input Text'),
    dcc.Textarea(
        placeholder='ここに値を入れてね！',
        #value='ここに値を入れてね！',
        style={'width': '100%'}
    ),

    html.H2(children='Check List'),
    dcc.Checklist(
    options=[
            {'label': '東京', 'value': 'Tokyo'},
            {'label': '大阪', 'value': 'Osaka'},
            {'label': '北海道', 'value': 'Hokkaido'}
    ], value=['Tokyo', 'Osaka']
    ),  

    html.H2(children='Radio button'),
    dcc.RadioItems(
        options=[
            {'label': '東京', 'value': 'Tokyo'},
            {'label': '大阪', 'value': 'Osaka'},
            {'label': '北海道', 'value': 'Hokkaido'}        
        ],
        value='Osaka',
        labelStyle={'display': 'inline-block'}
    )  

])

if __name__ == '__main__':
    app.run_server()
