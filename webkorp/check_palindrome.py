## TC = o(n**2), SC = o(n)
def check_palindrome(s):
    s1 = s
    s2 = ""
    for ch in s1:
        s2 = ch + s2
        
    return s1 == s2

print(check_palindrome("racecar"))
print(check_palindrome("hello"))
print(check_palindrome("madam"))
print(check_palindrome("level"))

## better solution(optimal)
def check_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
