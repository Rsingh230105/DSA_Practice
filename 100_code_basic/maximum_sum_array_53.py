#Optimal

# nums = [-2,1,-3,4,-1,2,1,-5,4]

# n = len(nums)
# maxi = float("-inf")
# total = 0

# for i in range(0,n):
#     total = total + nums[i]
#     maxi = max(maxi,total)
#     if total < 0 :
#         total = 0
        
# print(maxi)


## Brute force 
nums = [-2,1,-3,4,-1,2,1,-5,4]
maxi1 = float('-inf')
total1 = 0
n1 = len(nums)
for i in range(0,n1):
    total1 = 0
    for j in range(i,n1):
        total1 = total1 + nums[j]
        maxi1= max(maxi1,total1)
        
print(maxi1)