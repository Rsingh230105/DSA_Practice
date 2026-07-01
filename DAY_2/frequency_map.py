# nums = [5,6,7,7,1,9,111,1,1,5,1,1]

# freq_map = {}

# for i in range(len(nums)):
#     if nums[i] not in freq_map:
#         freq_map[nums[i]] = 1
#     else:
#         freq_map[nums[i]] += 1
        
# print(freq_map)

## TC = o(N)
## SC = o(N)

###method 2

nums = [5,6,7,7,1,9,111,1,1,5,1,1]
freq_map = {}
n = len(nums)
for i in range(0,n):
    freq_map[nums[i]] = freq_map.get(nums[i],0)+1