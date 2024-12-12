import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mpg.csv')
df['horsepower_per_cylinder'] = df['horsepower']/df['cylinders']
print(df.head())
ax = df.plot.scatter(x='horsepower_per_cylinder',y='acceleration')
acc_decreases = True
print(ax.get_xticks())
print(ax.get_yticks())
plt.show()

