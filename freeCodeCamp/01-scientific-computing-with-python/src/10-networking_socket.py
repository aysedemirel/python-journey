import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mySocket.send(cmd)

while True:
    data = mySocket.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mySocket.close()

# a simple web browser
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

print(ord('A')) # print ascii number of 'A'

# UTF-16 : Fixed length - two bytes
# UTF-32 : Fixed length - four bytes
# UTF-8  : 1-4 bytes, recommended practice for encoding data to be exchanged between systems
# UTF-8 is a type of encoding do most website use.
byte_x = b'abc'
print(type(byte_x))