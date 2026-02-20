import pandas as pd
df=pd.read_csv("../Pandas_tips_csv/tips.csv")
print("Shape(rows, cols):", df.shape)
print("\nColumn:",df.columns.tolist())
print("\nData type:", df.dtypes)
