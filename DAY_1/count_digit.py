num = int(int(input("Enter digit:")))

count = 0

while num > 0:
    ld = num % 10
    count += 1
    num =num // 10
print(count)