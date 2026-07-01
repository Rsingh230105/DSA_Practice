## all element reverse using slicing
#num = [5,7,3,2,6,1,5,9]
#print(num[::-1])

#------------

## Using while loop
## TC  = o(r-l+1) or o(k) 
## SC =o(1)
## K : length of subarray
'''
def reverse_Subarray(num,l,r):
    while  l<r:
        num[l],num[r] = num[r],num[l]
        l += 1
        r -= 1
    return num
    
rev = reverse_Subarray([5,7,3,2,6,1,5,9],2,5)
        
print(rev)  

#-------------
## method 3
def reverse_Subarray(num, l, r):
    for _ in range((r - l + 1) // 2):
        num[l], num[r] = num[r], num[l]
        l += 1
        r -= 1
    return num

rev=reverse_Subarray([5,7,3,2,6,1,5,9],2,5)
print(rev)
'''
#-----------
# method 4

num = [5,7,3,2,6,1,5,9]
num.reverse()
print(num)

