import pandas as pd
text = 'Hi, Arijit'
print(text.lower() + ' ' + str(1000))

df = pd.read_csv('customers-100.csv')
print(df.head())
print(df.tail())

print(df.columns)

df2 = df['Customer Id']
print(type(df2))
print(df.info())

# Print 2nd and 3rd rows by iloc
print(df.iloc[1:3])
print(df.loc[1:3])
