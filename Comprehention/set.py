## syntax : {expression for item in iterable}

numbers = [1,2,2,3,3,4]
result = {i for i in numbers}
print(result)

## 2.
numbers = [1,2,3,4]
square = {i*i for i in numbers}
print(square)