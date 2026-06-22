def insert_bw_array(arr):
    arr.sort()
    start = arr[0]
    end = arr[-1]
    count = 0
    for i in range(start,end+1):
        if i not in arr:
            count += 1
    return count

print(insert_bw_array([1,3,12]))