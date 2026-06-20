''''
num  =  int(input("Enter the number:"))
i = 1
while i<=num:
    if num%i ==0:
        print(i,end=" ")
    i+=1
    
 '''   
#-------
## count factors
num  =  int(input("Enter the number:"))
i = 1
count = 0
while i<=num:
    if num%i ==0:
        count +=1
    i+=1
    
print("total no. of factors:",count)