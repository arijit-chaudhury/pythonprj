import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('mpg.csv')
print(df.head())
print(df.info())

sns.pairplot(df)
plt.show()