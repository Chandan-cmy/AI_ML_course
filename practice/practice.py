#----------------------day2-------------------------

#Exercise 1 — Personal Info Printer (Beginner)

# name="chandan"
# age="21"
# city="bangalore"
# student=True
# print(f"My name is {name}, I am {age} years old, from {city}, and student status: {student} ")


# Exercise 2 — Simple Calculator (Beginner-Intermediate)

# a=int(input('enter the first number'))
# b=int(input('enter the second number'))
# print("Addition:",a+b)
# print("subraction:",a-b)
# print("Multipliction",a*b)
# print("result in decimal",float(a/b))
# print("floor devision",a//b)
# print("remainder:",a%b)

# Exercise 3 — Age Eligibility Checker (Intermediate)

# age= int(input("enter the age"))
# if age >= 18:
#     print("eligible to vote")   
# else:
#     print("noteligible to vote")
    
# if age>=21:
#     print("eligible to rent a car")
# else:
#     print("not eligible to rent a car")

# if age>=15 and age<21:
#     print("eligible to student discount")
# else:
#     print("not eligible to student discount")


# Exercise 4 — Shopping Bill (Intermediate)

# product_name=input("Enter the product name: ")
# quantity=int(input("Enter the quantity: "))
# price_per_unit=float(input("Enter the price per unit: "))
# subtotal=quantity*price_per_unit
# print(f"product name:{product_name}\n subtotal:{subtotal}")
# gst=0.18
# adding_gst=subtotal*gst
# print('after GST:',subtotal+adding_gst)

# Stretch Challenge — Tier A students

# name=input('Enter the name')
# w=int(input("Enter the wieght(in kgs):"))
# h=float(input("Enter the height(in m):"))
# bmi=(w/h**2)
# print(f"BMI value is {bmi:.2f}")
# if bmi > 18.5:
#     print("Underweight")
# elif bmi>18.5 and bmi<24.9:
#     print("Normal")
# elif bmi >25 and bmi<29.9:
#     print("Overweight")
# else:
#     print("Obese")

# ---------------------------------day3-------------------------------------

# Exercise 1 — Student Mark Sheet (Beginner)

# student=["rahul","dan","alice","bob","charlie"]
# marks=[ 85, 92, 78, 95, 88]
# print(f"name: {student[0]} | Marks: {marks[0]}")
# print(max(marks))
# print(min(marks))
# print(sum(marks)//len(marks))

# Exercise 2 — Remove Duplicates (Beginner-Intermediate)

# citys = ["New York", "Los Angeles", "Chicago",  "Phoenix", "New York", "Chicago","Houston",]
# sorted_citys=sorted(list(set(citys)))
# print(sorted_citys)


# Exercise 3 — Student Profile (Intermediate)


# name = input("enter the student's name: ")
# age = int(input("enter the student's age: "))
# city=input("enter the city")
# subject = input("enter the student's favourite subject: ")
# students = {
#         "name": name,
#         "age": age,
#         "city":city,
#         "subject": subject
#     }
    
# print(" profile card \n")
# print(f"Name:{students['name']}")
# print(f"Age: {students['age']}")
# print(f"City: {students['city']}")
# print(f"Favourite Subject : {students['subject']}")
    

# Exercise 4 — Class Register (Intermediate)

# students = [
#     {"name": "Rahul", "marks": 85, "passed": True},
#     {"name": "Priya", "marks": 35, "passed": False},
#     {"name": "Amit", "marks": 62, "passed": True},
#     {"name": "Sneha", "marks": 40, "passed": True}
# ]

# for student in students:
#     if student["passed"]:
#         print(student["name"], "- Passed")
#     else:
#         print(student["name"], "- Failed")
        
# Exercise 5 — List Comprehension Practice (Intermediate)

# numbers = [12, 25, 8, 64, 51, 37, 90, 45]
# sq = [i**2 for i in numbers]
# print("squared List",sq)
# en = [j for j in numbers if j % 2 == 0]
# print("even numbers",en)
# g=[k for k in numbers if k > 50]
# print("greater than 50",g)

# ---------------------------------day4-------------------------------------

# Exercise 1 — Grade Calculator Function (Beginner)

