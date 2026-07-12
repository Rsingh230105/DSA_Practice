'''
--> Distinct Sum
input: [1,2,2,3,4]
Output: 10
'''
def distinct_sum(l):
    seen = {}
    total = 0
    for i in l:
        if i not in seen:
            seen[i] = True
    
    for i in seen.keys():
        total += i
            
    return total




## best optimal
def distinct_sum1(arr):
    seen = {}
    total = 0

    for num in arr:
        if num not in seen:
            seen[num] = True
            total += num

    return total

print(distinct_sum([1,2,2,3,4,4,6]))
print(distinct_sum([1,2,3,2,1,2,5,6,7]))