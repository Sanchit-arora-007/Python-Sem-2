n = int(input("Enter number: "))
temp = n
order = len(str(n))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")
