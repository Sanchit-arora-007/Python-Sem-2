n = int(input("Enter number of persons: "))
people = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    people[name] = city

print("Names:", people.keys())

print("Cities:", people.values())

for name, city in people.items():
    print(name, "->", city)

city_count = {}
for city in people.values():
    city_count[city] = city_count.get(city, 0) + 1

print("Students per city:", city_count)
