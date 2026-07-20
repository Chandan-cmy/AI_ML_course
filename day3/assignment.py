# list=["chandan", "rohan", "bob", 2, 56, 45.89, "python"]
# # print(list[2])
# # print(list[-2])
# # print(list[2:6])
# # print(list[0:6:2])
# list[1]="rohan kumar"
# list.append("phone")
# list.insert(2, "alice")


# new_list=["hello","world"]
# list.extend(new_list)
# print(list)

# fruits = ["apple", "banana", "mango", "banana", "orange", "grapes", "banana"]
# fruits.remove("banana")
# print(fruits)
# removed=fruits.pop(4)
# print(removed)
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)

# scores = [85, 92, 78, 95, 88, 83, 23]
# print(95 in scores)
# print(len(scores))
# print(sum(scores))
# new_scores=[score*2 for score in scores]
# print(new_scores)
# high_scores=[s for s in scores if s>=85 ]
# print(high_scores)

# location = (12.97, 77.59)
# print(location[0]) 
# print(location[1])

# student = {"name": "Rahul", "age": 22, "class": 7, "marks": 85}
# print(student.get("class"))
# print(student.values())

# for keys in student.keys():
#     print(keys)
# for key, value in student.items():
#     print(f"{key} : {value}")

# students = [
#  {"name": "Rahul", "marks": 85, "passed": True},
#  {"name": "Priya", "marks": 92, "passed": True},
#  {"name": "Arjun", "marks": 38, "passed": False},
#  {"name": "Sneha", "marks": 76, "passed": True},]

# for student in students:
#     status = "PASS" if student["passed"] else "FAIL"
#     print(f"{student['name']} : {student['marks']}  {status}")

# skills = {"food", "break fast", "food", "dinner", "food","break fast"}
# print(skills)

# numbers = [3, 5, 2, 8, 1, 5, 2, 3, 8, 5]
# new_numbers=set(numbers)
# print(new_numbers)

# accending_numbers=sorted(new_numbers)
# print(accending_numbers)

# decending_numbers=sorted(new_numbers, reverse=True)
# print(decending_numbers)

# batch_a = {2, 13, 5, 7, 11}
# batch_b = {5, 6, 11, 13, 17}

# print(batch_a | batch_b)
# print(batch_a & batch_b)
# print(batch_a - batch_b)

# student=["rahul","dan","alice","bob","charlie"]
# marks=[ 85, 92, 78, 95, 88]
# print(f"name: {student[0]} | Marks: {marks[0]}")
# print(max(marks))
# print(min(marks))
# print(sum(marks)//len(marks))

# citys = ["New York", "Los Angeles", "Chicago",  "Phoenix", "New York", "Chicago","Houston",]
# sorted_citys=sorted(list(set(citys)))
# print(sorted_citys)

# i = 0
# while i < 5:
#     i += 1
#     name = input("Enter the student's name: ")
#     age = int(input("Enter the student's age: "))
#     class_name = input("Enter the student's class: ")
#     marks = int(input("Enter the student's marks: "))
#     students = {
#         "name": name,
#         "age": age,
#         "class": class_name,
#         "marks": marks
#     }
    
# for value in students.values():
#     print(f"The student's name is {students['name']} and age is {students['age']}. They are in class {students['class']} and scored {students['marks']} marks.")
# name=input("Enter the student's name: ")
# math_marks=float(input("Enter the student's math marks: "))
# physics_marks=float(input("enter the student's physiscs marks:"))
# chemistry_marks=float(input("Enter the student's chemistry marks: "))
# total_marks=math_marks+physics_marks+chemistry_marks
# average_marks=total_marks/3
# if average_marks>=40:
#     print(f"{name} has passed")
# else:
#     print(f"{name} has failed")

# product_name=input("Enter the product name: ")
# quantity=int(input("Enter the quantity: "))
# price_per_unit=float(input("Enter the price per unit: "))
# total_price=quantity*price_per_unit
# discount=0.1
# gst=0.18
# if total_price>5000:
#     total_price=total_price-(total_price*discount)
#     total_price=total_price+(total_price*gst)
# print(f"The total price for {quantity} units of {product_name} is: {total_price}")



student={
    "name": input("Enter the student's name: "),
    "age": int(input("Enter the student's age: ")),
    "city":input("Enter the student's city: "),
    "course":input("Enter the student's course: "),
    "CGPA": float(input("Enter the student's CGPA: "))
}
print(f"Name: {student['name']}, Age: {student['age']}, City: {student['city']}, Course: {student['course']}, CGPA: {student['CGPA']}")


