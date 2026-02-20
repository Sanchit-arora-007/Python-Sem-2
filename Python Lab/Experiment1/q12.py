print("A B  A&B  A|B  A^B")
print("---------------------")
for A in [0, 1]:
    for B in [0, 1]:
        and_op = A & B
        or_op = A | B
        xor_op = A ^ B
        print(A, B, "  ", and_op, "  ", or_op, "  ", xor_op)
