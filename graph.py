import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mpg.csv')
# print(df)
df.plot.box()
# first count number of rows and columns
# find number of columns from 2nd element of the array
n_box_plots = df.select_dtypes(include='number').shape[1]
print(n_box_plots)