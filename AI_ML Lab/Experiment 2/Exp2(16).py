import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("../Pandas_tips_csv/tips.csv")
avg_tip_by_day = df.groupby("day")["tip"].mean()
counts = df.groupby(["day", "smoker"]).size().unstack()
counts.plot(kind="bar", stacked=True)
plt.xlabel("Day")
plt.ylabel("Count")
plt.title("Smoker vs Non-Smoker Counts by Day")
plt.legend(title="Smoker")
plt.show()
