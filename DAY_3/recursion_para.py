## Recursion using parameters
'''
def func(x,n):
    if n==0:
        return
    print(x)
    func(x,n-1)
    
func(10,5)

## using recursion print 1 to N
## Head recursion
def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)

func(1,4)
'''
## Tail recursion/ Backtracking
def func(i,n):
    if i>n:
        return
    
    func(i+1,n)
    print(i)

func(1,4)
    
