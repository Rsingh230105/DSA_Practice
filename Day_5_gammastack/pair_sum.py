def has_pair_sum(arr,target):
    seen = set()
    for num in arr:
        com = target - num
        if com in seen:
            return True
        seen.add(num)
    return False

op=has_pair_sum(list(map(int,input("Enter the number:").split())), int(input("Enter target value:")))
print(op)

## TC = o(n)
## SC = o(n)

### method 2 brute force approach o(n**2)


def pair_sum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return True