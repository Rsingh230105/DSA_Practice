## method 1 brute force solution
## TC = o(n**2)
## SC = o(1)
def missing_number(nums):
    for i in range(len(nums)+1):
        if i not in nums:
            return i
        

nums = [8,6,4,2,3,5,7,0,1]
# print(missing_number(nums))

## method 2 Better solution
## Tc = o(N), SC = o(N)
def missing_number1(nums):
    n = len(nums)
    d = {}
    
    for i in range(0,n+1):
        d[i]=0
        
    for num in nums:
        d[num] = 1
    
    for k,v in d.items():
        if v == 0:
            return k
                          
print(missing_number1(nums))

## method 3 Optimal
## TC =o(N), SC = o(1)
def missing_number2(nums):
    n = len(nums)
    total_sum = n*(n+1)//2 ## o(1)
    actual_sum = sum(nums)## o(n)
    
    return total_sum - actual_sum

print(missing_number2(nums))