def add_two_number(l1, l2):
    op = []
    carry = 0

    i = len(l1) - 1
    j = len(l2) - 1

    while i >= 0 or j >= 0 or carry:

        x = l1[i] if i >= 0 else 0
        y = l2[j] if j >= 0 else 0

        total = x + y + carry

        op.append(total % 10)

        carry = total // 10

        i -= 1
        j -= 1

    

    return op


print(add_two_number([2,4,3],[5,6,4]))
print(add_two_number([0],[0]))
print(add_two_number([9,9,9,9,9,9,9],[9,9,9,9]))