# def get_grade(marks):
    
#     if marks >= 90:
#         return "A+ grade"
#     elif marks >= 80:
#         return "A grade"
#     elif marks >= 70:
#         return "B grade"
#     elif marks >= 60:
#         return "C grade"
    
#     elif marks >= 40:
#         return "D grade"
#     else:
#         return "F grade"

# print(get_grade(85))

# Exercise 2 — Number Patterns with Loops (Beginner-Intermediate)

# def multiplication():
#     num = int(input("Enter a number: "))
#     print(f"multiples of {num} is ")
#     for i in range(1, 11):
#         mul=num*i
#         print(f"{num}x{i}:{mul}")
        
    
# print(multiplication())

# def sum():
#     n = int(input("Enter the value of N: "))
#     t = 0
#     for i in range(1, n + 1):
#         t += i
    
#     print(f"Sum of numbers from 1 to {n} = {t}")
    
# print(sum())

# Exercise 3 — List Processor Function (Intermediate)

# def analyse_list(numbers):
#     result = {
#         "count": len(numbers),
#         "sum": sum(numbers),
#         "avg": sum(numbers) / len(numbers),
#         "max": max(numbers),
#         "min": min(numbers)
#     }
#     return result

# list_1 = [10, 20, 30, 40, 50]
# result=analyse_list(list_1)

# for key,value in result.items():
#     print(f"{key}:{value}")

# Exercise 4 — Number Guessing Game (Intermediate)

# --------------------------------------day5---------------------------------------------------

# Exercise 1 — Array Creation Practice (Beginner)

# import numpy as np

# a=np.zeros((3,5))
# print(a)
# print(a.shape)

# b=np.ones((4,4))
# print(b)
# print(b.shape)

# c=np.arange(10,50,5)
# print(c)
# print(c.shape)

# d=np.linspace(0,1,8)
# print(d)
# print(d.shape)

# e=np.eye(3)
# print(e)
# print(e.shape)


#Exercise 2 — Student Marks Analyser (Beginner-Intermediate)

# import numpy as np

# marks = np.array([
#     [85, 78, 92, 88],
#     [67, 75, 70, 80],
#     [90, 95, 89, 94],
#     [55, 60, 58, 62],
#     [76, 82, 79, 85],
#     [88, 91, 84, 87]
# ])

# print("shape:", marks.shape)
# print("highest Mark:", marks.max())
# print("lowest Mark:", marks.min())

# total = np.sum(marks, axis=1)
# print("total:",total)

# student_avg = np.mean(marks, axis=1)
# print("student Averages:",student_avg)

# subject_avg = np.mean(marks, axis=0)
# print("\nSubject Averages:",subject_avg)

# print("\nMarks above 80:",[marks>80])


#Exercise 3 — Normalisation Function (Intermediate)

# import numpy as np
# price=np.array([199, 499, 99, 999, 299, 149])
# normalized = (price-price.min())/(price.max()-price.min())
# print("Normalised Prices:",normalized)

# Exercise 4 — Broadcasting Practice (Intermediate)


# import numpy as np
# arr = np.random.randint(50, 101, (4, 3))
# bonus=np.array([3, 5, 2])
# new_arr = arr+bonus
# print(new_arr)

# a=np.mean(new_arr,axis=0)
# print(a)
# b=new_arr-a
# print(b)
# print(b[b>80])

# Exercise 5 — Checkerboard Pattern (Intermediate-Stretch)

# import numpy as np
# a=np.zeros((8,8))

# a[1::2, ::2]=1
# a[::2,1::2]=1
# print(a)


# ---------------------------------------------day6------------------------------------------

#Exercise 1 — Dot Product Prediction (Beginner)
# import numpy as np

# houses = np.array([
#     [1200, 2, 1, 20],
#     [1800, 3, 2, 5],
#     [2500, 4, 3, 2]
# ])

# weights = np.array([150, 45000, 30000, -1500])
# print("Predicted House Prices:")
# for i in range(len(houses)):
#     predictions = np.dot(houses[i], weights)
#     print(f"houses{i}={predictions}")



#Exercise 2 — Statistics Summary Function (Beginner-Intermediate)
# import numpy as np

