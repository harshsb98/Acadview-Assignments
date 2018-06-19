from threading import Thread
import time
import threading

class mythread(threading.Thread):
    def run(self):
        print("Threading")
M=mythread()
time.sleep(5)
M.start()

class mythreads(threading.Thread):
    def __init__(self,i):
        print(i)

for i in range(10):
    time.sleep(1)
    x = mythreads(i)

l = [2, 4, 6, 8, 10]
class thred(threading.Thread):
    def __init__(self,i):
        print(i)
for i in l:
    time.sleep(i)
    t=thred(i)

class thread(threading.Thread):
    def fact(self,f):
        if(f==1):
            return 1
        else:
            return f*v.fact(f-1)
v=thread()
z=int(input("Enter any no. for factorial"))
print(v.fact(z))

