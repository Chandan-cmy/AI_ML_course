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

# print("Shape:", marks.shape)
# print("Highest Mark:", marks.max())
# print("Lowest Mark:", marks.min())

# total = np.sum(marks, axis=1)
# print("\nTotal:",total)

# student_avg = np.mean(marks, axis=1)
# print("\nStudent Averages:")
# print(student_avg)

# subject_avg = np.mean(marks, axis=0)
# print("\nSubject Averages:")
# print(subject_avg)

# print("\nMarks above 80:")
# print([marks>80])

#Exercise 3 — Normalisation Function (Intermediate)
# import numpy as np
# price=np.array([199, 499, 99, 999, 299, 149])
# normalized = (price-price.min())/(price.max()-price.min())
# print("Normalised Prices:",normalized)


import n
arr = np.random.randint(50, 101, (4, 3))