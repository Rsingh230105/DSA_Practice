# map(function,iterable)
# function : lambda, int, float, str etc.
# iterable : List, Tuple , dict , range , set , string, generator
'''
-> Map is built in python function 
   used to apply a function to every element of 
    an iterable like a list,tuple etc. 
    
-> map() function return new value
'''
l = [1,2,3,4,5]
res = list(map(lambda x:x**2,l))
print(res)

## method 2
l = ["1","2","3","4","5"]
res = list(map(int,l))
print(res)
print(type(res))