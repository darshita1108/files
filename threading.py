import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):#when we do not care of variable but just want to loop 10 times we use _
           print(threading.currentThread().getName())


x = Messenger(name="send messages")
y = Messenger(name="received messages")

x.start()#goes to class and loooks for run
y.start()