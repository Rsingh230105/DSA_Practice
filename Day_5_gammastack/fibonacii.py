def fib(n):
    p,q = 0,1
    for _ in range(n):
        p, q = q, p+q
        
    return p
    
print(fib(10))
   