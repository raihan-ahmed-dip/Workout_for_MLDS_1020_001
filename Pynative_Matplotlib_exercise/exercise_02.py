"""
Exercise 2: Get total profit of all months and show line plot with the following Style properties

Generated line plot must include following Style properties: –
- Line Style dotted and Line-color should be red
- Show legend at the lower right location.
- X label name = Month Number
- Y label name = Sold units number
- Add a circle marker.
- Line marker color as read
- Line width should be 3

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
month_number = df['month_number'].tolist()
total_profit = df['total_profit'].tolist()

plt.plot(month_number, total_profit, 'o--r', linewidth=3, markerfacecolor='black', label="Profit data of last year")
plt.legend(loc='lower right')
plt.xticks(month_number)
plt.yticks(np.arange(100000, 500001, 100000))
plt.title("Company Sales data of last year")
plt.xlabel("Month Number")
plt.ylabel("Sold Units Number")
plt.show()