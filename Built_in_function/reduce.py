'''
--> reduce(function, iterable)

--> reduce() function applies a function repeatedly on iterable elements and return a single final value.
--> Require module: from functools import reduce

--> Time Complexity:  O(n)  (it processes each element once)
    Space Complexity: O(1)   extra space (ignoring the input iterable and function call overhead)
'''
from functools import reduce

numbers = [1,2,3,4,5,6]
res = reduce(lambda x,y:x+y,numbers)
print(res) # 21

## maximum find using reduce

numbers = [10, 45, 22, 89, 31]

result = reduce(lambda x, y: x if x > y else y, numbers)

print(result)