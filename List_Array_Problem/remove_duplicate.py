## Remove duplicate from sorted array(in place) and return unique element count
'''
## without in place
def remove_duplicate(nums):
    seen = set()
    for i in nums:
        if i not in seen:
            seen.add(i)
    return list(seen)

print(remove_duplicate([1,1,1,2,3,4,4,7,9,9,9,10]))

## In place remove duplicate
def remove_duplicate1(nums):
    for i in range(len(nums)):
        if nums[i] == nums[i+1]:
            nums.pop(i)
    return nums

print(remove_duplicate1([1,1,1,2,3,4,4,7,9,9,9,10]))

'''
## method 1 brute  force
def remove_duplicate2(nums):
    freq_map = {}
    for i in range(len(nums)):
        if nums[i] not in freq_map:
            freq_map[nums[i]] = 0
     
    i = 0       
    for j in freq_map.keys():
        nums[i] = j
        i += 1
    return i  ## count number unique element 
        
print(remove_duplicate2([1,1,1,2,3,4,4,7,9,9,9,10]))


### Optimal
def remove_duplicate3(nums):
    n = len(nums)
    if n == 1:
        return 1
    i = 0
    j = i+11
    while j<n:
        if nums[j]!=nums[i]:
            i +=1
            nums[i],nums[j] = nums[j],nums[i]
        j+=1
    return i+1

print(remove_duplicate3([1,1,1,2,3,4,4,7,9,9,9,10]))
