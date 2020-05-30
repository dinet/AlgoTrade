import pandas as pd
import webbrowser
from pandas_datareader import data as web
import plotly.graph_objects as go

total = 0


def GetSMA(ticker):
    global total
    try:
        df = web.DataReader(ticker, data_source='yahoo', start='01-01-2019')
    except:
        return
    # Calculate and define moving average of 30 periods
    avg_30 = df.Close.rolling(window=20, min_periods=1).mean()

    # Calculate and define moving average of 50 periods
    avg_50 = df.Close.rolling(window=50, min_periods=1).mean()
    # diff = avg_50.subtract(avg_30)
    if(avg_30.iloc[-1] < df.Close.iloc[-1] < avg_50.iloc[-1]):
        # trace1 = {
        #     'x': df.index,
        #     'open': df.Open,
        #     'close': df.Close,
        #     'high': df.High,
        #     'low': df.Low,
        #     'type': 'candlestick',
        #     'name': ticker,
        #     'showlegend': False
        # }
        # trace2 = {
        #     'x': df.index,
        #     'y': avg_30,
        #     'type': 'scatter',
        #     'mode': 'lines',
        #     'line': {
        #         'width': 1,
        #         'color': 'blue'
        #             },
        #     'name': 'Moving Average of 30 periods'
        # }

        # trace3 = {
        #     'x': df.index,
        #     'y': avg_50,
        #     'type': 'scatter',
        #     'mode': 'lines',
        #     'line': {
        #         'width': 1,
        #         'color': 'red'
        #     },
        #     'name': 'Moving Average of 50 periods'
        # }

        # trace4 = {
        #     'x': df.index,
        #     'y': diff,
        #     'type': 'scatter',
        #     'mode': 'lines',
        #     'line': {
        #         'width': 1,
        #         'color': 'green'
        #     },
        #     'name': 'Moving average Diff'
        # }

        # data = [trace1, trace2, trace3, trace4]
        # # Config graph layout
        # layout = go.Layout({
        #     'title': {
        #         'text': f'{ticker} Moving Averages',
        #         'font': {
        #             'size': 15
        #         }
        #     }
        # })

        # fig = go.Figure(data=data, layout=layout)
        # # fig.write_html("Microsoft(MSFT) Moving Averages.html")
        # fig.show()
        total += 1
        with open('E:\watchlist.csv', 'a') as fd:
            fd.write(f'{ticker}\n')
        print(
            f"{ticker} Matched 20:{avg_30.iloc[-1]} Close {df.Close.iloc[-1]} 50 :{avg_50.iloc[-1]} Total : {total}")
        webbrowser.open(f'https://finance.yahoo.com/chart/{ticker}', new=2)
    else:
        total += 1
        print(
            f"{ticker} Not Matched 20:{avg_30.iloc[-1]} Close {df.Close.iloc[-1]} 50 :{avg_50.iloc[-1]} Total : {total}")


df = pd.read_csv('E:\projects\AlgoTrade\companylist.csv')
# df2 = df.loc[df['Sector'] == 'Technology']
print(f'Total tickers found {len(df.index)}')
for key, value in df.Symbol.iteritems():
    GetSMA(value)
print(f'Total : {total} Processed')
# GetSMA("DDOG")
