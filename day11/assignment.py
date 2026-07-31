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




import pandas as pd
df=pd.read_csv("titanic.csv")

print(df.isnull().sum())
missing_value=(df.isnull().sum()/len(df))*100

print(missing_value.sort_values(ascending=False))

