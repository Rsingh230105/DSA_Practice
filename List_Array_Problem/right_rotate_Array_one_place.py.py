## Right rotate array by 1 place

## In place 1 rotate
'''
## using slicing
nums = [5,-2,3,9,0,6,10,7]
print(id(nums))
n = len(nums)
nums[:]= [nums[-1]] + nums[:n-1]
print(nums)
print(id(nums)) 
## same id above and below nums if nums[:] use . without using nums[:] left side new object created (nums)
'''

## without Slicing
## TC = o(n), SC = o(1)
nums = [5,-2,3,9,0,6,10,7]
n = len(nums)
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = temp
print(nums)

