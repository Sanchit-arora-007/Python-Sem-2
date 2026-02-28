n = int(input("Enter number of movies: "))
movies = {}

for i in range(n):
    name = input("Movie name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

for name, details in movies.items():
    print(name, details)

print("Movies before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

print("Profitable movies:")
for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print(name)

search_dir = input("Enter director name to search: ")
for name, details in movies.items():
    if details["director"] == search_dir:
        print(name)
