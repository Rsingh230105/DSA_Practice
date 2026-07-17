'''
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
'''



def arrayPairSum(self, nums):
        
    nums.sort()

    result = 0

    for i in range(0, len(nums), 2):
        result += nums[i]

    return result

print(arrayPairSum([1,4,3,2]))
print(arrayPairSum([6,2,6,5,1,2]))

### Time: O(n log n)
##  Space: O(1) 