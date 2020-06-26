import socket
from threading import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()  #for two machines use ip address or in as it is for server and client in same machine
PORT = 12348  # use port from 1000 to 56300 any

s.bind((HOST_NAME, PORT))
s.listen(5)  # listen 5 clients
client, address = s.accept()

class server_send(Thread):    #send massages

    def run(self):  # run function(import from threading)run or call both run parallel
        while True:
            client.send(bytes(str(input()), "utf-8"))

class server_receive(Thread):  #receive massages

    def run(self):  # this run function run parallel also
        while True:
            msg = client.recv(1024).decode("utf-8")
            print("client: "+msg)


s1 = server_send()  #call send class
s2 = server_receive()  # call receive class
s2.start()  # run(start) function in send
s1.start()  # run function in receive