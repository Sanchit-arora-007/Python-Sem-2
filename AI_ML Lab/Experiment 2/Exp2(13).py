import pandas as pd
df=pd.read_csv("../Pandas_tips_csv/tips.csv")
df["tip.percent"]=(df["tip"]/df["total_bill"])*100
avg_tip_by_day=df.groupby("day")["tip"].mean().sort_values (ascending=False)
print(avg_tip_by_day)
