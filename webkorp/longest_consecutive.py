'''
2. Longest Consecutive 1s in a Binary Array

Input: arr = [1, 1, 0, 1, 1, 1, 0, 1]
Output: 3
'''
## optimal
## TC = O(N)
# SC =  o(1)
def longest_con(arr):
    count = 0
    max_count = 0
    for i in arr:
        if i == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count

print(longest_con([1, 1, 0, 1, 1, 1, 0, 1]))