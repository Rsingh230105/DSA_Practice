def func(nums,left,right):
    if left >= right :
        return nums
    nums[left],nums[right] = nums[right],nums[left]
    return func(nums,left+1,right-1)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
rev = func(nums,int(input("Enter left index:")),int(input("Enter right index:")))
print(rev)

##------
'''
Time Complexity: O(right − left + 1)
Space Complexity: O(right − left + 1) due to the recursive call stack

Compared to the iterative while loop version:

Iterative: O(k) time, O(1) space
Recursive: O(k) time, O(k) space
'''
