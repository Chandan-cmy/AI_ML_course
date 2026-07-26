# import numpy as np

# s = np.float64([1,3,5]) 
# print(s)              # 36.6 
# print(s.ndim)         # 0  — zero dimensions, it is a scalar 

# import numpy as np  # A student's features: age, study_hours, attendance%, prev_score 

# student_features = np.array([20, 6.5, 92.0, 78])  
# print(student_features)        # [20.   6.5  92.   78. ] 
# print("Shape:", student_features.shape)   # (4,)  — 4 features 
# print("Length:", len(student_features))   # 4  
# # In ML this single row is called a 'feature vector' 
# # Each column (age, hours, attendance, score) is a 'feature' 

# import numpy as np  # Dataset: 5 customers, 3 features each # Columns: [age, annual_income_thousands, spending_score] 
# customers = np.array([     [25, 35,  81],     [47, 82,  44],     [31, 28,  55],     [22, 16,  20],     [35, 60,  76] ])  
# print(customers.shape)   # (5, 3) — 5 rows (customers), 3 cols (features) 
# print(customers.ndim)    # 2  — it is a 2D matrix  # In ML we call this the feature matrix, often written as X 
# X = customers 
# print(f"Dataset has {X.shape[0]} samples and {X.shape[1]} features")


# import numpy as np 
# a = np.array([2, 3, 4]) 
# b = np.array([1, 5, 2])

# # Method 1: np.dot()
# result = np.dot(a, b) 
# print(result)

# # Method 2: @ operator (cleaner, preferred in modern Python) 
# result2 = a @ b 
# print(result2) # 25

# # Manual verification 
# manual = (2*1) + (3*5) + (4*2) 
# print(manual) # 25

# import numpy as np
# house = np.array([1500, 3, 10, 5])

# weights = np.array([200, 50000, -2000, -10000])
# predicted_price = np.dot(house, weights)
# print(f"Predicted house price: Rs. {predicted_price:,}")

# import numpy as np

# marks = np.array([ [85, 90, 78, 92], [72, 88, 95, 80], [91, 76, 83, 87] ])

# weights = np.array([[0.40], [0.30], [0.20], [0.10]])

# weighted_avg = marks @ weights 
# print("Weighted averages:") 
# print(weighted_avg)

# students = ["Rahul", "Priya", "Arjun"]
# for i, name in enumerate(students):
#     print(f" {name}: {weighted_avg[i,0]:.1f}")

# import numpy as np

# A = np.array([ [1, 2, 3], [4, 5, 6] ])

# print("Original shape:", A.shape) # (2, 3) 
# print(A)

# A_T = A.T 
# print("Transposed shape:", A_T.shape) # (3, 2) 
# print(A_T)

# import numpy as np

# point_a = np.array([3, 4]) 
# norm = np.linalg.norm(point_a) 
# print(f"Norm of [3,4]: {norm}")

# point_b = np.array([0, 0]) 
# distance = np.linalg.norm(point_a - point_b) 
# print(f"Distance: {distance}")

# import numpy as np
# grades = np.array(["A", "B", "A", "C", "A", "B", "A", "D", "B","D"])

# values, counts = np.unique(grades, return_counts=True)
# mode_index = np.argmax(counts) 
# mode = values[mode_index]

# print(f"Grades: {values}") 
# print(f"Counts: {counts}") 
# print(f"Mode (most common grade): {mode}")

# import numpy as np
# scores = np.array([45, 52, 58, 61, 64, 67, 70, 73, 76, 80, 82, 85, 88, 91, 93, 95, 97, 98, 99, 100]) 
# p25 = np.percentile(scores, 25) # Q1 — 25th percentile 
# p50 = np.percentile(scores, 50) # Q2 — Median (same as np.median) 
# p75 = np.percentile(scores, 75)

# print(f"25th percentile (Q1): {p25}") 
# print(f"50th percentile (Q2), Median): {p50}") 
# print(f"75th percentile (Q3): {p75}")

# iqr = p75 - p25 
# print(f"IQR: {iqr}")
# lower_fence = p25 - 1.5 * iqr
# upper_fence = p75 + 1.5 * iqr
# print(f"Outlier bounds: [{lower_fence:.1f}, {upper_fence:.1f}]")
# outliers = scores[(scores < lower_fence) | (scores > upper_fence)]
# print(f"Outliers found: {outliers}")


# import numpy as np
# # 8 students: hours studied and exam score
# hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# exam_scores = np.array([45, 52, 58, 65, 72, 78, 85, 92])
# absences = np.array([8, 7, 6, 5, 4, 3, 2, 1])

# corr1 = np.corrcoef(hours_studied, exam_scores)
# print("Hours vs Scores correlation:")
# print(corr1)
# print(f"Correlation value: {corr1[0,1]:.3f}")


