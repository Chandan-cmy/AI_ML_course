# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(42)

# days = range(1, 31)
# daily_change = np.random.randn(30)*10
# starting_price = 1000
# stock_prices = starting_price + np.cumsum(daily_change)

# plt.plot(days, stock_prices, color="#2E86C1", linewidth=2.5, marker="o", markersize=6)
# plt.title("Stock Price Simulation — 30 Days", fontsize=16, fontweight="bold", pad=15)
# plt.xlabel("Day")
# plt.ylabel("Stock Price")
# plt.show()


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("titanic_cleaned.csv")
class_counts = df["Pclass"].value_counts().sort_index()
avg_fare_by_class = df.groupby("Pclass")["Fare"].mean().sort_index()