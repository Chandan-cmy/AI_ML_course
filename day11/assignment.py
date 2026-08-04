import pandas as pd


# temps = pd.Series([22.0, None, None, 25.0, None, 27.0])
# # print("Original:")
# # print(temps.tolist())

# # print("\nForward fill (ffill):")
# # print(temps.ffill().tolist())

# print("\nBackward fill (bfill):")
# print(temps.bfill().tolist())


# data = {
#  "name" : ["Rahul", "Priya", "Arjun", "Rahul", "Sneha", "Priya"],
#  "age" : [22, 21, 23, 22, 20, 21],
#  "score" : [85, 92, 78, 85, 95, 92]
# }

# df = pd.DataFrame(data)
# print("Original:")
# print(df)


# print(f"\nDuplicate rows: {df.duplicated().sum()}")

# print("\nDuplicate rows:")
# print(df[df.duplicated(keep=False)])

# df_clean = df.drop_duplicates()
# print(f"\nAfter removing duplicates: {df_clean.shape}")
# print(df_clean)

# df_name_unique = df.drop_duplicates(subset=["name"])
# print(f"\nUnique names only: {df_name_unique.shape}")


# messy = pd.DataFrame({
#  "age" : ["22", "21", "23", "20"], # Numbers as strings
#  "salary" : ["50,000", "65,000", "48,000", "72,000"], # Commas!
#  "join_date" : ["2022-01-15", "2021-06-01", "2023-03-10", "2020-11-20"],
#  "gender" : ["Male", "Female", "Male", "Female"]
# })

# print("Before fixing:")
# print(messy.dtypes)

# messy["age"] = messy["age"].astype(int)

# messy["salary"] = messy["salary"].str.replace(",", "").astype(int)

# messy["join_date"] = pd.to_datetime(messy["join_date"])

# messy["gender"] = messy["gender"].astype("category")

# print("\nAfter fixing:")
# print(messy.dtypes)
# print(messy)

# df = pd.DataFrame({
#  "city" : [" Mumbai ", "DELHI", "bengaluru", "Mumbai", " Delhi"],
#  "product" : ["Laptop Pro", "laptop pro", "LAPTOP PRO", "Laptop pro",
# "laptop Pro"]
# })

# print("Before cleaning:")
# print(df["city"].value_counts())

# df["city"] = df["city"].str.strip()
# print(df["city"])

# print("\nAfter strip + title:")
# print(df["city"].value_counts())

# df["product"] = df["product"].str.lower().str.strip()

# print("\nProduct after lower + strip:")
# print(df["product"].value_counts())

# import pandas as pd

# batch_jan = pd.DataFrame({
#  "name" : ["Rahul", "Priya"],
#  "score" : [85, 92]
# })
# batch_feb = pd.DataFrame({
#  "name" : ["Arjun", "Sneha", "Mohammed"],
#  "score" : [78, 95, 88]
# })
# # Stack vertically (add rows) — axis=0
# all_students = pd.concat([batch_jan, batch_feb], axis=0, ignore_index=True)
# print("Combined all students:")
# print(all_students)

import pandas as pd
df = pd.read_csv("titanic.csv")
# Average fare paid by each passenger class
# avg_fare = df.groupby("Pclass")["Fare"].mean()
# print("Average Fare by Class:")
# print(avg_fare.round(2))

# survival_by_gender = df.groupby("Sex")["Survived"].mean() * 100
# print("\nSurvival Rate by Gender (%):")
# print(survival_by_gender.round(1))

# count_by_class = df.groupby("Pclass")["PassengerId"].count()
# print("\nPassengers per Class:")
# print(count_by_class)


# fare_stats = df.groupby("Pclass")["Fare"].agg(["mean", "median", "min",
# "max", "count"])
# print("Fare Statistics by Class:")
# print(fare_stats.round(2))

# summary = df.groupby("Pclass").agg(
#  total_passengers = ("PassengerId", "count"),
#  survivors = ("Survived", "sum"),
#  survival_rate = ("Survived", "mean"),
#  avg_age = ("Age", "mean"),
#  avg_fare = ("Fare", "mean")
# )
# summary["survival_rate"] = (summary["survival_rate"] * 100).round(1)
# summary["avg_age"] = summary["avg_age"].round(1)
# summary["avg_fare"] = summary["avg_fare"].round(2)
# print("\nFull Summary by Passenger Class:")
# print(summary)
#---------------------------------------------------------------------

# cross_tab = df.groupby(["Pclass", "Sex"])["Survived"].agg(
#  count = "count",
#  survived = "sum",
#  rate = "mean"
# ).round(2)
# print(cross_tab)

# flat = cross_tab.reset_index()
# print("\nFlat version:")
# print(flat)


# pivot = df.pivot_table(
#  values = "Survived", # What to calculate
#  index = "Pclass", # Goes on the rows
#  columns = "Sex", # Goes on the columns
#  aggfunc = "mean" # How to aggregate
# ).round(3)

# print("Survival rate by Class and Gender:")
# print(pivot)

# pivot_count = df.pivot_table(
#  values = "PassengerId",
#  index = "Pclass",
#  columns = "Sex",
#  aggfunc = "count"
# )
# print("\nPassenger counts:")
# print(pivot_count)


# import pandas as pd
# import numpy as np

