numbers = [1, 2, 3, 4, 5]

square = []

for i in numbers:
    square.append(i*i)

print(square)## without comprehention

#-------------------------------------

# syntax : [exp. for item in iterable]
# with comprehention

l = [1,2,3,4,5]
square = [i*i for i in l]
print(square)

## with condition
numbers = [1,2,3,4,5,6]
even = [i for i in numbers if i%2==0]
print(even)


