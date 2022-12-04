"""
Exercise 1: Read Total profit of all months and show it using a line plot
Total profit data provided for each month. Generated line plot must include the following properties: –

X label name = Month Number
Y label name = Total profit
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("company_sales_data.csv")
month_number = df['month_number'].tolist()
total_profit = df['total_profit'].tolist()

plt.plot(month_number, total_profit)
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.title("Company profit per month")
ps = np.arange(100000, 500001, 100000).tolist()
plt.xticks(month_number)
plt.yticks(ps)
plt.show()