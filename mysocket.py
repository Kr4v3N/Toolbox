# coding: utf-8
import socket

import threading
# from urllib import response
from urllib3 import response

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

bind_ip = "0.0.0.0"
bind_port = 41577

server.bind((bind_ip, bind_port))
server.listen(5)

print(("[+] Listening on address %s and port %d" % (bind_ip, bind_port)))
(client, (ip, port)) = server.accept()

print(("Client IP is : %s " % ip))
print(("Client remote port is : %s" % port))

data = 'noob'

while len(data):
    data = client.recv(2048)
    print("Client sent :", data)
    client.send(b'response')

print("Closing the connections ")
client.close()
print("Shutting down the server ")
server.close()
