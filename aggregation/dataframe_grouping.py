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

print(df2['Date'].min())
print(df2['Date'].max())

noOfOccurrence.plot.scatter(x='Date', y='noOfOccurrence')
plt.show()






