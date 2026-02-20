import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')

tips_by_day = df.groupby('day')['tip'].sum()

tips_by_day.plot(kind='bar')
plt.xlabel('Day')
plt.ylabel('Total Tips')
plt.title('Total Tips by Day')
plt.show()
