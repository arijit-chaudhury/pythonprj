import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

df = pd.read_csv('../customers-100.csv')
df['Date'] = pd.to_datetime(df['Subscription Date'], errors='coerce')
print(df.head())

df2 = df[['Customer Id', 'Date']]
print(df2.head())

# Group by subscription date
noOfOccurrence = df2.groupby(['Date']).size().reset_index(name='noOfOccurrence')
print(noOfOccurrence)

# find min and max values
min_date = df2['Date'].min()
max_date = df2['Date'].max()

# Try date range from minimum and maximum value
# per1 = pd.date_range(start=min_date, end=max_date, freq='ME')
#for val in per1:
#    print(val)
dt = timedelta(days=30)
dates = np.arange(min_date, max_date, dt).astype(datetime)
print(dates)

n = pd.period_range(start=min_date, end=max_date, freq='M')
print(n)

filterData = (df2['Date'] > min_date) & (df2['Date'] <= max_date)
df3 = df2.loc[filterData]
print(df3)

noOfOccurrence.plot.scatter(x='Date', y='noOfOccurrence')
#plt.show()
