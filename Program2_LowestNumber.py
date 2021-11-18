def ask_4_number():
 _FIRST_number = float(input("Give a 1st number: "))
 _SECOND_number = float(input("Give a 2nd number: "))
 _THIRD_number = float(input("Give a 3rd number: "))
 return _FIRST_number, _SECOND_number, _THIRD_number

def display( first_num_, second_num_, third_num_):
 if first_num_<=second_num_ and first_num_<=third_num_:
    print(f"Among the three given number, the lowest is {first_num_:.2f}.")
 elif second_num_<=first_num_ and second_num_<=third_num_:
    print(f"Among the three given number, the lowest is {second_num_:.2f}.")    
 elif third_num_<=first_num_ and third_num_<=second_num_:
    print(f"Among the three given number, the lowest is {third_num_:.2f}.") 
 elif first_num_==second_num_ and second_num_==third_num_ and first_num_==third_num_:
    print(f"Among the three given number, the lowest is {first_num_:.2f}.")

first_number, second_number, third_number = ask_4_number()
display(first_number, second_number, third_number)
