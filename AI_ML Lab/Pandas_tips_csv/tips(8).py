import pandas as pd

df = pd.read_csv('tips.csv')

df['tip_by_day'] = df.groupby('day')['tip'].transform('sum')

print(df.head())

df.to_csv('tips_updated.csv', index=False)
