n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input(f"Enter value {i+1}: ")))

t = tuple(lst)

total = 0
for num in t:
    total += num

avg = total / n
print("Tuple:", t)
print("Average:", avg)