# df = pd.read_csv("titanic.csv")
# print(f"Step 1 — Loaded: {df.shape}")

# print("\nStep 2 — Missing values:")
# print((df.isnull().sum() / len(df) * 100).round(1))

# df = df.drop(columns=["Cabin", "Name", "Ticket", "PassengerId"])
# print(f"\nStep 3 — After dropping cols: {df.shape}")

# df["Age"] = df["Age"].fillna(df["Age"].median())

# df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# df = df.drop_duplicates()
# print(f"Step 6 — After dedup: {df.shape}")

# df["family_size"] = df["SibSp"] + df["Parch"] + 1
# df["is_alone"] = (df["family_size"] == 1).astype(int)
# df["age_group"] = pd.cut(df["Age"],
#                          bins=[0, 12, 18, 60, 100],
#                          labels=["Child", "Teen", "Adult", "Senior"])


# print("\nStep 8 — Missing after cleaning:")
# print(df.isnull().sum())
# print(f"\nFinal shape: {df.shape}")
# print("\nSample of cleaned data:")
# print(df.head())

# df.to_csv("titanic_cleaned.csv", index=False)
# print("\nCleaned dataset saved to titanic_cleaned.csv")


#--------------------------------------------------------------------------------------------------

# Exercise 1 — Missing Value Report (Beginner)

# import pandas as pd
# df = pd.read_csv("titanic.csv")
# print(df.isnull().sum())
# print(((df.isnull().sum()/len(df))*100).sort_values(ascending=False))




# import pandas as pd

# df = pd.read_csv("titanic.csv")

# missing_count = df.isnull().sum()

# missing_percentage = (missing_count / len(df)) * 100

# report = pd.DataFrame({
#     "Column": missing_count.index,
#     "Missing Count": missing_count.values,
#     "Missing Percentage": missing_percentage.values
# })

# report = report.sort_values(by="Missing Percentage", ascending=False)

# decision = []

# for column in report["Column"]:
#     if report.loc[report["Column"] == column, "Missing Count"].values[0] == 0:
#         decision.append("Keep as is")
#     elif column == "Age":
#         decision.append("Fill with Median")
#     elif column == "Embarked":
#         decision.append("Fill with Mode")
#     elif column == "Cabin":
#         decision.append("Drop")
#     else:
#         decision.append("Fill with Mean")

# report["Decision"] = decision

# print(report.to_string(index=False))



# Exercise 2 — Full Cleaning Pipeline (Beginner-Intermediate)

# import pandas as pd
# import numpy as np

# df=pd.read_csv("titanic.csv")
# print(df.isnull().sum())
# print((df.isnull().sum() / len(df) * 100).round(1))

# df = df.drop(columns=["Cabin", "Name", "Ticket", "PassengerId"])
# print(f"\n After dropping cols: {df.shape}")

# df["Age"] = df["Age"].fillna(df["Age"].median())

# df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# print(f"After removing duplicates: {df.shape}")

# df.to_csv("titanic_cleaned.csv", index=False)
# print("\nCleaned dataset saved to titanic_cleaned.csv")
# print(df.isnull().sum())

# Exercise 3 — String Cleaning (Intermediate)

# df = pd.DataFrame({"City": [" Bangalore","bangalore ","BANGALORE"," Mysore","mysore ","MYSORE"," Chennai ","chennai","CHENNAI "," bangalore"]})
# print("before cleaning:")
# print(df["City"].value_counts())

# df["city"] = df["City"].str.strip()
# df["city"] = df["city"].str.title()
# df["city"] = df["city"].str.lower()
# print("after cleaning:")
# print(df["city"].value_counts())

# Exercise 4 — GroupBy Analysis (Intermediate)

# import pandas as pd
# df = pd.read_csv("titanic_cleaned.csv")

# avg_fare = df.groupby("Embarked")["Fare"].mean()
# print(f"Average Fare by Embarked Port:{avg_fare.round(2)}")

# survival_rate = df.groupby("Pclass")["Survived"].mean() * 100
# print(f" Survival Rate by Passenger Class:{survival_rate.round(1)}")

# avg_age = df.groupby("Survived")["Age"].mean()
# print(f"Average age of survivors vs non-survivors: {avg_age.round(1)}")

# summary = df.groupby(["Pclass", "Sex"]).agg(
#     Total_Passengers=("Survived", "count"),
#     Survivors=("Survived", "sum"))

# print(f" Total passengers and survivors grouped by both class and gender:{summary}")

# Exercise 5 — Merge Practice (Intermediate)

# p = pd.DataFrame({
#      "product_id": [1, 2, 3, 4, 5, 6],
#      "product_name": ["Laptop","Mouse pad","Keyboard","Monitor","Printer","Speaker"],
#       "category": ["Electronics","Accessories","Accessories","Electronics","Electronics","Accessories"]
#     })

# s = pd.DataFrame({
#     "product_id": [1, 2, 3, 4, 5],
#     "units_sold": [50, 150, 80, 40, 25],
#     "revenue": [25000, 75000, 16000, 60000, 30000]
# })

# inner_merge = pd.merge(p, s, on="product_id", how="inner")
# print("Inner Merge:", inner_merge)

# left_merge = pd.merge(p, s, on="product_id", how="left")
# print("\nLeft Merge:", left_merge)