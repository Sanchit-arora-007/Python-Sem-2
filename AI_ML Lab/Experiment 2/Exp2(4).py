import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../Pandas_tips_csv/tips.csv')
df.plot(x='total_bill', y='tip')
plt.show()
