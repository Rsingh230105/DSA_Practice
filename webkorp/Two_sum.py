'''Q4: Two Sum Problem
Input: arr = [2, 7, 11, 15], target = 9
Output: [0, 1] (indices of 2 and 7)
'''

def two_sum(arr,target):
    seen = {}
    
    for i, num in enumerate(arr):
        com = target - num
        
        if com in seen:
            return [seen[com],i]
        
        seen[num] = i
    
# TC  = o(n)
# SC = o(n)


print(two_sum([2, 7, 11, 15],9))
 