import pandas as pd
df = pd.read_csv('../customers-100.csv')
print(df.head())
print(df["First Name"].describe())
print(df)
