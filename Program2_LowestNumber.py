a = float(input("Give 1st number:"))
b = float(input("Give 2nd number:"))
c = float(input("Give 3rd number:"))


if a<=b and a<=c:
    print(f"{a:.2f}")
elif b<=a and b<=c:
    print(f"{b:.2f}")    
elif c<=a and c<=b:
    print(f"{c:.2f}") 
elif a==b and b==c and a==c:
    print(f"{a,b,c}")




else:
    print("andoy baho!")