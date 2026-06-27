

nums = [55,32,97,-55,45,32,88,21]
## method 2
## Optimal Solution : single pass
## TC = o(n), SC = o(1)
def second_largest2(nums):
    largest = float("-inf")
    s_largest = float("-inf")
    
    for i in range(len(nums)):
        if nums[i] > largest:
            s_largest = largest
            largest = nums[i]
        elif nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]
    return s_largest
    
    
## method 3 ## better solution: double pass
## TC = o(n)
## SC = o(1)
def second_largest3(nums):
    largest = float("-inf")
    s_largest = float("-inf")
    
    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]
            
    for i in range(len(nums)):
        if nums[i] > s_largest and nums[i]!=largest:
            s_largest = nums[i]
    return s_largest


print(second_largest2(nums))
print(second_largest3(nums))