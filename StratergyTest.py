from indicators import SuperTrend
import pandas as pd
import webbrowser
from pandas_datareader import data as web
import plotly.graph_objects as go
try:
    df = web.DataReader('msft', data_source='yahoo', start='01-01-2019')
except expression as identifier:
    pass
SuperTrend(df, 10,3)
print(df.head)
