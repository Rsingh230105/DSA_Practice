try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = a / b
except ZeroDivisionError:
    print("Can't  divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("Result:",c)
finally:
    print("Program executed successfully")
    
    
t = (1,2,3,4)
print(t[0:2])

s = {1:1,2:2,3:3,4:4}
print(s[2])