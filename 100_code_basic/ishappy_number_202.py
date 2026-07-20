### TC = o(log n)
## SC = o(1)
class Solution:
    def isHappy(self, n: int) -> bool:

        def digit_square_sum(num):
            total = 0

            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10

            return total

        while n != 1 and n != 4:
            n = digit_square_sum(n)

        return n == 1
    
obj = Solution()
print(obj.isHappy(19))
print(obj.isHappy(2)) ## this is special 
print(obj.isHappy(4))

'''
### Why we check `n != 1` and `n != 4`?

In Happy Number, a number can have two outcomes:

1. If the process reaches `1`, the number is Happy.
2. If the number is not Happy, it enters an infinite cycle.

For all unhappy numbers, this cycle always contains `4`.

Example:
2 → 4 → 16 → 37 → 58 → ... → 20 → 4

So we stop the loop when:
- `n == 1` → Happy Number → return True
- `n == 4` → Cycle detected → return False

Condition:
`while n != 1 and n != 4`

means:
"Continue calculating until the number reaches 1 or enters the cycle at 4."
'''
