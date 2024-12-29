import pandas as pd

technologies = ({
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", "Hadoop", "Spark"],
    'Fee': [22000, 25000, 23000, 24000, 26000, 25000, 25000],
    'Duration': ['30days', '50days', '55days', '40days', '60days', '35days', '55days'],
    'Discount': [1000, 2300, 1000, 1200, 2500, 1300, 1400],
    'InsertedDates': ["2021-11-14", "2021-11-15", "2021-11-16", "2021-11-17", "2021-11-18", "2021-11-19", "2021-11-20"]
})
df = pd.DataFrame(technologies)
print(df)

start_date = '2021-11-15'
end_date = '2021-11-19'

# Select DataFrame rows between two dates
mask = (df['InsertedDates'] > start_date) & (df['InsertedDates'] <= end_date)
df2 = df.loc[mask]
print(df2)

after_start_date = df["InsertedDates"] >= start_date
before_end_date = df["InsertedDates"] <= end_date
between_two_dates = after_start_date & before_end_date

# Using pandas.DataFrame.loc
# To filter rows by dates
df2 = df.loc[between_two_dates]
print(df2)

# Using pandas.DataFrame.query()
# To select DataFrame Rows
start_date = '2021-11-15'
end_date = '2021-11-18'
df2 = df.query('InsertedDates >= @start_date and InsertedDates <= @end_date')
print(df2)

# Select rows between two dates
# Using DataFrame.query()
start_date = '2021-11-15'
end_date = '2021-11-18'
df2 = df.query('InsertedDates > @start_date and InsertedDates < @end_date')
print(df2)

# Pandas.Series.between() function
# Using two dates
df2 = df.loc[df["InsertedDates"].between("2021-11-16", "2021-11-18")]
print(df2)

# Select DataFrame rows between two dates
# Using DataFrame.isin()
df2 = df[df["InsertedDates"].isin(pd.date_range("2021-11-15", "2021-11-17"))]
print(df2)
