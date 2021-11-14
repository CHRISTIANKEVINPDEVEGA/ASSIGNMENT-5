import math
# grade/mark    percentage     description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.50          79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropeed
input_grade = float(input("input your grade percentage:"))
if round(input_grade) >= 97 or round(input_grade) == 100:
    print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 1.00\nDescription: Excellent")
elif round(input_grade) >= 94 and round(input_grade) <= 96:
    print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 1.25\nDescription: Excellent")

elif round(input_grade) >= 91 and round(input_grade) <= 93:
    print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 1.50\nDescription: Very Good")
elif round(input_grade) >= 88 and round(input_grade) <= 90:
    print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 1.75\nDescription: Very Good")

elif round(input_grade) >= 85 and round(input_grade) <= 87:
    print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 2.00\nDescription: Good")
elif round(input_grade) >= 82 and round(input_grade) <= 84:
    print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 2.25\nDescription: Good")

elif round(input_grade) >= 79 and round(input_grade) <= 81:
    print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 2.50\nDescription: Satisfactory")
elif round(input_grade) >= 76 and round(input_grade) <= 78:
    print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 2.75\nDescription: Satisfactory")

elif round(input_grade) == 75:
    print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 3.00\nDescription: Passing")

elif round(input_grade) >= 65 and round(input_grade) <= 74:
    print(f"Input grade: {input_grade:.2f}\nGrade/Mark: 5.00\nDescription: Failure")

print("done!")