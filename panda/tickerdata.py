import pandas_datareader.data as web
import matplotlib.pyplot as plt

# collect data for Lyft from 2019-05-22 to 2020-01-01
start = '2019-04-22'
end = '2020-01-01'
symbol='LYFT'
df = web.DataReader(name=symbol, data_source='iex', start=start, end=end)
#df.index = df.index.to_datetime()
print(df)
df.to_csv("~/workspace/{}.csv".format("stock"))
# select only close column
close = df[['close']]
# rename the column with symbol name
close = close.rename(columns={'close': "stock"})
ax = close.plot(title='Lyft')
ax.set_xlabel('date')
ax.set_ylabel('close price')
ax.grid()
plt.show()