## Parameter: A parameter is a variable written in the function definition that receives a value when the function is called.

def greet(name):   # name is a parameter
    print("Hello", name)


## Argument :An argument is the actual value passed to a function when calling it.

# greet("Raj")
# Here, "Raj" is the argument.


# def argument(a,b,*args):  ## a, b is a Parameter
#     return a+b+sum(args)

# print(argument(1,2,3,4,5)) ## 1,2,3,.. is a argument

## EX: 2
def add(*args):
    total = 0

    for num in args:
        total += num

    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))