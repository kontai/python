from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 4096

print('Starting the server at', datetime.now())
print('Wating for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
# 將5個用戶端連結排入序列,並拒絕新來的
server.listen(5)

# 接收訊息
client, addr = server.accept()
# 將最大接收訊息設為1,000byte
data = client.recv(max_size)

print('At', datetime.now(), client, 'said', data)
client.sendall(b'Are you talking to me?')
client.close()
server.close()
