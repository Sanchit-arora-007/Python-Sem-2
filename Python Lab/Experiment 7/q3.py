f = open("city.txt", "r")
cities = f.readlines()
f.close()

total_area = 0

for line in cities:
    name, pop, area = line.split()
    pop = float(pop)
    area = float(area)

    print(name, pop, area)

    if pop > 10:
        print("More than 10L:", name)

    total_area += area

print("Total area:", total_area)