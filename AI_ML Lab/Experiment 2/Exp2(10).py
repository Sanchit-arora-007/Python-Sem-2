import pandas as pd
df=pd.read_csv("../Pandas_tips_csv/tips.csv")
print(df.isnull().sum())
print(df[["total_bill","tip","size"]].describe())
