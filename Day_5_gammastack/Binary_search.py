'''
Input: arr = [1,3,5,7,9], target = 7 → Output: index 3
'''

## Basic method
# def binary_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i


# print(binary_search([1,3,5,7,9],7))

## method 2 : Iterative
def binary_search(arr,target):
    l , r = 0 , len(arr) - 1
    
    while l<=r:
        mid = (l+r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


# # Recursive
# def bs_recursive(arr, l, r, target):
#     if l > r: return -1
#     mid = (l + r) // 2
#     if arr[mid] == target: return mid
#     elif arr[mid] < target:
#         return bs_recursive(arr, mid+1, r, target)
#     else:
#         return bs_recursive(arr, l, mid-1, target)

arr = [1,3,5,7,9]
print(binary_search(arr, 7))  # 3

