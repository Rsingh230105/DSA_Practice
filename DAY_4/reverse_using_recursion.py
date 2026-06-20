def func(nums,left,right):
    if left >= right :
        return nums
    nums[left],nums[right] = nums[right],nums[left]
    return func(nums,left+1,right-1)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
rev = func(nums,int(input("Enter left index:")),int(input("Enter right index:")))
print(rev)