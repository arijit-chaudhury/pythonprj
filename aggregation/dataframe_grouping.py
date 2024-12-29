import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../customers-100.csv')
print(df.head())

df['Date'] = pd.to_datetime(df['Subscription Date'], errors='coerce')
print(df.head())

df2 = df[['Customer Id', 'Date']]
print(df2.head())

# Group by subscription date
noOfOccurrence = df2.groupby(['Date']).size().reset_index(name='noOfOccurrence')
print(noOfOccurrence)

min_date = df2['Date'].min()
max_date = df2['Date'].max()

per1 = pd.date_range(start=min_date, end=max_date, freq='30D')
for val in per1:
    print(val)

noOfOccurrence.plot.scatter(x='Date', y='noOfOccurrence')
plt.show()
