num = int(input("Enter digit:"))
n = str(num)
rev = 0

while num > 0:
    ld = num % 10
    rev = rev * 10 + ld
    num =num // 10
    
if rev == int(n):
    print("Palindrome")
else:
    print("Not Palindrome")

