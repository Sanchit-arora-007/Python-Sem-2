import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')

plt.scatter(df['total_bill'], df['tip'])
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Total Bill vs Tip')
plt.show()
