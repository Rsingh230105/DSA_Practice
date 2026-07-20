
## TC = o(n),SC = o(1)
def perfect_num(n):
    total = 0
    for i in range(1,n):
        if n%i == 0:
            total += i
    return total == n

print(perfect_num(29))
print(perfect_num(6))
print(perfect_num(28))

## other best approach
import math

def perfect_num(n):
    if n <= 1:
        return False

    total = 1

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i

    return total == n

print(perfect_num(28))

## TC = o(n**0.5)
## SC = o(1)

