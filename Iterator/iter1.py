num = [10,20,30,40,50]
my_iter = iter(num)   ## Internally : __iter__() method call

print(next(my_iter)) # internally : __next__() method , if all element cover than this method call so give STOPITERATION Exception occure.
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))