import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plot
import plotly.graph_objects as go

start = datetime.datetime(2018, 5, 1)
end = datetime.datetime.now()
df = web.DataReader("hcci", 'yahoo', start, end)
df["100ma"] = df['Adj Close'].rolling(window=100,min_periods=0).mean()
df["50ma"] = df['Adj Close'].rolling(window=10,min_periods=0).mean()
# df["Adj Close"].plot()
# df["Close"].plot()
ax1 = plot.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plot.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)

ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['100ma'])
ax1.plot(df.index,df['50ma'])
ax2.bar(df.index,df['Volume'])
plot.show()
# print(df.tail())
# print(df.head())
# df.head()
# plot.show()
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

# print(df.head())