#Question1

# import numpy as np
# a=np.array([10, 20, 30, 40, 50])
# print("shape of array:",a.shape)
# print("type of array:", a.dtype)

#Question 2

# import numpy as np
# a=np.zeros((3,4))
# b=np.ones((2,3))
# print(a,"\n",b)

#Question 3

# import numpy as np
# a=np.arange(1,11)
# print(a)
# b=np.linspace(1,101,5)
# print(b)

#Question 4

# import numpy as np
# arr = np.array([5,10,15,20,25,30])
# a=arr[:3]
# b=arr[-2:]
# c=arr[::2]

# print(f"{a}\n{b}\n{c}")


#Question 5

# import numpy as np
# marks = np.array([[80,90,70],[75,85,95],[60,88,92]])
# print(marks[1,2])

#Question 6

# import numpy as np 
# np.random.seed(42)
# a=np.random.randint(1,13,size=12)
# b=a.reshape(3,4)
# c=a.reshape(2,6)
# d=a.reshape(3,4)

# print(a)
# print(b)
# print(c)
# print(d)

#Question 7

# import numpy as np
# scores = np.array([45,82,91,38,76,95,60])
# passed=scores>=75
# print(passed)
# print(np.sum(passed))

#Question 8

# import numpy as np
# a=np.array([10,20,30,40])
# b=np.array([2,4,6,8])
# addition=a+b
# subtraction=a-b
# multiplication=a*b
# division=a/b

# print(addition,"\n", subtraction,"\n", multiplication,"\n", division)

#Question 9

# import numpy as np

# a = np.array([
#  [85, 90, 78],
#  [72, 88, 95],
#  [91, 76, 83],
#  [60, 70, 65]])

# bonus = np.array([5, 3, 2])
# new_marks=a+bonus
# print(new_marks)

#Question 10

# import numpy as np

# marks = np.array([
#     [85, 90, 78, 88],
#     [76, 81, 69, 72],
#     [92, 95, 89, 94],
#     [65, 70, 60, 68],
#     [80, 85, 82, 79]
# ])

# row_totals = np.sum(marks, axis=1)
# print("\nRow-wise Totals:",row_totals)

# row_averages = np.mean(marks, axis=1)
# print("\nRow-wise Averages:",row_averages)

# column_total = np.sum(marks, axis=0)
# print("\nColumn-wise Averages:",column_total)

# column_averages = np.mean(marks, axis=0)
# print("\nColumn-wise Averages:",column_averages)
# #maximum, minimum, and standard deviation
# print("maximum:",np.max(marks))
# print("minimum:",np.min(marks))
# print("standard deviation:",np.std(marks))

#Question 11

# import numpy as np

# matrix = np.array([
#     [2, 4, 6, 8],
#     [1, 3, 5, 7],
#     [9, 8, 7, 6]
# ])

# weights = np.array([
#     [0.2],
#     [0.3],
#     [0.1],
#     [0.4]
# ])

# weighted_matrix=matrix@weights

# print("\nWeighted matrix:",weighted_matrix)