# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# sns.set_theme(style="white")
# df = pd.read_csv("titanic_cleaned.csv")

# numeric_df = df.select_dtypes(include="number")
# corr_matrix = numeric_df.corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(
#     corr_matrix,
#     annot = True,
#     fmt = ".2f",
#     cmap = "coolwarm",
#     center = 0, 
#     square = True, 
#     linewidths = 0.5,
#     cbar_kws = {"shrink": 0.8}
#     )
# plt.title("Correlation Matrix — Titanic Dataset",fontsize=15, fontweight="bold", pad=15)
# plt.xticks(rotation=45, ha="right", fontsize=11)
# plt.yticks(rotation=0, fontsize=11)
# plt.tight_layout()
# plt.savefig("heatmap.png", dpi=150, bbox_inches="tight")
# plt.show()



# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# sns.set_theme(style="whitegrid")
# df = pd.read_csv("titanic_cleaned.csv")
# plt.figure(figsize=(10, 6))
# # Count of survivors vs non-survivors, split by gender
# sns.countplot(
#  data = df,
#  x = "Survived",
#  hue = "Sex",
#  palette = {"male": "#2196F3", "female": "#E91E63"}
# )
# # Replace 0 and 1 with readable labels
# plt.xticks([0, 1], ["Did Not Survive", "Survived"], fontsize=12)
# plt.title("Survival Count by Gender", fontsize=15, fontweight="bold")
# plt.xlabel("", fontsize=13)
# plt.ylabel("Number of Passengers", fontsize=13)
# plt.legend(title="Gender", fontsize=11)
# plt.tight_layout()
# # plt.savefig("count_plot.png", dpi=150, bbox_inches="tight")
# plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_theme(style="whitegrid")
df = pd.read_csv("titanic_cleaned.csv")
# Select relevant numeric columns only (pair plot gets busy with too many)
cols = ["Age", "Fare", "SibSp", "Parch", "Survived"]
df_pair = df[cols].dropna()
# Create pair plot coloured by survival status
pair_plot = sns.pairplot(
 data = df_pair,
 hue = "Survived",
 palette = {0: "#E74C3C", 1: "#2ECC71"},
 diag_kind= "kde", # Smooth density curve on diagonal
 plot_kws = {"alpha": 0.5, "s": 30}
)
pair_plot.figure.suptitle("Pair Plot — Titanic Numeric Features",
 y=1.02, fontsize=14, fontweight="bold")
# plt.savefig("pair_plot.png", dpi=120, bbox_inches="tight")
plt.show()



