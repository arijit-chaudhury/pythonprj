import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
df = pd.read_csv('mpg.csv')
# print(df)
df.boxplot(ax=ax)
ax.set_xticks(range(10))
ax.set_xticklabels(range(10))
#plt.show()
# first count number of rows and columns
# find number of columns from 2nd element of the array
n_box_plots = df.select_dtypes(include='number').shape[1]
print(n_box_plots)

# get box plot from 'cylinders' & 'model_year'
ax = df[['cylinders','model_year']].plot.box()
all_labels = ax.get_yticks()
smallest_label = all_labels[1]
largest_label = max(all_labels)
print(all_labels,smallest_label,largest_label)

# plot hist diagram
df.plot.hist()
#plt.show()
ax = df[['acceleration']].plot.hist()
#plt.show()
xlabels = ax.patches
for patch in xlabels:
    print(patch.get_height())

approx_peak_height = max(patch.get_height() for patch in ax.patches)
print(approx_peak_height)

# Scatter graph
ax = df[['acceleration','mpg']].plot.scatter(x = 'acceleration', y = 'mpg')
ylabels = ax.get_yticks()
largest_mpg_label = ylabels[-2]
