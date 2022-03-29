import socket

#回傳ip
print(socket.gethostbyname("www.yahoo.com.tw"))

#回傳名稱,一串替代名稱,一串位址
print(socket.gethostbyname_ex("www.yahoo.com.tw"))

print(socket.getaddrinfo("www.yahoo.com.tw",80))

print(socket.getservbyname('http'))
print(socket.getservbyport(80))