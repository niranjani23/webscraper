import pandas_datareader.data as web
import matplotlib.pyplot as plt

# collect data for Amazon from 2017-04-22 to 2018-04-22
start = '2017-04-22'
end = '2018-04-22'
symbol='AMZN'
df = web.DataReader(name=symbol, data_source='iex', start=start, end=end)
df.index = df.index.to_datetime()
print(df)
df.to_csv("~/workspace/{}.csv".format(","))
# select only close column
close = df[['close']]
# rename the column with symbole name
close = close.rename(columns={'close': ","})
ax = close.plot(title='Amazon')
ax.set_xlabel('date')
ax.set_ylabel('close price')
ax.grid()
plt.show()