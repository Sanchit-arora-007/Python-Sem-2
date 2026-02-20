import pandas as pd
df = pd.read_csv('../Pandas_tips_csv/tips.csv')
groups= df.groupby('day')
print(groups)
summary = groups['tip'].sum()
print(summary)
