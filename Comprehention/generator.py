# syntax : (expression for item in iterable)
numbers = [1,2,3,4]
square = (i*i for i in numbers)
print(square) # return generator object
# SO
for i in square:
    print(i)

## if - else comprehention
numbers = [1,2,3,4,5]
result = ["Even" if i%2==0 else "Odd" for i in numbers]
print(result)