import pandas_datareader.data as web
import matplotlib.pyplot as plt

# collect data for Lyft from 2019-05-22 to 2020-01-01
start = '2019-04-22'
end = '2020-01-01'
symbol='LYFT DRIVER'

#Read from csv file


# rename the column with symbol name
#close = close.rename(columns={'close': "stock"})
ax = close.plot(title='Lyft')
ax.set_xlabel('date')
ax.set_ylabel('close price')
ax.grid()
plt.show()