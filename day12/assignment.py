# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# df = pd.read_csv("titanic_cleaned.csv")
# plt.figure(figsize=(10, 6))
# # Scatter: Age vs Fare, coloured by survival
# survivors = df[df["Survived"] == 1]
# non_survivors = df[df["Survived"] == 0]
# plt.scatter(non_survivors["Age"], non_survivors["Fare"],
#  color="#E74C3C", alpha=0.5, s=40,
#  label="Did Not Survive", edgecolors="white", lw=0.5)
# plt.scatter(survivors["Age"], survivors["Fare"],
#  color="#2ECC71", alpha=0.5, s=40,
#  label="Survived", edgecolors="white", lw=0.5)
# plt.title("Age vs Fare — Coloured by Survival", fontsize=15,
# fontweight="bold")
# plt.xlabel("Age", fontsize=13)
# plt.ylabel("Fare (GBP)", fontsize=13)
# plt.legend(fontsize=11)
# plt.grid(True, linestyle="--", alpha=0.5)
# plt.tight_layout()
# # plt.savefig("scatter_plot.png", dpi=150, bbox_inches="tight")
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv("titanic_cleaned.csv")
# # Embarked port distribution
# port_counts = df["Embarked"].value_counts()
# port_labels = {"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"}
# labels = [port_labels.get(p, p) for p in port_counts.index]

# plt.figure(figsize=(8, 8))
# wedges, texts, autotexts = plt.pie(
#  port_counts.values,
#  labels = labels,
#  autopct = "%1.1f%%", # Show percentage on each slice
#  startangle= 90, # Start from top
#  colors = ["#2196F3", "#4CAF50", "#FF9800"],
#  explode = [0.05, 0.05, 0.05], # Slight separation between slices
#  shadow = True
# )
# # Style the percentage text
# for autotext in autotexts:
#     autotext.set_fontsize(13)
#     autotext.set_fontweight("bold")
# plt.title("Port of Embarkation — Titanic Passengers",fontsize=15, fontweight="bold", pad=20)

# plt.tight_layout()
# # plt.savefig("pie_chart.png", dpi=150, bbox_inches="tight")
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# sns.set_theme(style="whitegrid")
# df = pd.read_csv("titanic_cleaned.csv")
# plt.figure(figsize=(10, 6))
# # Box plot: Fare distribution by passenger class
# sns.boxplot(
#     data = df,
#     x = "Pclass",
#     y = "Fare",
#     palette = "Blues",
#     order = [1, 2, 3]
# )
# plt.title("Fare Distribution by Passenger Class",fontsize=15, fontweight="bold")
# plt.xlabel("Passenger Class", fontsize=13)
# plt.ylabel("Fare (GBP)", fontsize=13)
# plt.tight_layout()
# # plt.savefig("boxplot.png", dpi=150, bbox_inches="tight")
# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# sns.set_theme(style="whitegrid")
# df = pd.read_csv("titanic_cleaned.csv")
# plt.figure(figsize=(10, 6))
# sns.violinplot(
#     data = df,
#     x = "Pclass",
#     y = "Age",
#     palette = "muted",
#     inner = "box" # Show box plot inside the violin
# )
# plt.title("Age Distribution by Passenger Class",fontsize=15, fontweight="bold")
# plt.xlabel("Passenger Class", fontsize=13)
# plt.ylabel("Age (years)", fontsize=13)
# plt.tight_layout()
# # plt.savefig("violin_plot.png", dpi=150, bbox_inches="tight")
# plt.show()


