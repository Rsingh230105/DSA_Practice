
def convertToTitle( columnNumber: int) -> str:
    ans = ""

    while columnNumber > 0:
        columnNumber -= 1
        rem = columnNumber % 26
        ans = chr(ord('A') + rem) + ans
        columnNumber //= 26

    return ans
    
print(convertToTitle(28))
print(convertToTitle(701))
print(convertToTitle(702))
print(convertToTitle(703))
print(convertToTitle(704))