# number=input("Enter the number: ")
# new_list=list(map(int, number.split()))
# unique_numbers=set(new_list)
# print(unique_numbers)
# print(new_list)
# print(max(unique_numbers))
# print(min(unique_numbers))

# marks = [45, 82, 65, 91, 39, 75, 88, 54, 97, 30]
# new_marks = [mark for mark in marks if mark >= 70]
# pass_marks = [mark for mark in marks if mark >= 40]


# print(f"marks greater than or equal to 70: {new_marks}")
# print(len(marks))
# print(new_marks)
# print(pass_marks)
# print(max(marks))
# print(min(marks))
# print(sum(marks)/len(marks))



# employees = {}
# n = int(input("Enter number of employees: "))
# for i in range(n):
#     name = input("Enter employee name: ")
#     phone = input("Enter phone number: ")
#     employees[name] = phone
# print("\nEmployee Records:")
# print(employees)
# search = input("\nEnter employee name to search: ")
# if search in employees:
#     print("Phone Number of", search + ":", employees[search])
# else:
#     print("Employee not found.")
    
    

# Print only students who passed (marks >= 40)
# marks_list = [85, 45, 37, 41, 92, 45]
# print("Students who passed:")
# for marks in marks_list:
#     if marks < 40:
#         continue # skip this student, go to next
#     print(f" Marks: {marks} — PASS")

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

def analyse_scores(scores):
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    return highest, lowest, average # returns 3 values
class_scores = [85, 92, 78, 95, 88, 70, 63]
# Unpack the returned values into 3 separate variables
top, bottom, avg = analyse_scores(class_scores)
print(f"Highest : {top}")
print(f"Lowest : {bottom}")
print(f"Average : {avg:.2f}")