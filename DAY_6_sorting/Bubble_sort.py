## Bubble sort [Adjacent swap]
## large element last me swap

def bubble_sort(nums):
    n = len(nums)
    
    for i in range(n):
        for j in range(n):
             if j<n-1:
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                        
    return nums

print(bubble_sort([5,8,1,6,9,2,4]))