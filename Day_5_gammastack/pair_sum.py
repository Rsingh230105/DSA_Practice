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