# corr2 = np.corrcoef(absences, exam_scores)
# print(corr2)
# print(f"\nAbsences vs Scores correlation: {corr2[0,1]:.3f}")

# import numpy as np

# np.random.seed(42)

# study_hours = np.array([2, 5, 1, 7, 4, 6, 3, 8, 2, 5])
# attendance = np.array([60, 85, 45, 95, 78, 90, 65, 98, 55, 82])
# prev_score = np.array([50, 72, 38, 88, 65, 80, 55, 91, 42, 70])
# exam_score = np.array([48, 75, 35, 92, 68, 83, 52, 96, 40, 74])

# X = np.column_stack([study_hours, attendance, prev_score])
# y = exam_score

# # print("===== DATASET OVERVIEW =====")
# # print(f"Samples : {X.shape[0]}")
# # print(f"Features: {X.shape[1]}")
# # print(f"Target : exam_score (y)")

# print("\n===== DESCRIPTIVE STATISTICS =====")
# feature_names = ["study_hours", "attendance%", "prev_score"]
# for i, name in enumerate(feature_names):
#     col = X[:, i]
#     print(f"\n{name}:")
#     print(f" Mean : {np.mean(col):.2f}")
#     print(f" Median : {np.median(col):.2f}")
#     print(f" Std : {np.std(col):.2f}")
#     print(f" Min : {np.min(col):.2f}")
#     print(f" Max : {np.max(col):.2f}")

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
#     print("Count          :", arr.size)
#     print("Mean           :", np.mean(arr))
#     print("Median         :", np.median(arr))
#     print("Std Deviation  :", np.std(arr))
#     print("Minimum        :", np.min(arr))
#     print("25th Percentile:", np.percentile(arr, 25))
#     print("75th Percentile:", np.percentile(arr, 75))
#     print("Maximum        :", np.max(arr))
    
# test_arr=np.array([78, 85, 90, 67, 88, 92, 75, 81])

# describe(test_arr,"example")


#Exercise 4 — Correlation Analysis (Intermediate)

# import numpy as np

# np.random.seed(42)

# temperature = np.array([20, 22, 24, 26, 28, 30, 33, 36, 39, 42])

# ice_cream_sales = temperature * 8 + np.random.randint(-10, 11, 10)

# hot_chocolate_sales = 300 - temperature * 5 + np.random.randint(-10, 11, 10)

# correlation_ice = np.corrcoef(temperature, ice_cream_sales)[1,0]
# correlation_hot = np.corrcoef(temperature, hot_chocolate_sales)[1,0]

# print("Temperature:", temperature)
# print("Ice Cream Sales:", ice_cream_sales)
# print("Hot Chocolate Sales:", hot_chocolate_sales)

# print("\nCorrelation (Temperature vs Ice Cream):", correlation_ice)
# print("Correlation (Temperature vs Hot Chocolate):", correlation_hot)

# if correlation_ice > 0:
#     print("Ice cream has Positive Correlation")

# if correlation_hot < 0:
#     print("Hot chocolate has Negative Correlation")


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

# import numpy as np
# hs=np.random.randint(5,10,size=15)

# sl=np.random.randint(0,11,size=15)

# es=np.random.randint(40,100,size=15)

# dataset=np.column_stack((hs,sl,es))
# print(dataset)

import numpy as np

# Dataset
hours_slept = np.array([8,7,9,6,5,8,7,9,6,5,8,7,9,6,5])

stress_level = np.array([2,4,1,6,8,3,5,2,7,9,2,4,1,6,8])

exam_score = np.array([92,82,96,68,50,88,80,94,65,45,90,84,98,70,55])

# Combine dataset
dataset = np.column_stack((hours_slept, stress_level, exam_score))

# Shape
print("Shape:", dataset.shape)

# Descriptive Statistics
features = {
    "Hours Slept": hours_slept,
    "Stress Level": stress_level,
    "Exam Score": exam_score
}

for name, data in features.items():
    print("\n", name)
    print("Mean:", np.mean(data))
    print("Median:", np.median(data))
    print("Std:", np.std(data))
    print("Min:", np.min(data))
    print("Max:", np.max(data))

# Correlation
print("\nCorrelation (Sleep vs Score):", np.corrcoef(hours_slept, exam_score)[0,1])
print("Correlation (Stress vs Score):", np.corrcoef(stress_level, exam_score)[0,1])

# Outlier Detection
q1 = np.percentile(exam_score,25)
q3 = np.percentile(exam_score,75)

iqr = q3-q1

lower = q1-1.5*iqr
upper = q3+1.5*iqr

outliers = exam_score[(exam_score<lower) | (exam_score>upper)]

print("\nOutliers:", outliers)

# Percentage above 75
percentage = np.sum(exam_score>75)/len(exam_score)*100

print("\nPercentage above 75:", percentage,"%")