# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

### -----------------------

df = sns.load_dataset('tips')

use_data = df[['total_bill','size','time','tip']]
use_data = pd.get_dummies(use_data, drop_first=True)

#目的変数と説明変数
X = use_data[['total_bill','size','time_Dinner']]
Y = use_data[['tip']]

#線形重回帰で数値予測のモデリング
clf = LinearRegression()
clf.fit(X, Y)

#表示するグラフの作成
from plotly.subplots import make_subplots
import plotly.graph_objects as go

tip_plots = make_subplots(rows=1, cols=3, start_cell="bottom-left")
tip_plots.add_trace(go.Box(x=df['time'], y=df['tip'], name='time vs tip'), row=1, col=1)
tip_plots.add_trace(go.Scatter(x=df['total_bill'], y=df['tip'], mode='markers', name='total bill vs tip'), row=1, col=2)
tip_plots.add_trace(go.Scatter(x=df['size'], y=df['tip'], mode='markers', name='size vs tip'), row=1, col=3)
tip_plots.update_layout(
    xaxis_title_text='Time (Lunch or Dinner)', 
    yaxis_title_text='Tip [$]'
)
tip_plots.update_layout(
    xaxis2_title_text='Total bill [$]', 
    yaxis2_title_text='Tip [$]'
)
tip_plots.update_layout(
    xaxis3_title_text='Size [人]', 
    yaxis3_title_text='Tip [$]'

)

### -------------------------


app = dash.Dash()

app.layout = html.Div(
    [
        html.H1('チップの額を予測するアプリだよ', style={"textAlign":"center"}),
        html.H3('まずは分析に使うチップのデータを見せるね！'),  #style={"textAlign":"center"}),
        dash_table.DataTable(
            style_cell={"textAlign":"center",'width':'150px'},
            fixed_rows={"headers":True},
            page_size=10,
            filter_action = 'native', #おまけ
            sort_action = 'native',   #おまけ

            columns=[{"name":col, "id":col} for col in df.columns],
            data = df.to_dict("records"),
            fill_width=False
        ),
        html.P('モデリングに使うデータは{}件だよ'.format(len(df))),
        html.H3('さて次はグラフを見てみよう！（今回はグラフは固定）'),
        #プロットの表示
        dcc.Graph(
            id='graph',
            figure=tip_plots,
            style={}    
        ),

        html.H3('最後に予測用のデータをインプットしよう！'),
        #total_bil, size, time を選択するスライダーやボタン
        #何かサブミット的なボタンが必要？
        dcc.Input(
            id='total_bill',
            placeholder='total_bill ここに値を入れてね！',
            type='text',
            style={'width':'20%'},
            value="" #値を入れとかないとpredのときにエラーが出る  
        ),
        dcc.Input(
            id='size',
            placeholder='size ここに値を入れてね！',
            type='text',
            style={'width':'20%'},
            value="" #値を入れとかないとpredのときにエラーが出る
        ),
        dcc.RadioItems(
            id='time',
            options=[
                {'label': 'ランチ', 'value': 'Lunch'},
                {'label': 'ディナー', 'value': 'Dinner'}        
            ],
            value='Lunch',
            labelStyle={'display': 'inline-block'}
        ),
        html.Button(id="submit-button", n_clicks=0, children="Submit"),

        html.H3('チップの額はいくらと予測されるかな？'),
        html.Div(id='output-pred', style={"textAlign":"center", "color":"red", "fontSize":30}),
    ]
) 
@app.callback(Output('output-pred', 'children'),
            [Input('submit-button','n_clicks')],
            [State('total_bill', 'value'),
            State('size', 'value'),
            State('time','value')]
)
def prediction(n_clicks, total_bill, size, time):
#def prediction(submit-button, total_bill, size, time):
    if time=='Lunch':
        dinner01 = 0
    else:
        dinner01 = 1

    if (total_bill and size):
        value_df = pd.DataFrame([],columns=['Total bill','Size','Dinner flag'])
        record = pd.Series([total_bill, size, dinner01], index=value_df.columns, dtype='float64')
        value_df = value_df.append(record, ignore_index=True)
        Y_pred = clf.predict(value_df) 

        return_text = 'チップ額はおそらく'+ str('{:.2g}'.format(Y_pred[0,0]) +'ドルくらいでしょう !!!')
        return return_text
    else:
        return 'ちゃんとデータを入力してね！'

if __name__ == '__main__':
    app.run_server()
