'''
*
**
***
****
*****
'''
n = int(input("Enter the number:"))
# for i in range(1,n+1):
#     print(i*"*")
    
### method 2
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
    
