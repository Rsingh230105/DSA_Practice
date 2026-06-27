## Optimal
def check_arr_sorted(arr):
    if len(arr) <= 1:
        return True
    else:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True
    
print(check_arr_sorted([1,2,3,6,4,5]))