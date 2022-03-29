import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is:', self.request)  # conn
        print('addr is:', self.client_address)  # addr

        while True:
            try:
                # 收消息
                data = self.request.recv(1024)  # 接收資料
                if not data: break
                print('收到客戶端:', data)
                if data=='quit':break

                # 發消息
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)

if __name__ == '__main__':
    s=socketserver.ThreadingTCPServer(('localhost',8080),MyServer)
    s.serve_forever()
    