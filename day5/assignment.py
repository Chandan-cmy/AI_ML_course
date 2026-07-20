# Print only students who passed (marks >= 40)


# def calculate_gst(price, gst_rate=0.18):
#     gst_amount = price * gst_rate
#     total = price + gst_amount
#     return total 
# # gives the result back to whoever called this
# # The returned value is captured in a variable
# bill1 = calculate_gst(500)
# bill2 = calculate_gst(1200, 0.15)
# bill3 = calculate_gst(800, 0.12) # 12% GST for this one
# print(f"Bill 1: Rs. {bill1}")
# print(f"Bill 2: Rs. {bill2}")
# print(f"Bill 3: Rs. {bill3}")

# marks = 35
# if marks >= 40:
#     print("Result: PASS")
#     print("Congratulations!")
# else:
#     print("Result: FAIL")
#     print("Please appear for the re-exam.")


# marks = 73
# if marks >= 90:
#     grade = "A+"
#     remark = "Outstanding!"
# elif marks >= 80:
#     grade = "A"
#     remark = "Excellent!"
# elif marks >= 70:
#     grade = "B"
#     remark = "Good work."
# elif marks >= 60:
#     grade = "C"
#     remark = "Average. Can improve."
# elif marks >= 40:
#     grade = "D"
#     remark = "Just passed. Work harder."
# else:
#     grade = "F"
#     remark = "Failed. Please re-appear."
# print(f"Marks: {marks}")
# print(f"Grade: {grade}")
# print(f"Remark: {remark}"


# age = 25
# monthly_income= 45000
# credit_score = 720
# if age >= 21:
#     print("Age requirement met.")
#     if monthly_income >= 30000:
#         print("Income requirement met.")
#         if credit_score >= 700:
#             print("Loan APPROVED! You qualify for all products.")
#         else:
#             print("Loan PARTIALLY approved. Credit score too low for premium loans.")
#     else:
#         print("Loan REJECTED. Income does not meet the minimum requirement.")
# else:
#     print("Loan REJECTED. Applicant must be at least 21 years old.")


# def analyse_scores(scores):
#     highest = max(scores)
#     lowest = min(scores)
#     average = sum(scores) / len(scores)
#     return highest, lowest, average # returns 3 values
# class_scores = [85, 92, 78, 95, 88, 70, 63]
# # Unpack the returned values into 3 separate variables
# top, bottom, avg = analyse_scores(class_scores)
# print(f"Highest : {top}")
# print(f"Lowest : {bottom}")
# print(f"Average : {avg:.2f}")

# count=3

# while count > 0:
#     print(f"Launching in {count}...")
#     count = count - 1 
# print("Liftoff!")


# correct_password="abcdabcd1212"
# attempts=0
# max_attempts=4

# while attempts < max_attempts:
#     attempts+=1
#     passwaord=input("enter the password")
#     if passwaord == correct_password:
#         print('access granted ')
#         break   
#     else:
#         remaining_attempts=max_attempts-attempts
#         if remaining_attempts>0:
#             print(f"wrong password. Remaining attempts:{remaining_attempts}")
#         else:
#             print("account locked, too many failed attempts")
            

# marks_list = [85, 45, 37, 41, 92, 45]
# print("Students who passed:")
# for marks in marks_list:
#     if marks < 40:
#         continue 
#     print(f" Marks: {marks} — PASS")


# numbers = [2, 4, 6, 1, 7 ,5, 9]
# search_number = 9
# for number in numbers:
#     if number == search_number:
#         print(f"Found {search_number}!")
#         break
#     else:
#         print(f"{search_number} was not found in the list.")

# students = ["Rahul", "Priya", "Arjun", "Sneha"]
# search_name = "Kavya"
# for student in students:
#     if student == search_name:
#         print(f"Found {search_name}!")
#         break
#     else:

#         print(f"{search_name} was not found in the list.")




# import math
# print(math.pi) 
# print(math.sqrt(144)) 
# print(math.ceil(4.3)) 
# print(math.floor(4.9)) 
# print(math.pow(2, 2)) 
# print(math.fabs(-7.5))

# import random
# dice = random.randint(1, 6)
# print(f"Dice roll: {dice}")

# probability = random.random()
# print(f"Random probability: {probability:.4f}")

# students = ["Rahul", "Priya", "Arjun", "Sneha", "Mohammed"]
# chosen = random.choice(students)
# print(f"Today's presenter: {chosen}")

# random.shuffle(students)
# print(f"New order: {students}")

# sample = random.sample(students, 2)
# print(f"3 random students: {sample}")

# from datetime import datetime,date
# now = datetime.now()
# print(f"Right now: {now}")
# print(f"Year : {now.year}")
# print(f"Month : {now.month}")
# print(f"Day : {now.day}")
# print(f"Hour : {now.hour}")

# formatted = now.strftime("%d %B %Y, %I:%M %p")
# print(f"Formatted: {formatted}")

# birthday = date(2005, 10, 17)
# today = date.today()
# age_days = (today - birthday).days
# age_years = age_days // 365
# print(f"Age: approximately {age_years} years old")
# import math
# print(math.sqrt(25)) # 5.0

# from math import sqrt, pi
# print(sqrt(25)) # 5.0 (no math. prefix needed)
# print(pi) # 3.141592653589793

# import random as rd
# print(rd.randint(1, 100)

import random
def get_grade(marks):
    if marks>=90:
        return "A+", "Outstanding"
    elif marks >= 80:
        return "A", "Excellent"
    elif marks >= 70:
         return "B", "Good"
    elif marks >= 60:
        return "C", "Average"
    elif marks >= 40:
        return "D", "Passed"
    else:
        return "F", "Failed"
    
def print_result_card(name, marks):
    grade, remark = get_grade(marks)
    status = "PASS" if marks >= 40 else "FAIL"
    print(f" Name : {name}")
    print(f" Marks : {marks} / 100")
    print(f" Grade : {grade}")
    print(f" Status : {status}")
    print(f" Remark : {remark}")
    print(" " + "-" * 30)

students = ["Rahul", "Priya", "Arjun", "Sneha", "Mohammed"]

print("====== CLASS RESULT SHEET ======")
print()

all_marks=[]
for student in students:
    marks = random.randint(30, 100)
    all_marks.append(marks)
    print_result_card(student, marks)
    
print("====== CLASS SUMMARY ======")
print(f" Highest Marks : {max(all_marks)}")
print(f" Lowest Marks : {min(all_marks)}")
print(f" Class Average : {sum(all_marks)/len(all_marks):.1f}")
passed = sum(1 for m in all_marks if m >= 40)
print(f" Students Passed: {passed} out of {len(students)}")





