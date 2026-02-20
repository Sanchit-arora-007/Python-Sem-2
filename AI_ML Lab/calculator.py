print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
choice= int(input("Enter your choice"))
a= int(input("Enter 1st number"))
b= int(input("Enter 2nd number"))
if choice == 1:
    c= a+b
    print(c)
elif choice == 2:
    d= a-b
    print(d)
elif choice == 3:
    e= a*b
    print(e)
elif choice == 4:
    if b == 0:
        print("Invalid Value")
    f= a/b
    print(f)
else:
    print("Invalid Input")