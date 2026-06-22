'''
Input: "A man, a plan, a canal: Panama!!" → Output: True
Input: "race a car" → 
'''
## method 1
def is_palindrome(s):
    clean = ""
    for c in s:
        if c.isalnum():
            clean += c.lower()
    return clean == clean[::-1]

print(is_palindrome("A man, a plan, a canal: Panama!!"))


## method 2
# Two pointer approach (O(1) space)
def is_palindrome_v2(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum(): 
            l += 1
        while l < r and not s[r].isalnum(): 
            r -= 1
        if s[l].lower() != s[r].lower(): 
            return False
        l += 1
        r -= 1
    return True

is_palindrome_v2("race a car")