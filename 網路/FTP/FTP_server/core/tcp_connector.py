import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('ok')