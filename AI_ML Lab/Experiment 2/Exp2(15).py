import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("../Pandas_tips_csv/tips.csv")
avg_tip_by_day = df.groupby("day")["tip"].mean()
plt.scatter(df["total_bill"],df["tip"])
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.title("Average Tip by Day")
plt.show()
