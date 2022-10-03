# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_table
import plotly.express as px
import pandas as pd
 
df = px.data.gapminder() 

app = dash.Dash()
 
app.layout = html.Div(
    [
        html.H1('GapMinder Data', style={"textAlign":"center"}),
        dash_table.DataTable(
            style_cell={"textAlign":"center"},
            fixed_rows={"headers":True},
            page_size=15,
            filter_action = 'native', #おまけ
            sort_action = 'native',   #おまけ

            columns=[{"name":col, "id":col} for col in df.columns],
            data = df.to_dict("records")
        )
    ]
) 

if __name__ == '__main__':
    app.run_server()