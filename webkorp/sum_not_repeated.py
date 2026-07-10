'''
3. Sum of Array Elements Excluding Repeated Ones

Input: arr = [1, 2, 2, 3, 4, 4, 5]
Output: 9 (1 + 3 + 5, since 2 and 4 repeat)
'''
## TC = o(n)
## SC = o(n)
## optimal

def sum_of_array(arr):
    d = {}
    
    # for i in arr:
    #     d[i] = d.get(i,0) + 1
        
    
    
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            d[arr[i]] += 1
            
    sum_uniqe_ele = 0
    for k,v in d.items():
        if v == 1:
            sum_uniqe_ele += k
            
    return sum_uniqe_ele

print(sum_of_array([1, 2, 2, 3, 4, 4, 5]))