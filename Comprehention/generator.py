# syntax : (expression for item in iterable)
numbers = [1,2,3,4]
square = (i*i for i in numbers)
print(square) # return generator object
# SO
for i in square:
    print(i)

##