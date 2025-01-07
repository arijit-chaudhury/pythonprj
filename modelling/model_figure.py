import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot()
ax.set_title('Sample mpg graph')
ax.set_xlabel('Model per year')
ax.set_ylabel('Mpg')

df = pd.read_csv('mpg.csv')
df2 = df[['mpg', 'horsepower']]

df2.sort_values('mpg', ascending=False, inplace=True)
print(df2)

ax = plt.bar(x=df2['mpg'], height=df2['horsepower'])
plt.show()
