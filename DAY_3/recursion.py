## recursion 987 recursion one time

## print  Queen 10 times
## using head recursion

# def func(count):
#     if count == 10:
#         return 
#     print("Queen") # first print 
#     func(count + 1) # than call

# func(0)

### Tail recursion : first call funtion

def func(count):
    if count == 10:
        return
    count += 1
    func(count)
    print("Queen")

func(0)
        