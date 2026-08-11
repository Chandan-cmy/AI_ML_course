# # Exercise 1 — Statistics Deep Dive (Beginner)

# import numpy as np

# np.random.seed(42)

# n=np.random.normal(loc=50,scale=10,size=1000)
# exp=np.random.exponential(scale=20, size=1000)
# uniform_d=np.random.uniform(low=0, high=1, size=10000)
# def results(s):
#     print(f"Mean:{np.mean(s)}")
#     print(f"Median:{np.median(s)}")
#     print(f"Standard Deviation:{np.std(s)}")
#     return

# print("\n",results(n))

# print("\n",results(exp))
# print("\n",results(uniform_d))


# # Exercise 2 — Z-Score Outlier Detector (Beginner-Intermediate)

# import numpy as np

# def detect_outliers_zscore(data, threshold=3):
#     mean = np.mean(data)
#     std = np.std(data)
#     z_scores = (data - mean) / std
#     outliers = data[np.abs(z_scores) > threshold]
#     return outliers

# salaries = np.array([28, 31, 29, 32, 30, 28, 500, 29, 31, 27, 480, 30, 29])


# print("Outliers in salaries for threshold 3: ")
# print(detect_outliers_zscore(salaries, threshold=3))

# print("Outliers in salaries for threshold 2: ")
# print(detect_outliers_zscore(salaries, threshold=2))


# Exercise 3 — Conditional Probability on Titanic (Intermediate)

# import pandas as pd

# df = pd.read_csv("titanic_cleaned.csv")

# p_survived = df["Survived"].mean()
# print(f"P(Survived) : {p_survived:.3f}({p_survived*100:.1f}%)")

# females = df[df["Sex"] == "female"]
# p_surv_f = females["Survived"].mean()
# print(f"P(Survived | Female) : {p_surv_f:.3f}({p_surv_f*100:.1f}%)")

# males = df[df["Sex"] == "male"]
# p_surv_m = males["Survived"].mean()
# print(f"P(Survived | Male) : {p_surv_m:.3f}({p_surv_m*100:.1f}%)")

# f_first = df[(df["Sex"] == "female") & (df["Pclass"] == 1)]
# p_surv_f1 = f_first["Survived"].mean()
# print(f"P(Survived | Female, 1st) : {p_surv_f1:.3f}({p_surv_f1*100:.1f}%)")

# f_second = df[(df["Sex"] == "female") & (df["Pclass"] == 2)]
# p_surv_f2 = f_second["Survived"].mean()
# print(f"P(Survived | Female, 2nd) : {p_surv_f2:.3f}({p_surv_f2*100:.1f}%)")

# f_third = df[(df["Sex"] == "female") & (df["Pclass"] == 3)]
# p_surv_f3 = f_third["Survived"].mean()
# print(f"P(Survived | Female, 3rd) : {p_surv_f3:.3f}({p_surv_f3*100:.1f}%)")

# m_third = df[(df["Sex"] == "male") & (df["Pclass"] == 3)]
# p_surv_m3 = m_third["Survived"].mean()
# print(f"P(Survived | Male, 3rd) : {p_surv_m3:.3f}({p_surv_m3*100:.1f}%)")