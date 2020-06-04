import pandas as pd
import talib
import matplotlib.pyplot as plot
from pandas_datareader import data as web

df = web.DataReader('msft', data_source='yahoo', start='01-01-2019')
close = df.Close
df["RSI"] = talib.RSI(close, timeperiod=14)

ax1 = plot.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plot.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)

ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['RSI'])
ax2.bar(df.index,df['Volume'])
plot.show()