'''
Decorators: Decorators are functions that modify the behaviour of another function without changing its actual code.
        --> Decorators follows bottom-up approach. 
'''

def my_decorator(func):   ## func = say_hello
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper    ## say_hello = wrapper

@my_decorator            # Internally : say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()


'''
                 @my_decorator
                       │
                       ▼
      say_hello = my_decorator(say_hello)
                       │
                       ▼
              my_decorator(func)
                       │
         func = original say_hello
                       │
                       ▼
             return wrapper
                       │
                       ▼
        say_hello now points to wrapper
                       │
                       ▼
               say_hello()
                       │
                       ▼
                  wrapper()
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
 print("Before")     func()      print("After")
                         │
                         ▼
               original say_hello()
                         │
                         ▼
                 print("Hello!")
                 
'''
#### ------------------------------------------------
'''
1. Without a decorator:
                Order Pizza
                     ↓
                Get Pizza
                
2 . with a Decorator:
                    Order Pizza
                           ↓
                    Decorator adds Cheese 
                           ↓
                    Decorator adds Sauce 
                         ↓
                    Get Better Pizza

'''            
