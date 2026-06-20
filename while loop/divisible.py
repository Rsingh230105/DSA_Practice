start = int(input("Enter the number:"))
end = int(input("Enter the number:"))

i = start
while i<=end:
    if i % 3 == 0 and i % 5 == 0 :
        print(i)
    i+=1
