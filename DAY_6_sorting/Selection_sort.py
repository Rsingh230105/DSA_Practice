## Selection sort
def selection_sort(nums):
    n=len(nums)
    for i in range(0,n):
        min_indx = i
        for j in range(i+1,n):
            if nums[j] < nums[min_indx]:
                min_indx = j
        nums[i],nums[min_indx] = nums[min_indx],nums[i]
    return nums

x = selection_sort([5,7,3,2,1,8,9,4])
print(x)

## TC 
'''
Best	O(n²)
Average	O(n²)
Worst	O(n²)
'''

## SC = o(1)
