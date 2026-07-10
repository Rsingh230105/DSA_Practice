## 3754. Concatenate Non-Zero Digits and Multiply by Sum
## Method 1
## TC = o(n**2)
## SC = o(n)
def sumAndmultiply(n):
    res = ""
    total = 0
    
    for i in str(n):
        if int(i) != 0:
            res += i
            total += int(i)
    return int(res)*total
    
print(sumAndmultiply(10203004))
print(sumAndmultiply(1000))

## method 2 # Optimal
## TC = o(n)
## SC = o(n)
'''
--> d: number of digits in n
1. str(n) → O(d)
2. Loop → O(d)
3. "".join(digits) → O(d)
4. int(res) conversion → O(d)
5. int(i: single value)-> o(1)
'''

def sumAndMultiply1(self, n: int) -> int:
        if n == 0:
            return 0

        digits = []
        total = 0

        for ch in str(n):
            if ch != '0':
                digits.append(ch)
                total += int(ch)
        return int(''.join(digits)) * total