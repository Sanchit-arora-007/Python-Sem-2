try:
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()
except:
    count = 0

count += 1

f = open("count.txt", "w")
f.write(str(count))
f.close()

print("Program executed", count, "times")