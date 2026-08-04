# Line Chart


# import matplotlib.pyplot as plt
# import numpy as np
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# sales = [45000, 52000, 48000, 61000, 58000, 70000]
# plt.figure(figsize=(10, 6)) 
# plt.plot(months, sales, color="steelblue", linewidth=2,marker="o", markersize=8, label="Monthly Sales")
# plt.title("Monthly Sales Performance 2024", fontsize=16, fontweight="bold",
# pad=15)
# plt.xlabel("Month", fontsize=13)
# plt.ylabel("Sales (Rs.)", fontsize=13)
# plt.grid(True, linestyle="--", alpha=0.7)
# plt.legend(fontsize=11)
# # plt.savefig("sales_chart.png", dpi=150, bbox_inches="tight")
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# months = range(1, 13)
# product_a = [45, 52, 48, 61, 58, 70, 65, 72, 68, 80, 85, 92]
# product_b = [30, 35, 40, 38, 45, 50, 48, 55, 60, 58, 62, 70]
# product_c = [20, 22, 25, 30, 28, 32, 35, 40, 38, 45, 50, 55]
# month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# plt.figure(figsize=(12, 6))
# plt.plot(month_names, product_a, color="#2196F3", lw=2.5,
#  marker="o", ms=7, label="Product A")
# plt.plot(month_names, product_b, color="#4CAF50", lw=2.5,
#  marker="s", ms=7, label="Product B")
# plt.plot(month_names, product_c, color="#FF9800", lw=2.5,
#  marker="^", ms=7, label="Product C")
# plt.title("Monthly Revenue by Product (2024)", fontsize=16,
# fontweight="bold")
# plt.xlabel("Month", fontsize=13)
# plt.ylabel("Revenue (Rs. thousands)", fontsize=13)
# plt.legend(fontsize=11)
# plt.grid(True, linestyle="--", alpha=0.6)
# plt.tight_layout()
# # plt.savefig("line_chart.png", dpi=150, bbox_inches="tight")
# plt.show()


# bar chart

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv("titanic_cleaned.csv")

# class_counts = df["Pclass"].value_counts().sort_index()
# print(class_counts)
# plt.figure(figsize=(8, 6))
# bars = plt.bar(
#     x = ["First", "Second", "Third"],
#     height = class_counts.values,
#     color = ["#1F5C8B", "#2E86C1", "#85C1E9"],
#     edgecolor = "white",
#     linewidth = 1.5,
#     width = 0.6
#     )
# for bar in bars:
#     height = bar.get_height()
#     plt.text(
#         x = bar.get_x() + bar.get_width() / 2,
#         y = height + 5,
#         s = str(int(height)),
#         ha = "center",
#         va = "bottom",
#         fontsize = 12,
#         fontweight = "bold"
#         )
# plt.title("Passengers by Class — Titanic", fontsize=16, fontweight="bold")
# plt.xlabel("Passenger Class", fontsize=13)
# plt.ylabel("Number of Passengers", fontsize=13)
# plt.ylim(0, 560)
# plt.grid(axis="y", linestyle="--", alpha=0.6)
# plt.tight_layout()
# # plt.savefig("bar_chart.png", dpi=150, bbox_inches="tight")
# plt.show()

# Example

# import pandas as pd
# import matplotlib.pyplot as plt

# Student= ["A", "B", "C", "D"]
# Marks= [85, 90, 78, 92]
# bars = plt.bar(Student, Marks, color="#FF5733", edgecolor="black")
# plt.title("Student Marks", fontsize=16, fontweight="bold")
# plt.xlabel("Student", fontsize=13)
# plt.ylabel("Marks", fontsize=13)

# plt.show()

# import matplotlib.pyplot as plt
# cities = ["Mumbai", "Bengaluru", "Delhi", "Hyderabad", "Chennai","Pune"]
# startups = [2800, 2100, 1900, 1200, 900, 750]

# sorted_pairs = sorted(zip(startups, cities))
# startups_sorted, cities_sorted = zip(*sorted_pairs)
# plt.figure(figsize=(13, 7))
# bars = plt.barh(cities_sorted, startups_sorted, color="#2E86C1",
#  edgecolor="white", height=0.6)
# for bar in bars:
#     width = bar.get_width()
#     plt.text(width + 30, bar.get_y() + bar.get_height()/2,f"{int(width):,}", va="center", fontsize=11)
# plt.title("Tech Startups by City — India 2024", fontsize=15,
# fontweight="bold")
# plt.xlabel("Number of Startups", fontsize=12)
# plt.grid(axis="x", linestyle="--", alpha=0.6)
# plt.tight_layout()
# # plt.savefig("horizontal_bar.png", dpi=150, bbox_inches="tight")
# plt.show()

# Histogram

# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# df = pd.read_csv("titanic_cleaned.csv")
# fig, axes = plt.subplots(1, 2, figsize=(14, 7))



# axes[0].hist(df["Age"].dropna(), bins=30, color="#2196F3",ec="white", linewidth=0.8)
# axes[0].axvline(df["Age"].mean(), color="red", ls="--",lw=2, label=f"Mean: {df['Age'].mean():.1f}")
# axes[0].axvline(df["Age"].median(), color="orange", ls="--",lw=2, label=f"Median: {df['Age'].median():.1f}")
# axes[0].set_title("Age Distribution", fontsize=14, fontweight="bold")
# axes[0].set_xlabel("Age", fontsize=12)
# axes[0].set_ylabel("Count", fontsize=12)
# axes[0].legend(fontsize=11)
# axes[0].grid(axis="y", linestyle="--", alpha=0.6)


# axes[1].hist(df["Fare"], bins=40, color="#4CAF50",
#  edgecolor="white", linewidth=0.8)
# axes[1].set_title("Fare Distribution", fontsize=14, fontweight="bold")
# axes[1].set_xlabel("Fare (GBP)", fontsize=12)
# axes[1].set_ylabel("Count", fontsize=12)
# axes[1].grid(axis="y", linestyle="--", alpha=0.6)
# plt.suptitle("Titanic: Numeric Variable Distributions",fontsize=16, fontweight="bold", y=1.02)
# plt.tight_layout()
# # plt.savefig("histograms.png", dpi=150, bbox_inches="tight")
# plt.show()

# Pie Chart

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv("titanic_cleaned.csv")
# # Embarked port distribution
# port_counts = df["Embarked"].value_counts()
# port_labels = {"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"}
# labels = [port_labels.get(p, p) for p in port_counts.index]
# plt.figure(figsize=(8, 8))
# wedges, texts, autotexts = plt.pie(
#     port_counts.values,
#     labels = labels,
#     autopct = "%1.1f%%", # Show percentage on each slice
#     startangle= 90, # Start from top
#     colors = ["#2196F3", "#4CAF50", "#FF9800"],
#     explode = [0.05, 0.05, 0.05],
#     shadow = True
#     )
# for autotext in autotexts:
#     autotext.set_fontsize(13)
#     autotext.set_fontweight("bold")
# plt.title("Port of Embarkation — Titanic Passengers",fontsize=15, fontweight="bold", pad=20)
# plt.tight_layout()
# # plt.savefig("pie_chart.png", dpi=150, bbox_inches="tight")
# plt.show()

