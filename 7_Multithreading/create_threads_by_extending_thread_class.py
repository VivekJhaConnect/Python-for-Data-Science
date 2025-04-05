from threading import Thread
from time import sleep

videos = ['OP Syllabus', 'constructor', 'destructor','file handling']
class MyThread(Thread):
    def __init__(self, val):
        print("constructor called")
        self.kid = val
        Thread.__init__(self)

    def compression(self):
        print("Video compression code.")

    def run(self):
        self.compression()
        if self.val:
            print("Suitable for kids.")
        for video in videos:
            print(f"{video} started uploading...")
            sleep(3)
            print(f"{video} uploading.")

t1 = MyThread(False)
t1.start()

for i in range(4):
    sleep(0.5)
    print("Checking Copyrights")