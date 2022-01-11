import urllib.request as ur
url = 'https://www.programmableweb.com/api/i-heart-quotes-rest-api'
conn = ur.urlopen(url)
# print(conn.info())
print(conn)
print(conn.status)
print(conn.getheader('Content-Type'))
for key, values in conn.getheaders():
    print(key,values)
# print(conn.read())