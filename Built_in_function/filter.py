'''
-->filter(function,iterable)
---> filter() is built in python function used to filter elements from an iterable based on a condition.
---> filter() return filter object and  iterable object .
----> filter() return True or False.

Function	Time Complexity	           Space Complexity*
map()	        O(n)	               O(n) if you convert to list()
filter()	    O(n)	               O(n) if you convert to list()
'''

nums = [1,2,3,4,5,6,7,8,9,10]
res = list(filter(lambda x:x%2==0,nums))
print(res) # [2, 4, 6, 8, 10]

#or
res = list(filter(int,[1,0,3,False,5,6.7, True]))
print(res) ## [1, 3, 5, 6.7, True]

print(int(True))# 1
print(int(False))# 0
print(int(0)) # 0

'''                             | bool(int(value))
| Original Value | `int(value)` | Truthy/Falsy | Kept? |
| -------------- | ------------ | ------------ | ----- |
| `1`            | `1`          | Truthy       | ✅     |
| `3`            | `3`          | Truthy       | ✅     |
| `0`            | `0`          | Falsy        | ❌     |
| `True`         | `1`          | Truthy       | ✅     |
| `False`        | `0`          | Falsy        | ❌     |
| `9`            | `9`          | Truthy       | ✅     |
| `6.7`          | `6`          | Truthy       | ✅     |

'''


## que.3
data = ["", "Python", " ", "Django"]

print(list(filter(bool, data)))  # ['Python', ' ', 'Django']
print(bool("")) # False
print(bool(" ")) # True
print(bool(0))  # False

