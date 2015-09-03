import socket, os

class Server:
    def __init__(self):
        self.host, self.port = 'localhost', 8080
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        print "Init OK"
        
		
    def send(self, msg):
        if type(msg) == str: self.conn.send(msg )
        elif type(msg) == list or tuple: self.conn.send('\n'.join(msg) )

    def recv(self):
        print "recv:", self.conn.recv(4096).strip()
        self.send("OK")
		
    def exit(self):
        self.send('Disconnecting you...'); self.conn.close(); self.run()
        # closing a connection, opening a new one

    # main runtime
    def run(self):
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
        self.send("OK")
        # there would be more activity here
        # i.e.: sending things to the connection we just made


S = Server()
S.run()
