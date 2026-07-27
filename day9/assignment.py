# import numpy as np 
# import pandas as pd

# marks = pd.Series([85, 92, 78, 95, 88])
# print(marks)
# print("")

# marks_named = pd.Series([85, 92, 78, 95, 88],index=["Rahul", "Priya", "Arjun", "Sneha", "Mohammed"])

# print(marks_named)
# print("")

# attendance = pd.Series({
#  "Rahul" : 92,
#  "Priya" : 85,
#  "Arjun" : 78,
#  "Sneha" : 96
# })
# print(attendance)


# print(marks_named["Rahul"]) # 85
# print(marks_named["Priya"]) 

# print(marks_named.iloc[0]) # 85 (first item)
# print(marks_named.iloc[-1])

# print(marks_named["Rahul":"Arjun"]) # Rahul to Arjun inclusive
# # Boolean filtering — same as NumPy
# print(marks_named[marks_named > 85]) 

# marks = pd.Series([85, 92, 78, 95, 88, 70, 99, 63])
# # Quick statistics
# print(marks.mean()) # 83.75
# print(marks.median()) # 86.5
# print(marks.max()) # 99
# print(marks.min()) # 63
# print(marks.std()) # 11.67
# print(marks.count()) # 8 (number of non-null values)
# # .describe() — all stats in one shot
# print(marks.describe())
# # Value counts — very useful for categorical data
# grades = pd.Series(["A", "B", "A", "C", "A", "B", "F", "A"])
# print(grades.value_counts())


# import pandas as pd
# # Method 1: From a dictionary (most common)
# data = {
#  "name" : ["Rahul", "Priya", "Arjun", "Sneha", "Mohammed"],
#  "age" : [22, 21, 23, 20, 24],
#  "city" : ["Bengaluru", "Mumbai", "Delhi", "Chennai","Hyderabad"],
#  "marks" : [85, 92, 78, 95, 88],
#  "passed" : [True, True, True, True, True]
# }
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# df = pd.read_csv("titanic.csv")
# print(df.head())

# import pandas as pd

# df_excel=pd.read_excel("data.xlsx", sheet_name="Sheet1")

# df_json = pd.read_json("data.json")

# url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
# df_url = pd.read_csv(url)
# print(f"Loaded {len(df_url)} rows directly from the internet")

# df.to_csv("my_results.csv", index=False) # index=False — don't save row
# numbers

# import pandas as pd 

# df=pd.read_csv("titanic.csv")

# # print(df.shape)

# # print(df.head())
# # print(df.head(10))

# # print(df.tail())

# # print(df.info())

# print(df.describe())

# print(df.co)

# import pandas as pd 

# df=pd.read_csv("titanic.csv")

# ages=df["Age"]
# print(type(ages))

# print(ages.head())

# subset = df[["Name", "Age", "Survived"]]
# print(subset.head())

# no_id = df.drop(columns=["PassengerId", "Ticket", "Cabin"])
# print(no_id.shape) 


# import pandas as pd
# df = pd.read_csv("titanic.csv")

# print(df.loc[0])
# print("") 

# print(df.loc[0:4]) 

# print(df.loc[0, "Name"]) 
# print(df.loc[0, ["Name", "Age", "Survived"]])
# print(df.loc[0:3, ["Name", "Survived", "Fare"]])

# import pandas as pd
# df = pd.read_csv("titanic.csv")

#print(df.iloc[0]) 
# print("")
#print(df.iloc[-1]) 

#print(df.iloc[0:5])

# print(df.iloc[0:3, 0:4])

# print(df.iloc[::2].head())

# print(df.iloc[-10:])

# import pandas as pd
# df = pd.read_csv("titanic.csv")

# survivors = df[df["Survived"] == 1]
# print(f"Survivors: {len(survivors)}")

# women = df[df["Sex"] == "female"]
# print(f"Women: {len(women)}")

# older = df[df["Age"] > 40]
# print(f"Over 40: {len(older)}")

# women_survived = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
# print(f"Women who survived: {len(women_survived)}")

# premium = df[(df["Pclass"] == 1) | (df["Fare"] > 100)]
# print(f"Premium passengers: {len(premium)}")

# not_third = df[df["Pclass"] != 3]
# print(f"Not third class: {len(not_third)}")


#Exercise 1

# import pandas as pd
# df = pd.read_csv("titanic.csv")

# print("1. Shape:")
# print(df.shape)

# print("2. Column Names:")
# print(df.columns)

# print("3. First 8 Rows:")
# print(df.head(8))

# print("4. Last 5 Rows:")
# print(df.tail())

# print("5. Data Types:")
# print(df.dtypes)

# print("6. Missing Values Percentage:")
# missing = (df.isnull().sum() / len(df)) * 100
# print(missing)

#Exercise 2


# import pandas as pd
# df = pd.read_csv("titanic.csv")

# print("Selected Columns")
# print(df[["Name", "Age", "Sex", "Survived"]])

# print("\n10th to 20th Rows")
# print(df.iloc[10:21])

# print("\nFare of Passenger at Index 100")
# print(df.loc[100, "Fare"])

# print("\nUnique Embarked Values")
# print(df["Embarked"].unique())

# print("\nPclass Value Counts")
# print(df["Pclass"].value_counts())

#Exercise 3

# import pandas as pd
# df = pd.read_csv("titanic.csv")

# survived = df[df["Survived"] == 1]
# print("Survived:", len(survived))

# female_first = df[(df["Sex"] == "female") & (df["Pclass"] == 1)]
# print("Female First Class:", len(female_first))

# children = df[df["Age"] < 10]
# print("Under 10 Years:", len(children))

# expensive = df[df["Fare"] * 90 > 5000]
# print("Fare > 5000 INR:", len(expensive))

# male_old = df[
#     (df["Sex"] == "male") &
#     (df["Age"] > 50) &
#     (df["Survived"] == 0)
# ]
# print("Male >50 and Not Survived:", len(male_old))

# #Exercise 4

# import pandas as pd
# df = pd.read_csv("titanic.csv")

# df["fare_inr"] = df["Fare"] * 90

# df["is_child"] = df["Age"] < 18

# df["family_size"] = df["SibSp"] + df["Parch"] + 1

# print(df[["Name", "fare_inr", "is_child", "family_size"]].head(10))


#Exercise 5

# import pandas as pd
# df = pd.read_csv("titanic.csv")

# print("Shape:")
# print(df.shape)

# print("\nInfo:")
# print(df.info())

# print("\nDescribe:")
# print(df.describe())

# print("\nMissing Values:")
# print(df.isnull().sum())