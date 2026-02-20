import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')

counts = df.groupby(['day', 'smoker']).size().unstack(fill_value=0)

counts.plot(kind='bar', stacked=True)
plt.xlabel('Day')
plt.ylabel('Count')
plt.title('Smoker vs Non-Smoker Counts by Day')
plt.show()
