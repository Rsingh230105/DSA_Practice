'''
Q8: Print Fibonacci Sequence up to N terms
Input: n = 6
Output: [0, 1, 1, 2, 3, 5]
'''

def fib(n):
    fib_seq = []
    a, b = 0, 1

    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b

    return fib_seq

print(fib(6))
    