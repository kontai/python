from socket import *
client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect(('localhost',8080))
import sys

while True:
    data=input('>>>')
    client_socket.send(data.encode('utf-8'))
    receive=client_socket.recv(1024)
    print(receive)