import threading

def show():
    print("Thread is Running")
    
t1 = threading.Thread(target = show)
t2 = threading.Thread(target = show)

t1.start()
t2.start()
