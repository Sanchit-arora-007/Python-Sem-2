def student(name, age):
    print("Name:", name)
    print("Age:", age)

def greet(name="Guest"):
    print("Hello", name)

def total_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum:", total)

student(age=20, name="Sanchit")
greet("Sanchit")
greet()
total_sum(10, 20, 30, 40)

