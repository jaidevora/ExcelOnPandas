# This is a sample Python script for Excel Processing.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("SalesRecords100000.xlsx", sheet_name=0, header=0, index_col=False, keep_default_na=True, usecols="I:N")

# df = pd.read_excel()
print("Means")
print(df.mean())
print("Standard Deviations")
print(df.std())
df['Percentile Rank on Units Sold'] = df.UnitsSold.rank(pct = True)
df.to_excel("output.xlsx")

plt.scatter(x=df.UnitsSold, y=df.TotalProfit)
plt.show()
