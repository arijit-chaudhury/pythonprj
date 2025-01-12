import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('mpg.csv')
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
ax1.bar(x=df['name'], height=df['horsepower'])
ax2.barh(y=df['model_year'], width=df['origin'])
plt.show()