# def describe(arr, name):
   
#     print(f"{name}:{arr}")
#     print("Count:", arr.size)
#     print("Mean:", np.mean(arr))
#     print("Median:", np.median(arr))
#     print("Std Deviation:", np.std(arr))
#     print("Minimum:", np.min(arr))
#     print("25th Percentile:", np.percentile(arr, 25))
#     print("75th Percentile:", np.percentile(arr, 75))
#     print("Maximum:", np.max(arr))
    
# test_arr=np.array([78, 85, 90, 67, 88, 92, 75, 81])

# describe(test_arr,"example")

#Exercise 3 — Outlier Detector (Intermediate)

# import numpy as np
# def  find_outliers(arr):
#     q1=np.percentile(arr,25)
#     q3=np.percentile(arr,75)
#     iqr=q3-q1
#     ll=q1-1.5*iqr
#     ul=q3+1.5*iqr
#     outliere= arr[(arr<ll) | (arr>ul)]
#     return outliere
# employee_salaries=np.array([28000, 31000, 29500, 32000,30000, 28500, 550000, 29000, 31500, 27000, 480000])

# print(len(find_outliers(employee_salaries)))

# Exercise 5 — Mini NumPy EDA (Intermediate)

# import numpy as np
# hs=np.random.randint(5,10,size=15)

# sl=np.random.randint(0,11,size=15)

# es=np.random.randint(40,100,size=15)

# dataset=np.column_stack((hs,sl,es))
# print(dataset)

# print("Shape:", dataset.shape)
# features = {
#     "Hours Slept": hs,
#     "Stress Level": sl,
#     "Exam Score": es
# }

# for name, data in features.items():
#     print("\n", name)
#     print("Mean:", np.mean(data))
#     print("Median:", np.median(data))
#     print("Std:", np.std(data))
#     print("Min:", np.min(data))
#     print("Max:", np.max(data))

# print("\nCorrelation (Sleep vs Score):", np.corrcoef(hs, es)[0,1])
# print("Correlation (Stress vs Score):", np.corrcoef(sl,es)[0,1])

# q1 = np.percentile(es,25)
# q3 = np.percentile(es,75)

# iqr = q3-q1

# ll = q1-1.5*iqr
# ul = q3+1.5*iqr

# outliers = es[(es<ll) | (es>ul)]
# print("\nOutliers:", outliers)
# percentage = np.sum(es>75)/len(es)*100
# print("\nPercentage above 75:", percentage,"%")

# -------------------------------------day7---------------------------

#Exercise 1

# import pandas as pd
# df = pd.read_csv("titanic.csv")

# print("Shape:",df.shape)


# print("Column Names:",df.columns)

# print("First 8 Rows:",df.head(8))

# print("Last 5 Rows:",df.tail())

# print("Data Types:",df.dtypes)


# missing = (df.isnull().sum() / len(df)) * 100
# print("Missing Values Percentage:",missing)

# print(df.isnull().sum())

#Exercise 2


# import pandas as pd
# df = pd.read_csv("titanic.csv")

# print("Selected Columns")
# print(df[["Name", "Age", "Sex", "Survived"]])

# print("\n10th to 20th Rows")
# print(df.iloc[10:21])

# print("\nFare of Passenger at Index 100")
# print(df.loc[100, ["Fare","Name","Age","Sex"]])

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

# male_old = df[(df["Sex"] == "male") &(df["Age"] > 50) &(df["Survived"] == 0)]
# print("Male >50 and Not Survived:", len(male_old))

# Exercise 4

# import pandas as pd
# df = pd.read_csv("titanic.csv")

# df["fare_inr"] = df["Fare"] * 90

# df["is_child"] = df["Age"] < 18

# df["family_size"] = df["SibSp"] + df["Parch"] + 1

# print(df[["Name", "fare_inr", "is_child", "family_size"]].head(10))

#Exercise 5

import pandas as pd
df = pd.read_csv("titanic.csv")

# print("shape:",df.shape)

# print("info:",df.info())

# print("describe:",df.describe())

# print("missing values:",df.isnull().sum())

print(df.loc[:, 'Age'] )