def ask_4_age():
   age_input=int(input("Type your age: "))
   return age_input

def display(age):
   if age >= 0 and age <=12:
    print("life stage: Kid")
   elif age >= 13 and age <=17:
    print("life stage: Teen")
   elif age == 18:
    print("life stage: Debut")
   elif age >= 19:
    print("life stage: Adult")  

ASK_4_AGE=ask_4_age()
display(ASK_4_AGE)

print("done!")