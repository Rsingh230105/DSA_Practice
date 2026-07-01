##method 1
## TC = o(n)
## SC = o(1)
def largest_element(arr):
    largest = arr[0]
    
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    return largest

print(largest_element([55,32,-97,99,3,67]))

## method 2
def largest_element(arr):
    largest = float("-inf")
    
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    return largest