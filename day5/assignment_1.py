# import numpy as np
# # prices = np.array([199, 349, 99, 599]) # NumPy array
# # new_prices = prices * 1.18 
# # print(new_prices)

# # scores = np.array([85, 92, 78, 95, 88])
# # print(scores)
# # print(type(scores)) # <class 'numpy.ndarray'>
# # print(scores.dtype)

# # marks_table = np.array([[85, 92, 78], [90, 85, 88], [70, 75, 80] ])
# # print(marks_table)
# # print(marks_table.shape) 

# # empty_scores = np.zeros(8)
# # print(empty_scores)

# # weight_matrix = np.zeros((3, 4))
# # print(weight_matrix)

# # all_ones = np.ones((2, 3))
# # print(all_ones)

# # a = np.arange(10)
# # print(a)

# # b = np.arange(1, 21, 3)
# # print(b)

# # c = np.arange(0.0, 1.1, 0.1)
# # print(c)

# # a = np.linspace(0, 1, 5)
# # print(a)

# # temps = np.linspace(0, 100, 10)
# # print(temps)

# c = np.empty((2, 3))
# print(c)

import numpy as np

# results = np.array([
#  [85, 90, 78, 92],
#  [72, 88, 95, 80],
#  [91, 76, 83, 87]
# ])

# print("Shape :", results.shape) # (3, 4) — 3 students, 4 subjects
# print("Dimensions:", results.ndim) # 2 — it is a 2D table
# print("Total marks:", results.size)# 12 — 12 numbers in total
# print("Data type:", results.dtype) # int64

# flat = np.arange(1, 13)
# # print(flat) # [ 1 2 3 4 5 6 7 8 9 10 11 12]
# # print(flat.shape) 

# # table = flat.reshape(3, 4)
# # print(table)
# # print(table.shape)

# # table2 = flat.reshape(2, 6)
# # print(table2)

# auto = flat.reshape(4, -1) # 4 rows, NumPy figures out columns = 3
# print(auto.shape) 


# scores = np.array([85, 92, 78, 95, 88, 70, 99])

# # print(scores[0]) # 85 (first)
# # print(scores[-1]) # 99 (last)
# # print(scores[3]) # 95
# # # Slicing [start : end : step]
# # print(scores[1:4])
# # print(scores[:3]) 
# # print(scores[4:]) 
# # print(scores[::2]) 
# print(scores[::-2]) 


# results = np.array([
#  [85, 90, 78], # Student 0: Rahul
#  [72, 88, 95], # Student 1: Priya
#  [91, 76, 83], # Student 2: Arjun
#  [60, 70, 65] # Student 3: Sneha
# ])
# # Single element: [row, column]
# print(results[0, 0]) # 85 (Rahul's Maths mark)
# print(results[1, 2]) # 95 (Priya's English mark)
# print(results[-1, -1]) # 65 (Sneha's English mark)
# # Entire row (one student's results)
# print(results[1]) # [72 88 95] (Priya's all marks)
# print(results[1, :]) # [72 88 95] (same, explicit)
# # Entire column (all students' marks for one subject)
# print(results[:, 0]) # [85 72 91 60] (all Maths marks)
# print(results[:, 1]) # [90 88 76 70] (all Science marks)
# # Sub-table: first 2 students, last 2 subjects
# print(results[:2, 1:])
# print

# scores = np.array([85, 92, 78, 95, 38, 70, 99, 45, 30])

# passed_marks = scores>=40
# print(passed_marks)

# passed_scores= scores[passed_marks]
# print(passed_scores)

# print(scores[scores >= 40])
# print(scores[scores > 90])

# print(np.sum(scores >= 40))


# import numpy as np
# maths = np.array([85, 72, 91, 60])
# science = np.array([90, 88, 76, 70])

# total = maths + science
# print(total) # [175 160 167 130]

# diff = maths - science
# print(diff) # [ -5 -16 15 -10]

