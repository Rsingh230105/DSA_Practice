# Sum of all the number from 1 to 100 divisible by 2 and 7

start = int(input("Enter the first number:"))
end = int(input("Enter the end number:"))
i = start
sum = 0

while i<=end:
    if i%2 == 0 and i%7 ==0:
        sum += i
    i+=1

print(sum)
