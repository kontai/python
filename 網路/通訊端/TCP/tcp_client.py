from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 4096

print('Staring the clent at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'Hey!')
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
client.close()
