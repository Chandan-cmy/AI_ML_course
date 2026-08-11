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


# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv("titanic_cleaned.csv")

# avg_fare = df.groupby("Pclass")["Fare"].mean()
# plt.figure(figsize=(7,5))
# bars = plt.bar(avg_fare.index.astype(str), avg_fare.values)
# for bar in bars:
#     plt.text(bar.get_x()+bar.get_width()/2,
#     bar.get_height(),
#     f"{bar.get_height():.2f}",ha="center")
# plt.title("Average Fare by Passenger Class")
# plt.xlabel("Passenger Class")
# plt.ylabel("Average Fare")
# plt.show()

# survival = (df.groupby("Embarked")["Survived"].mean()*100).sort_values(ascending=False)
# plt.figure(figsize=(7,5))
# bars = plt.barh(survival.index, survival.values)
# for bar in bars:
#     plt.text(bar.get_width()+1,
#     bar.get_y()+bar.get_height()/2,
#     f"{bar.get_width():.1f}%",va="center")
# plt.title("Survival Rate by Embarkation Port")
# plt.xlabel("Survival Rate (%)")
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv("titanic_cleaned.csv")
# fig, ax = plt.subplots(1,2, figsize=(12,5))

# ax[0].hist(df["Age"].dropna(), bins=20)
# ax[0].axvline(df["Age"].mean(), color="red", label="Mean")
# ax[0].axvline(df["Age"].median(), color="orange", label="Median")
# ax[0].legend()

# ax[1].hist(df["Fare"], bins=20)
# ax[1].axvline(df["Fare"].mean(), color="red", label="Mean")
# ax[1].axvline(df["Fare"].median(), color="orange", label="Median")
# ax[1].legend()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np


# df = pd.read_csv("titanic_cleaned.csv")

# fig, axes  = plt.subplots(2,2, figsize=(12,10))
# sns.boxplot(
#     data=df,
#     x="Pclass",
#     y="Age",
#     ax=axes[0, 0]
# )
# axes[0, 0].set_title("Age Distribution by Passenger Class")

# sns.violinplot(
#     data=df,
#     x="Sex",
#     y="Fare",
#     ax=axes[0, 1]
# )
# axes[0, 1].set_title("Fare Distribution by Sex")

# sns.countplot(
#     data=df,
#     x="Pclass",
#     hue="Survived",
#     ax=axes[1, 0]
# )
# axes[1, 0].set_title("Passenger Class by Survival")

# numeric_df = df.select_dtypes(include="number")
# corr_matrix = numeric_df.corr()
# sns.heatmap(
#     corr_matrix,
#     annot=True,
#     fmt=".2f",
#     cmap="coolwarm",
#     ax=axes[1, 1]
# )
# axes[1, 1].set_title("Correlation Matrix")

# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv("titanic_cleaned.csv")
sr = df.groupby("Pclass")["Survived"].mean() * 100


plt.figure(figsize=(8,6))

bars = plt.bar(
    sr.index.astype(str),
    sr.values,
    color=["green", "red", "blue"]
)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 1,
        f"{height:.1f}%",
        ha="center",
        fontsize=11
    )

plt.title("First-Class Passengers Had the Highest Survival Rate",fontsize=15,fontweight="bold")

plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")

highest = sr.max()
highest_class = sr.idxmax()

plt.annotate(
    "Highest survival rate",
    xy=(str(highest_class), highest),
    xytext=(1.6, highest + 15),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
    fontsize=11
)

plt.tight_layout()

# plt.savefig("titanic_story_chart.png", dpi=150)

plt.show()