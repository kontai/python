import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1', 9999))
server.listen(5)  # backlog

while True:
    print('服務器運行了.')
    conn, addr = server.accept()
    print('雙向鏈接:', conn)
    print('客戶端地址:', addr)

    while True:
        print("正在等待接收資料....")
        msg = conn.recv(2048)
        if not msg:
            break
        receive_msg = msg.decode('utf-8')
        print('>>', receive_msg)
        conn.send(receive_msg.upper().encode('utf-8'))

conn.close()
server.close()
