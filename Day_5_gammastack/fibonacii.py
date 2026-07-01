## best method iterative DP o(1) space
def fib(n):
    p,q = 0,1
    for _ in range(n):
        p, q = q, p+q
        
    return p
    
print(fib(10))

### basic recursion method 2
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
   