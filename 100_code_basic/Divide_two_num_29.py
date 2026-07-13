
## very slow for leetcode  TC = o(dividend/divisor), SC = o(1)
# def divide( dividend: int, divisor: int):

#         negative = False

#         if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
#             negative = True

#         if dividend < 0:
#             dividend = -dividend

#         if divisor < 0:
#             divisor = -divisor

#         quotient = 0

#         while dividend >= divisor:
#             dividend -= divisor
#             quotient += 1

#         if negative:
#             return -quotient

#         return quotient
    
# print(divide(10,3))
# print(divide(7,-3))
# print(divide(-2147483648,-1))
# print(divide(10,0))
# print(divide(1,-1))
# print(divide(-1,-1))

###############--------------------------
### Optimal obj
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Find sign of answer
        negative = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            negative = True

        # Convert to positive without abs()
        if dividend < 0:
            dividend = -dividend

        if divisor < 0:
            divisor = -divisor

        quotient = 0

        while dividend >= divisor:

            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp = temp << 1
                multiple = multiple << 1

            dividend -= temp
            quotient += multiple

        if negative:
            return -quotient

        return quotient
obj = Solution()    
print(obj.divide(10,3))
print(obj.divide(7,-3))
print(obj.divide(-2147483648,-1))  
print(obj.divide(10,0))
print(obj.divide(1,-1))
print(obj.divide(-1,-1))


"""
Left Shift (<<):
- Shifts all bits to the left.
- Multiplies the number by 2.

Example:
5 << 1 = 10 ==> 5*2 = 10
5 << 2 = 20 ==> 5*2*2 = 20
5 << 3 = 40

Right Shift (>>):
- Shifts all bits to the right.
- Divides the number by 2.

Example:
20 >> 1 = 10 ==> 20/2 = 10
20 >> 2 = 5
40 >> 3 = 5

Approach:
1. Convert both numbers to positive and store the final sign.
2. Use left shift (<<) to repeatedly double the divisor.
3. Find the largest multiple less than or equal to the dividend.
4. Subtract it from the dividend and add the multiple to the quotient.
5. Repeat until dividend < divisor, then return the quotient with the correct sign.

Time Complexity: O((log n)^2)
Space Complexity: O(1)
"""



