import pandas as pd
df=pd.read_csv("../Pandas_tips_csv/tips.csv")
df["tip.percent"]=(df["tip"]/df["total_bill"])*100
print(df[["total_bill","tip","tip.percent"]].head())
