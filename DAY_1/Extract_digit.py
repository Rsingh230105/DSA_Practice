num = int(input("Enter digit:"))

while num > 0:
    ld = num % 10
    print(ld, end=" ")
    num =num // 10


