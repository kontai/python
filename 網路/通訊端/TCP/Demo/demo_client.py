import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))
print('已連接至服務端.')
while True:
    send_msg = input(">>>").strip()
    client.send(send_msg.encode('utf-8'))
    receive_msg = client.recv(1024).decode('utf-8')
    print(receive_msg)
client.close()
