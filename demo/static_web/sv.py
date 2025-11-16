import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(("", 9000))
tcp_socket.listen()
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)


def main():
    while True:
        new_socket, addr = tcp_socket.accept()
        print(f"server start {addr}")

        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
            new_socket.close()
            return
        recv_data = recv_data.decode()
        recv_path = recv_data.split()[1]

        if recv_path == '/':
            recv_path = '/index.html'
        with open("static" + recv_path, 'rb') as file:
            file_data = file.read()
            res_line = "HTTP/1.1 200 OK\r\n"
            res_header = "server: TSW\r\n"
            res_body = file_data

            response = (res_line + res_header + '\r\n').encode() + res_body
            new_socket.send(response)


if __name__ == '__main__':
    main()
