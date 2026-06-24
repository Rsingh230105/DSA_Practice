'''
Quick Sort
1. Pivot
  -> it can be first element
  -> it can be last element
  -> it can be middle element
  -> it can be any random element 
2. put pivot at its correct position/index
## best/avg case
TC = o(nlogn)
SC = o(1)
##
# worst case: TC = o(n**2), SC = o(1)
[5,5,5,5,5,5,5,5,5,5,5,5]
'''
def partition(nums,low,high):
    pivot = nums[low]
    i = low
    j = high
    while i<j:
        while nums[i] <= pivot and i<=high-1:
            i+=1
        while nums[j]> pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]
            
    nums[low],nums[j] = nums[j],nums[low]
    return j
    
def quick_sort(nums,low,high):
    if low<high:
        p_ind = partition(nums,low,high)
        quick_sort(nums,low,p_ind-1)
        quick_sort(nums,p_ind+1,high)
    return nums   

print(quick_sort([4,6,3,1,9,8,7,2,5],0,8))