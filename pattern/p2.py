"""
11111
22222
33333
44444
55555

n = int(input("Enter the rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()
"""

n = int(input("Enter the rows:"))
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()
    