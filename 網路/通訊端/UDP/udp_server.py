from datetime import datetime
import socket

server_address = ('localhost', 6789)
max_size = 4096

print('Starting the server at', datetime.now())
print('Waiting for a client to call.')

# 建立通訊端  AF_INET(建立internet(IP)通訊端,SOCK_DGRAM(UDP-傳送接收包)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 連結
server.bind(server_address)

data, client = server.recvfrom(max_size)

print('At', datetime.now(), client, 'said', data)
server.sendto(b'Are you talking to me?', client)
server.close()
