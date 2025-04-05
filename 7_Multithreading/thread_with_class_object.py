# Threads for methods
from threading import Thread

class Example:
    def display(self):
        for i in range(5):
            print("Hello World")

    @staticmethod
    def display_more():
        for i in range(5):
            print("Hello World More")

e1 = Example()
t1 = Thread(target=e1.display)
t1 = Thread(target=e1.display_more)
t1.start()

for i in range(5):
    print("Welcome")