## Bubble sort [Adjacent swap]
## large element last me swap
'''
TC = o(n**2)
SC = o(1)
'''

def bubble_sort(nums):
    n = len(nums)
    
    for i in range(n):
        for j in range(n):
             if j<n-1:
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                        
    return nums

print(bubble_sort([5,8,1,6,9,2,4]))

#----------------
# optimize approach
def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True

        if not swapped:
            break

    return nums

'''
| Case                  | Time  |
| --------------------- | ----- |
| Best (already sorted) | O(n)  |
| Average               | O(n²) |
| Worst                 | O(n²) |

space = o(1)
'''
