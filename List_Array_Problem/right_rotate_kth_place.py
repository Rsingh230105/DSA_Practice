# Right rotate Array by kth place, in place

## TC =o(n), SC = o(n): slicing extra space contain
nums = [5,-2,3,9,0,6,10,7]
def right_rotate(nums, k):
    n=len(nums)
    for i in range(n):
        k = k%n
        if i == k:
            return nums[n-i:] + nums[:n-i]
        

print(right_rotate(nums, 2))

## optimal 
# TC = o(n)
# SC = o(1)



