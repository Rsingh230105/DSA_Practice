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
    
    
