# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
 
df = px.data.gapminder() 
df = df[df['continent']=='Asia']

app = dash.Dash()
 
year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})
 
app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='select-year',options=year_options,value=df['year'].min())
])
 
@app.callback(Output('graph', 'figure'),
              Input('select-year', 'value'))
def update_figure(selected_year):
    filtered_df = df[df['year'] == selected_year]
    figure = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', log_x=True, color='continent')
    return figure

if __name__ == '__main__':
    app.run_server()