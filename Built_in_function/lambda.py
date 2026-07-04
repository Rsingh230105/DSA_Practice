'''
syntax : lambda arguments: expression
lambda → Keyword
arguments → Input parameters
expression → Returns the result automatically (no return keyword)

Time Complexity

A lambda function itself doesn't have a fixed time complexity. Its complexity depends on the expression inside it.

Examples:

lambda x: x*x → O(1)
map(lambda x: x*2, nums) → O(n)
filter(lambda x: x>0, nums) → O(n)
sorted(data, key=lambda x: x["age"]) → Overall sorting is O(n log n)
'''
## Normal Function
def square(x):
    return x * x

print(square(5))

## 1. lambda function : with on argument
square = lambda x: x * x

print(square(5))


## 2. with two argument
mul = lambda a,b : a*b
print(mul(2,3))

## Type 3 : Wrapping lambda function inside another function

def myWrapper(n): # n =5
    return lambda a:a*n # a = a * 5

mul = myWrapper(5) 
print(mul(2)) # a = 2 * 5 => 10


## 4. with condition: Odd and Even
even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(even(10))
print(even(5))


## 5. lambda with map()
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)

## 6. lambda with filter
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

## 7.  lambda with sorted()
students = [
    {"name": "Raj", "age": 22},
    {"name": "Ram", "age": 20},
    {"name": "Amit", "age": 24},
]

result = sorted(students, key=lambda x: x["age"])

print(result)

