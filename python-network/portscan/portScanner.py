import socket
import threading
from queue import Queue

target = ''
queue = Queue()
openPorts = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False

def fillQueue(portList):
    for port in portList:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Post {} is Open".format(port))
            openPorts.append(port)
    

portList = range(1, 1074)

fillQueue(portList)

threadList = []

for t in range(10):
    thread = threading.Thread(target=worker)
    threadList.append(thread)

for thread in threadList:
    thread.start()

for thread in threadList:
    thread.join()

print("Open ports are: ", openPorts)

