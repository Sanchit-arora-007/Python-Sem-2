n = int(input("Enter number of values: "))
values = []

for i in range(n):
    val = int(input("Enter value (0-3): "))
    values.append(val)

count = [0, 0, 0, 0]

for v in values:
    if 0 <= v <= 3:
        count[v] += 1

for i in range(4):
    print(f"{i} occurred {count[i]} times")
