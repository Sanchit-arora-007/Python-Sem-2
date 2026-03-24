f = open("numbers.txt", "r")
nums = [int(line.strip()) for line in f]
f.close()

print("Max:", max(nums))

avg = sum(nums) / len(nums)
print("Average:", avg)

count = 0
for n in nums:
    if n > 100:
        count += 1
print("Count >100:", count)