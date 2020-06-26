import socket
from threading import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12348

s.connect((HOST_NAME, PORT))
print("connected")

class client_send(Thread):
    def run(self):
        while True:
            s.send(bytes(str(input()), "utf-8"))

class client_receive(Thread):
    def run(self):
        while True:
            msg = s.recv(1024).decode("utf-8")
            print("server: "+msg)


c1 = client_send()
c2 = client_receive()
c1.start()
c2.start()