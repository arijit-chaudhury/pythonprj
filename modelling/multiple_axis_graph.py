import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("mpg.csv")
fig = plt.figure(figsize=(20, 10))

axes1 = fig.add_axes([0, 0, 1, 1])
axes2 = axes1.twinx()

axes1.plot('mpg', 'weight', data=df, color='#CE7BB0')
axes2.plot('mpg', 'horsepower', data=df, color='#6867AC')

plt.legend()

plt.show()
