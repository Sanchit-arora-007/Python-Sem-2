f = open("name.txt", "r")
names = [line.strip() for line in f]
f.close()

print("Total names:", len(names))

vowels = "AEIOUaeiou"
count_vowel = 0
for name in names:
    if name[0] in vowels:
        count_vowel += 1
print("Names starting with vowel:", count_vowel)

longest = max(names, key=len)
print("Longest name:", longest)