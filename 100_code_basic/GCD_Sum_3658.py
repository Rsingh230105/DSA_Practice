'''
Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.
'''
'''Loop      : O(n)

GCD       : O(log n)

Total     : O(n + log n)

Since O(n) dominates,

Time Complexity = O(n)

Space Complexity = O(logn)'''


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        sum_even = 0
        sum_odd = 0

        for i in range(1, 2 * n + 1):
            if i % 2 == 0:
                sum_even += i
            else:
                sum_odd += i

        return gcd(sum_even, sum_odd)
    
obj = Solution()
print(obj.gcdOfOddEvenSums(4))
print(obj.gcdOfOddEvenSums(5))


##### optimal 2
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        return gcd(n * n, n * (n + 1))
    

### Time: O(log n)
### Space: O(log n) (recursive GCD) or O(1) if using an iterative GCD.