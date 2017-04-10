import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"
port = 9999
listening_q = 5

serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.sock = socket
        # self.addr = address
        self.start()

    def run(self):
        while 1:
            print "Client sent: %s" % self.sock.recv(1024).decode()
            self.sock.send("Data recieved")


serversocket.listen(listening_q)

print "[+] New TCP Server Listening: %s port %d " % (host, port)
while 1:
    clientsocket = serversocket.accept()
    client(clientsocket)