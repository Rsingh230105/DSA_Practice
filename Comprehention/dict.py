## Syntax : {key:value for item in iterable}

numbers = [1,2,3,4]
square = {i:i*i for i in numbers}
print(square)

## with condition
numbers = [1,2,3,4,5]
result = {i:i*i for i in numbers if i%2==0}
print(result)