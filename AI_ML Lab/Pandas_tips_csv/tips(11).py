import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')
tips_by_size = df.groupby('size')['tip'].sum().sort_index()

plt.plot(tips_by_size.index, tips_by_size.values)
plt.xlabel('Party Size')
plt.ylabel('Total Tips')
plt.title('Total Tips by Party Size')
plt.show()
