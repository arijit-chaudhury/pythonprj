import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../organizations-1000.csv")

axes1 = plt.subplot(2, 1, 1)
axes1.bar(x=df['Founded'], height=df['Number of employees'])

axes2 = plt.subplot(2, 2, 3)
df2 = df.groupby(['Country']).size().reset_index(name='count')
axes2.pie(df2['count'])


axes3 = plt.subplot(2, 2, 4)

plt.show()

