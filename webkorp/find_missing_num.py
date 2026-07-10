def missing_number(arr,n):
    total = n*(n+1)//2
    given_total = 0
    for i in arr:
        given_total += i
        
    return total - given_total

print(missing_number([1,2,3,5,6],6))

#TC = o(n)
#SC = o(1)