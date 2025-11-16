import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(("192.168.50.196", 8080))
tcp_client.send("測試".encode("gbk"))
tcp_client.send(f"{tcp_client}".encode())
recv_data = tcp_client.recv(1024)
print(recv_data)
tcp_client.close()
