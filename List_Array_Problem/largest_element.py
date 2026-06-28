def largest_element(arr):
    large = arr[0]
    
    for i in range(1,len(arr)):
        if arr[i]>large:
            large = arr[i]
    return large

print(largest_element([55,32,-97,99,3,67]))