# doubled = maths * 2
# print(doubled) # [170 144 182 120]

# avg = (maths + science) / 2
# print(avg) # [87.5 80. 83.5 65. ]

# prices = np.array([100, 250, 80, 500, 120])
# with_gst = prices * 1.18
# print(with_gst) # [118. 295. 94.4 590. 141.6]

# import numpy as np
# scores = np.array([85, 92, 78, 95, 88, 70, 99, 63])
# print("Sum :", np.sum(scores)) # 670
# print("Mean :", np.mean(scores)) # 83.75
# print("Median :", np.median(scores)) # 86.5
# print("Max :", np.max(scores)) # 99
# print("Min :", np.min(scores)) # 63
# print("Std Dev :", np.std(scores)) # 11.67 (standard deviation)
# print("Variance:", np.var(scores)) # 136.19



# subject_avg = np.mean(marks, axis=1)
# print("Subject averages:", subject_avg)

# test=np.linspace(0,10,20)
# print(test)

# c = np.empty((2, 3))
# print(c)

# print(marks.ndim)

# marks = np.array([
#  [85, 90, 78],
#  [72, 88, 95], 
#  [91, 76, 83] 
# ])

# """if the axis=0 then it will compute per column it will go down
#     if the axis=1 then it will compute per row it will go side ways"""
    
# subject_avg = np.mean(marks, axis=0)
# print("Subject averages:", subject_avg)

# student_avg = np.mean(marks, axis=1)
# print("Student averages:", student_avg)

# student_total = np.sum(marks, axis=1)
# print("Student totals :", student_total)

# b=np.full((1,3),fill_value=5)
# print(b)

# a = np.full((2, 4), fill_value=7)
# print(a)

# flat = np.arange(1, 13)
# print(flat)
# print(flat.shape)

# table = flat.reshape(3, 4)
# print(table)
# print(table.shape) # (3, 4)


# table2 = flat.reshape(2, 6)
# print(table2)

# auto = flat.reshape(6, -1)
# print(auto)# 4 rows, NumPy figures out columns = 3
# print(auto.shape)

# import numpy as np
# prices = np.array([100, 250, 80, 500, 120])
# with_shipping = prices + 50
# print(with_shipping)

# discounted = prices * 0.80
# print(discounted)

# marks = np.array([
#  [85, 90, 78],
#  [72, 88, 95],
#  [91, 76, 83],
#  [60, 70, 65]
# ])

# bonus = np.array([5, 3, 2])
# new_marks = marks + bonus
# print(new_marks)




# students = ["Rahul", "Priya", "Arjun", "Sneha", "Mohammed"]
# subjects = ["Maths", "Science", "English", "Hindi"]
# marks = np.array([
#  [85, 90, 78, 92],
#  [72, 88, 95, 80],
#  [91, 76, 83, 87],
#  [60, 70, 65, 55],
#  [95, 92, 89, 97]
# ])

# print(f"Data shape: {marks.shape}")

# totals = np.sum(marks, axis=1)
# averages = np.mean(marks, axis=1)

# print("\nStudent Results:")
# for i, name in enumerate(students):
#     grade = "PASS" if averages[i] >= 40 else "FAIL"
#     print(f" {name:10}: Total={totals[i]}, Avg={averages[i]:.1f} —{grade}")

# subject_avg = np.mean(marks, axis=0)
# print("\nSubject Averages:")
# for i, sub in enumerate(subjects):
#     print(f" {sub:10}: {subject_avg[i]:.1f}")
 
# print(f"\nClass highest : {np.max(marks)}")
# print(f"Class lowest : {np.min(marks)}")
# print(f"Class average : {np.mean(marks):.1f}")

# high_scorers = marks > 85
# print(f"\nMarks above 85: {np.sum(high_scorers)} out of {marks.size}")

# normalised = (marks - marks.min()) / (marks.max() - marks.min())
# print(f"\nNormalised (sample): {normalised[1]}")