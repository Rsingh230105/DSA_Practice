def perfect_num(n):
    total = 0
    for i in range(1,n):
        if n%i == 0:
            total += i
    return total == n

print(perfect_num(29))
print(perfect_num(6))
print(perfect_num(28))
