num = int(input("Enter a number: "))
l = len(str(num))

sum = 0
while num>0:
    ld = num % 10
    sum = sum + (ld ** l)
    num = num // 10

if sum == (num):
    print("Armstrong")
else:
    print("Not Armstrong")