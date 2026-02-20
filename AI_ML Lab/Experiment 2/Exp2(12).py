import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("../Pandas_tips_csv/tips.csv")
df["tip_percentage"] = (df["tip"] / df["total_bill"]) *100
plt.figure()
plt.boxplot(df["tip_percentage"])
plt.title("Tip Percentage Distribution")
plt.xlabel("Tip Percentage")
plt.ylabel("Frequency")
plt.show()
