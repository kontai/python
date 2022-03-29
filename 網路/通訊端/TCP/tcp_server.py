from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 4096

print('Starting the server at', datetime.now())
print('Wating for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
'''
当socket关闭后，本地端用于该socket的端口号立刻就可以被重用。通常来说，只有经过系统定义一段时间后，才能被重用。
用法:
    S.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 这里value设置为1，表示将SO_REUSEADDR标记为TRUE，操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口。

'''
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
