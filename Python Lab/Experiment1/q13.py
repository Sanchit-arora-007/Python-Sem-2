number = int(input("Enter a number: "))
positions = int(input("Enter how many positions to shift: "))
left = number << positions
right = number >> positions
print("After left shift =", left)
print("After right shift =", right)
