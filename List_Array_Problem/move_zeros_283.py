## Leetcode problem : 283
## Move Zeros to the End In place without changing order

## mehtod 1
def move_zero(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
    return nums

print(move_zero([0,1,0,3,12]))

## method 2 Brute force and without built in method\
def move_zero1(nums):
    n = len(nums)
    temp = []
    
    ## append non-zero element  
    for i in range(n):
        if nums[i] != 0:
            temp.append(nums[i])
            
    temp_len = len(temp)
    
    #update nums from temp non-zero element 
    for i in range(0,temp_len):
        nums[i] = temp[i]
        
    ## last append non-zero element
    for i in range(temp_len,n):
        nums[i] = 0
    return nums

print(move_zero1([0,1,0,3,12,0,2,3]))
    
## TC = o(n)  ,SC = o(1) ## if given nums all element non zero
#-------------
## method 3 : Optimal Solution

def move_zero2(nums):
    n = len(nums)
    
    if n == 1:
        return 
    i = 0
    ## if all element Zero
    while i<n:
        if nums[i] == 0:
            break
        i += 1
    
    ## if In nums, all element non-zero so,    
    if i == n:
        return
    j = i + 1
    
    while j<len(nums):
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
        j += 1
    
    return nums

print(move_zero2([0,1,0,3,12,0,2,3]))

## TC = o(n)
## SC = o(1)
    