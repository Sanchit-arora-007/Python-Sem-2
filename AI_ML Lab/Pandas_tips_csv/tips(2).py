import pandas as pd

df = pd.read_csv('tips.csv')

print("Features (Columns):")
print(df.columns.tolist())

print("\nNumber of samples (rows):")
print(df.shape[0])
