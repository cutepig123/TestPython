# Echo client program
import socket
HOST = 'localhost'                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, world'.zfill(1000))
data = s.recv(1024)
s.close()
print 'Received', repr(data)

