def fib(n):
    p,q = 0,1
    
    while p<n:
        yield p
        p,q = q,p+q
        
x = fib(10)

for i in x:
    print(i)
    
# Fibonacci generator:

# Time Complexity: O(n) (each Fibonacci number is generated once until the limit)
# Space Complexity: O(1) extra space (only a few variables like p and q are stored)
# return → Gives everything at once and ends the function.
# yield → Gives one value at a time, pauses, and continues later.

'''
fib(10)
     │
     ▼
Generator Object
     │
     ▼
for loop
     │
     ▼
yield 0
     │
(paused)
     │
next()
     │
     ▼
yield 1
     │
(paused)
     │
next()
     │
     ▼
yield 1

'''
#### --------------------------------------
'''
Real-Life Example
Example 1: YouTube Videos 

Imagine YouTube has 1 million videos.

Without a generator:

Load all 1 million videos
↓
Very slow
↓
High memory usage

#----------------------

With a generator:
Load Video 1
↓
User watches
↓
Load Video 2
↓
User watches
↓
Load Video 3
'''
