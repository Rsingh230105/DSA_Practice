class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i>=0 or j>=0 or carry:
            if i>=0:
                carry += int(a[i])
                i -= 1
            if j>=0:
                carry += int(b[j])
                j -= 1

            s.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(s))

obj = Solution()
print(obj.addBinary("11","1"))
print(obj.addBinary("1010","1011"))

'''
1. Add the current bits from right to left.
2. Include any carry from the previous step.
3. Store the current result bit (carry % 2).
4. Compute the new carry (carry // 2).
5. Continue until all bits and the final carry are processed.
'''
#TC = o(N)
# SC = o(N)