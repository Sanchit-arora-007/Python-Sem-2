def find_max_min(numbers):
    max_val = numbers[0]
    min_val = numbers[0]

    for num in numbers:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val

nums = [10, 6, 8, 90, 12, 56]
print(find_max_min(nums))
