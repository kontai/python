import optparse
from conf import setup
import socketserver
from core import tcp_connector

class ARGVProcess:
    def __init__(self):
        self.parser = optparse.OptionParser()
        # self.parser.add_option('-s', '--server', dest='server')
        # self.parser.add_option('-p', '--port', dest='port')
        options, msg = self.parser.parse_args()
        self.verify_args(options, msg)


    def verify_args(self, option, msg):
        if hasattr(self, msg[0]):
            func = getattr(self, msg[0])
            func(setup.ip, setup.port)
        else:
            print('指令找不到:', msg)


    def start(self, ip, port):
        s = socketserver.ThreadingTCPServer((ip, port), tcp_connector.MyServer)
        s.serve_forever()
        

    def help(self):
        pass


    def close(self):
        pass
    # print(sys.argv[1])
