import pandas as pd

df = pd.read_csv('tips.csv')

df['tip_percent'] = (df['tip'] / df['total_bill']) * 100

df.to_csv('tips_updated.csv', index=False)

print(df.head())
