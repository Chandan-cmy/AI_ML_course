# import numpy as np
# import pandas as pd
# # Salaries in a 10-person startup (in thousands of rupees per month)
# salaries = np.array([25, 28, 27, 30, 26, 29, 28, 27, 26, 500])
# # Note: 500 = the CEO's salary. Everyone else earns 25-30k.
# mean = np.mean(salaries)
# median = np.median(salaries)
# # Mode using pandas
# mode = pd.Series(salaries).mode()[0]
# print(f"Mean salary : Rs. {mean:.0f}k <- This is MISLEADING")
# print(f"Median salary : Rs. {median:.0f}k <- This is HONEST")
# print(f"Mode salary : Rs. {mode:.0f}k <- Most common value")
# print(f"\nThe CEO earns Rs. 500k. Everyone else earns Rs. 25-30k.")
# print(f"The mean ({mean:.0f}k) makes the company sound richer than it is.")
# print(f"The median ({median:.0f}k) tells the real story.")



# import numpy as np
# import matplotlib.pyplot as plt
# # Two exam classes, same average, different spread
# class_consistent = np.array([70, 72, 71, 73, 70, 74, 72, 71, 73, 74])
# class_varied = np.array([40, 95, 30, 98, 55, 88, 20, 99, 45, 90])
# for name, data in [("Consistent class", class_consistent),("Varied class", class_varied)]:
#     print(f"{name}:")
#     print(f" Mean : {np.mean(data):.1f}")
#     print(f" Variance : {np.var(data):.1f}")
#     print(f" Std Dev : {np.std(data):.1f}")
#     print(f" Min-Max : {np.min(data)} to {np.max(data)}")
#     print()


# import numpy as np
# scores = np.array([55, 62, 70, 75, 80, 85, 90, 92, 98])
# mean = np.mean(scores)
# std_dev = np.std(scores)
# # Calculate z-score for every value
# z_scores = (scores - mean) / std_dev
# print(f"Mean : {mean:.1f}")
# print(f"Std Dev: {std_dev:.1f}")
# print()
# print("Score -> Z-Score -> Interpretation")
# print("-" * 50)
# for score, z in zip(scores, z_scores):
#     if z > 2:
#         interp = "Exceptional (outlier high)"
#     elif z > 1:
#         interp = "Above average"
#     elif z > -1:
#         interp = "Average range"
#     elif z > -2:
#         interp = "Below average"
#     else:
#         interp = "Very low (outlier)"
#     print(f"{score:5d} -> {z:+.2f} -> {interp}")
# # Outlier detection: values with |z| > 3 are almost always outliers
# outliers = scores[np.abs(z_scores) > 2]
# print(f"\nPotential outliers (|z| > 2): {outliers}")

# import numpy as np
# # Simulating coin flips to understand probability
# np.random.seed(42)
# flips = np.random.choice(["Heads", "Tails"], size=10000)
# heads_count = np.sum(flips == "Heads")
# tails_count = np.sum(flips == "Tails")
# print(f"Total flips : {len(flips)}")
# print(f"Heads : {heads_count} ({heads_count/len(flips)*100:.1f}%)")
# print(f"Tails : {tails_count} ({tails_count/len(flips)*100:.1f}%)")


# for n in [10, 100, 1000, 10000]:
#     sample = np.random.choice([0, 1], size=n) 
#     prob = np.mean(sample)
#     print(f"n={n:6d}: estimated P(Heads) = {prob:.4f}")


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

# m_third = df[(df["Sex"] == "male") & (df["Pclass"] == 3)]
# p_surv_m3 = m_third["Survived"].mean()
# print(f"P(Survived | Male, 3rd) : {p_surv_m3:.3f}({p_surv_m3*100:.1f}%)")


# import numpy as np
# import matplotlib.pyplot as plt
# np.random.seed(42)

# heights = np.random.normal(loc=170, scale=8, size=10000)
# print(f"Generated {len(heights)} height values")
# print(f"Mean : {np.mean(heights):.2f} cm")
# print(f"Std Dev: {np.std(heights):.2f} cm")
# print(f"Min : {np.min(heights):.1f} cm")
# print(f"Max : {np.max(heights):.1f} cm")

# mean, std = np.mean(heights), np.std(heights)
# within_1std = np.mean(np.abs(heights - mean) <= 1*std) * 100
# within_2std = np.mean(np.abs(heights - mean) <= 2*std) * 100
# within_3std = np.mean(np.abs(heights - mean) <= 3*std) * 100
# print(f"\nWithin 1 std dev (154-186 cm): {within_1std:.1f}% (theory:68%)")
# print(f"Within 2 std dev (146-194 cm): {within_2std:.1f}% (theory: 95%)")
# print(f"Within 3 std dev (138-202 cm): {within_3std:.1f}% (theory:99.7%)")


