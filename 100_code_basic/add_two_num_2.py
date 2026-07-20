

def add_two_number(l1, l2):
    op = []
    carry = 0

    i = len(l1) - 1
    j = len(l2) - 1

    while i >= 0 or j >= 0 or carry:

        x = l1[i] if i >= 0 else 0
        y = l2[j] if j >= 0 else 0

        total = x + y + carry

        op.append(total % 10)

        carry = total // 10

        i -= 1
        j -= 1

    

    return op


print(add_two_number([2,4,3],[5,6,4]))
print(add_two_number([0],[0]))
print(add_two_number([9,9,9,9,9,9,9],[9,9,9,9]))

'''
Problem:
--------
Given two arrays where each element represents a digit of a number,
add the two numbers and return the result as a new array.

Example:
Input:
l1 = [2, 4, 3]
l2 = [5, 6, 4]

243 + 564 = 807

Output:
[8, 0, 7]


Approach:
---------
1. Start from the last index of both arrays because addition always
   begins from the rightmost digit.
2. Initialize a carry variable with 0.
3. Add the current digits and the carry.
4. Store only the last digit (total % 10).
5. Update carry using total // 10.
6. Move both pointers to the left.
7. Continue until both arrays are processed and carry becomes 0.
8. Reverse the result because digits were added from right to left.


Algorithm:
----------
- Initialize:
    i = len(l1) - 1
    j = len(l2) - 1
    carry = 0
    result = []

- Repeat while:
    i >= 0 or j >= 0 or carry

- Get current digits:
    x = l1[i] if i >= 0 else 0
    y = l2[j] if j >= 0 else 0

- Compute:
    total = x + y + carry

- Store digit:
    result.append(total % 10)

- Update carry:
    carry = total // 10

- Move pointers:
    i -= 1
    j -= 1

- Reverse the result and return.


Dry Run:
--------
l1 = [2,4,3]
l2 = [5,6,4]

Step 1:
3 + 4 + 0 = 7
result = [7]
carry = 0

Step 2:
4 + 6 + 0 = 10
result = [7,0]
carry = 1

Step 3:
2 + 5 + 1 = 8
result = [7,0,8]
carry = 0

Reverse:
[8,0,7]


Time Complexity:
----------------
Let:
n = len(l1)
m = len(l2)

Loop:
O(max(n,m))

Reverse:
O(max(n,m))

Total:
O(max(n,m))


Space Complexity:
-----------------
The output array stores at most
max(n,m)+1 digits.

Space Complexity:
O(max(n,m))


Why This Solution?
------------------
- Works for arrays of different lengths.
- Correctly handles carry.
- Traverses each array only once.
- Uses an optimal O(n) approach.
- Easy to understand and suitable for coding interviews.

'''


####-----------------------------------------------------------------------########
#### Leetcode Solution ############
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry

            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next