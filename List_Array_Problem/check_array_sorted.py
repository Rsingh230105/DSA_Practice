## Optimal
## TC = o(n)
## SC= o(1)

def check_arr_sorted(arr):
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
    
print(check_arr_sorted([1,2,3,6,4,5]))