# import pandas as pd
# import numpy as np

# df=pd.read_csv("titanic.csv")

# #print(df.isnull().sum())

# missing_pct = (df.isnull().sum() / len(df)) * 100
# #print(missing_pct.round(1))

# #print(missing_pct[missing_pct>0].sort_values(ascending=False))

# print(df.isnull().any().any())

# print(df.isnull().sum().sum())


#step drop missing values
# import pandas as pd

# df=pd.read_csv("titanic.csv")

# print(f"Original shape: {df.shape}")

# df_dropped_all = df.dropna()
# # print(f"After dropna(): {df_dropped_all.shape}")

# df_age_clean = df.dropna(subset=["Age"])
# # print(f"After dropna(Age): {df_age_clean.shape}")

# df_two_clean = df.dropna(subset=["Age", "Embarked"])
# # print(f"After dropna(Age,Embarked): {df_two_clean.shape}")

# threshold = len(df) * 0.5
# df_col_clean = df.dropna(axis=1, thresh=threshold)
# print(f"After dropping sparse cols: {df_col_clean.shape}")
# print(f"Dropped: {set(df.columns) - set(df_col_clean.columns)}")

# import pandas as pd

# df=pd.read_csv("titanic.csv")

# most_common_port = df["Embarked"].mode()[0]
# print(f"Most common port: {most_common_port}")

# df["Embarked"] = df["Embarked"].fillna(most_common_port)
# print(f"Embarked missing after fill: {df['Embarked'].isnull().sum()}")


# import pandas as pd

# df=pd.read_csv("titanic.csv")

# print(f"Age missing before: {df['Age'].isnull().sum()}") # 177

# mean_age = df["Age"].mean()
# df_mean = df.copy()
# df_mean["Age"] = df_mean["Age"].fillna(mean_age)
# print(f"Fill with mean ({mean_age:.1f}): {df_mean['Age'].isnull().sum()}missing")

# median_age = df["Age"].median()
# df["Age"] = df["Age"].fillna(median_age)
# print(f"Fill with median ({median_age:.1f}): {df['Age'].isnull().sum()}missing")

# print(df["Age"].describe())


# import pandas as pd

# students = pd.DataFrame({
#  "student_id" : [101, 102, 103, 104, 105, 106],
#  "name" : ["Rahul", "Priya", "Arjun", "Sneha", "Mohammed","alex"],
#  "class" : ["10A", "10B", "10A", "10B", "10A","10B"]
# })

# scores = pd.DataFrame({
#  "student_id" : [101, 102, 103, 104,106,107],
#  "maths" : [85, 92, 78, 95, 88,78],
#  "science" : [90, 88, 76, 91, 82,98]
# })

# inner = pd.merge(students, scores, on="student_id", how="inner")
# print("Inner merge:")
# print(inner)

# left = pd.merge(students, scores, on="student_id", how="left")
# print("\nLeft merge:")
# print(left)

# right = pd.merge(students, scores, on="student_id", how="right")
# print("\nRight merge:")
# print(right)


import pandas as pd
# Two batches of students from different months
batch_jan = pd.DataFrame({
 "name" : ["Rahul", "Priya"],
 "score" : [85, 92]
})
batch_feb = pd.DataFrame({
 "name" : ["Arjun", "Sneha", "Mohammed"],
 "score" : [78, 95, 88]
})
all_students = pd.concat([batch_jan, batch_feb], axis=0, ignore_index=True)
print("Combined all students:")
print(all_students)
