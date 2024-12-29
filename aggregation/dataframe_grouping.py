import pandas as pd

df = pd.read_csv('../customers-100.csv')
print(df.head())

df['Date'] = pd.to_datetime(df['Subscription Date'], errors='coerce')
print(df['Date'])

df2 = df[['Customer Id', 'Country', 'Subscription Date']]
print(df2.head())

# Group by subscription date
noOfOccurrence = df2.groupby(['Subscription Date']).size().reset_index(name='noOfOccurrence')
print(noOfOccurrence)

print(df2['Subscription Date'].min())
print(df2['Subscription Date'].max())

