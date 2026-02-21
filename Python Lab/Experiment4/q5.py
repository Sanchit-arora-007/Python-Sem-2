text = input("Enter a string: ")
text = text.upper()
freq = {}
for char in text:
    if char.isalpha():
        freq[char] = freq.get(char, 0) + 1
for key in sorted(freq):
    print(freq[key], key, sep="")
