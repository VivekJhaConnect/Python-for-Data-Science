# Import Thred class
from threading import Thread, current_thread

# Create a finction containing code to be executed parallaly
def display(n, msg):
    print(current_thread())
    for i in range(n):
        print(msg)

# Create new thread Here
# t1 = Thread(target=display, kwargs={'n':4,'msg': 'Hello World'})
t1 = Thread(target=display, args=(4,'Hello World'))

# Start the new thread
t1.start()

# Thread name and Details


for i in range(4):
    print("Welcome")