check_same = lambda d: len(set(d.values())) == 1

d1 = {"a": 10, "b": 10, "c": 10}
d2 = {"a": 10, "b": 20}

print(check_same(d1))
print(check_same(d2))
