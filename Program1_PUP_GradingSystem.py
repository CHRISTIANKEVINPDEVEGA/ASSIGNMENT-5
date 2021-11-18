import math

def ask_4_grade():
 _Input_grade = input("Input your grade percentage: ")
 return _Input_grade

def display(Input_grade):
 if Input_grade == "Inc.":
    print("Description: Incomplete")
 elif Input_grade == "W":
    print("Description: Withdrawn")
 elif Input_grade == "D":
    print("Description: Dropped")
 else:
   input_grade = float(Input_grade)
   if math.ceil(input_grade) >= 97 and math.ceil(input_grade) <= 100:
     print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 1.00\nDescription: Excellent")
   elif math.ceil(input_grade) >= 94 and math.ceil(input_grade) <= 96:
     print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 1.25\nDescription: Excellent")
   elif math.ceil(input_grade) >= 91 and math.ceil(input_grade) <= 93:
     print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 1.50\nDescription: Very Good")
   elif math.ceil(input_grade) >= 88 and math.ceil(input_grade) <= 90:
     print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 1.75\nDescription: Very Good")
   elif math.ceil(input_grade) >= 85 and math.ceil(input_grade) <= 87:
     print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 2.00\nDescription: Good")
   elif math.ceil(input_grade) >= 82 and math.ceil(input_grade) <= 84:
     print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 2.25\nDescription: Good")
   elif math.ceil(input_grade) >= 79 and math.ceil(input_grade) <= 81:
     print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 2.50\nDescription: Satisfactory")
   elif math.ceil(input_grade) >= 76 and math.ceil(input_grade) <= 78:
     print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 2.75\nDescription: Satisfactory")
   elif math.ceil(input_grade) == 75:
     print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 3.00\nDescription: Passing")
   elif math.ceil(input_grade) >= 65 and math.ceil(input_grade) <= 74:
     print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 5.00\nDescription: Failure")

INPUT_GRADE = ask_4_grade()
display(INPUT_GRADE)
print("done!")