import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')

plt.hist(df['total_bill'], bins=10)
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.title('Histogram of Total Bill')
plt.show()
