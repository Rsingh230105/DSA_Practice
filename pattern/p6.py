'''
12345
1234
123
12
1
'''

n = int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j,end=" ")
    print()