# import numpy as np
# uniform_data = np.random.uniform(low=0, high=1, size=10000)
# print(f"Mean : {np.mean(uniform_data):.4f} (should be ~0.5)")
# print(f"Std Dev: {np.std(uniform_data):.4f} (should be ~0.289)")

# dice_rolls = np.random.randint(1, 7, size=60000)
# for face in range(1, 7):
#     count = np.sum(dice_rolls == face)
#     print(f"Face {face}: {count/len(dice_rolls)*100:.1f}% (should be16.7%)")


# import numpy as np
# import pandas as pd

# np.random.seed(0)
# income = np.random.exponential(scale=50000, size=1000)
# mean = np.mean(income)
# median = np.median(income)
# print(f"Income distribution:")
# print(f" Mean : Rs. {mean:,.0f}")
# print(f" Median : Rs. {median:,.0f}")
# print(f" Difference: Rs. {mean-median:,.0f}")

# if mean > median * 1.1:
#     print(" -> RIGHT-SKEWED distribution")
#     print(" -> Use MEDIAN as the central measure, not mean")
# elif median > mean * 1.1:
#     print(" -> LEFT-SKEWED distribution")
# else:
#     print(" -> Roughly SYMMETRIC distribution")


# # Bayes' Theorem in Python
# p_disease = 0.01 # 1% of population has disease (prior)
# p_positive_sick= 0.95 # 95% chance test is positive if sick (sensitivity)
# p_positive_well= 0.05 # 5% chance test is positive if healthy (false positive rate)
# # P(Positive) = P(Pos|Sick)*P(Sick) + P(Pos|Healthy)*P(Healthy)
# p_healthy = 1 - p_disease
# p_positive = (p_positive_sick * p_disease) + (p_positive_well * p_healthy)
# # Bayes: P(Sick | Positive) = P(Positive | Sick) * P(Sick) / P(Positive)
# p_sick_given_positive = (p_positive_sick * p_disease) / p_positive
# print(f"P(disease in population) : {p_disease*100:.0f}%")
# print(f"P(test positive if sick) : {p_positive_sick*100:.0f}%")
# print(f"P(test positive if healthy): {p_positive_well*100:.0f}%")
# print(f"")
# print(f"P(actually sick | positive test):{p_sick_given_positive*100:.1f}%")
# print(f"")
# print("Even with a 95% accurate test, a positive result only means")
# print(f"{p_sick_given_positive*100:.1f}% chance of actually having thedisease.")


# from statsmodels.stats.proportion import proportions_ztest
# import numpy as np

# conversions_a = 120
# conversions_b = 145
# total_a = 1000
# total_b = 1000

# rate_a = conversions_a / total_a
# rate_b = conversions_b / total_b

# print(f"Version A conversion rate: {rate_a*100:.1f}%")
# print(f"Version B conversion rate: {rate_b*100:.1f}%")
# print(f"Difference : {(rate_b-rate_a)*100:.1f} percentage points")

# count = np.array([conversions_a, conversions_b])
# nobs = np.array([total_a, total_b])
# z_stat, p_value = proportions_ztest(count, nobs)
# print(z_stat, p_value)
# print(f"\np-value: {p_value:.4f}")

# if p_value < 0.05:
#     print("Result: SIGNIFICANT. The green button performs BETTER.")
#     print("Reject H0. Deploy Version B.")
# else:
#     print("Result: NOT SIGNIFICANT. Difference could be random chance.")
#     print("Fail to reject H0. Keep Version A or run longer test.")



# import numpy as np
# import matplotlib.pyplot as plt

# # Fix the random numbers so output is same every time
# np.random.seed(42)

# # Original population: a highly skewed distribution (exponential)
# population = np.random.exponential(scale=10, size=100000)

# print("Population shape: heavily right-skewed")
# print(f"Population mean: {np.mean(population):.2f}")

# # Take 5000 samples of different sizes and compute their means
# for sample_size in [5, 30, 100, 500]:

#     # Empty list to store sample means
#     sample_means = []

#     # Repeat sampling 5000 times
#     for _ in range(5000):
#         sample = np.random.choice(population, size=sample_size)
#         sample_means.append(np.mean(sample))

#     # Convert list to NumPy array AFTER the loop
#     sample_means = np.array(sample_means)

#     print(f"\nSample size = {sample_size}")
#     print(f"Mean of sample means : {np.mean(sample_means):.2f} (true: ~10)")
#     print(f"Std of sample means  : {np.std(sample_means):.2f}")
#     print("Shape approaching normal: YES (by CLT)")

