n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores: ").split()))

unique_scores = list(set(scores))
unique_scores.sort()

print("Runner-up score:", unique_scores[-2])
