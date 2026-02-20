import pandas as pd
df = pd.read_csv("../Pandas_tips_csv/tips.csv")
print(df.isnull().sum())
df_clean = df.dropna()
print(df_clean.isnull().sum())
df_filled = df.fillna(df.mean(numeric_only=True))
print(df_filled.isnull().sum())
print(df_filled)
