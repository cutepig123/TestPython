#!/bin/sh -
"exec" "python" "-O" "$0" "$@"

__doc__ = """Tiny HTTP Proxy.

This module implements GET, HEAD, POST, PUT and DELETE methods
on BaseHTTPServer, and behaves as an HTTP proxy.  The CONNECT
method is also implemented experimentally, but has not been
tested yet.

Any help will be greatly appreciated.		SUZUKI Hisao
"""

__version__ = "0.2.1"

import BaseHTTPServer, select, socket, SocketServer, urlparse

class ProxyHandler (BaseHTTPServer.BaseHTTPRequestHandler):
	__base = BaseHTTPServer.BaseHTTPRequestHandler
	__base_handle = __base.handle

	server_version = "TinyHTTPProxy/" + __version__
	rbufsize = 0						# self.rfile Be unbuffered
	parent_proxy = "aaants10.aaaex.asmpt.com:80"
	
	def handle(self):
		print "handle"
		(ip, port) =  self.client_address
		print self.client_address
		if 1:	#hasattr(self, 'allowed_clients') and ip not in self.allowed_clients:
			raw_requestline = self.rfile.readline()
			print raw_requestline
			#if self.parse_request(): self.send_error(403)
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			#try:
			if 1:
				print "\t ***_connect_to", self.parent_proxy
				if self._connect_to(self.parent_proxy, soc):
					print "_connect_to OK"
					#self.log_request(200)
					soc.send(raw_requestline)
					#self.log_request(200)	#Crash
					self.wfile.write(self.protocol_version +
									 " 200 Connection established\r\n")
					self.wfile.write("Proxy-agent: %s\r\n" % self.version_string())
					self.wfile.write("\r\n")
					self._read_write(soc, 300)
			#finally:
				print "\t" "bye"
				soc.close()
				self.connection.close()
		#else:
		#	self.__base_handle()

	#netloc the address:ip of real server
	def _connect_to(self, netloc, soc):
		i = netloc.find(':')
		if i >= 0:
			host_port = netloc[:i], int(netloc[i+1:])
		else:
			host_port = netloc, 80
		print "\t" "connect to %s:%d" % host_port
		#try: 
		soc.connect(host_port)
		#except socket.error, arg:
		#	try: msg = arg[1]
		#	except: msg = arg
		#	self.send_error(404, msg)
		#	return 0
		return 1

	#read from real server, and then send the reply to client
	def _read_write(self, soc, max_idling=20):
		iw = [self.connection, soc]
		ow = []
		count = 0
		while 1:
			count += 1
			(ins, _, exs) = select.select(iw, ow, iw, 3)
			if exs: break
			if ins:
				for i in ins:
					if i is soc:
						out = self.connection
					else:
						out = soc
					data = i.recv(8192)
					if data:
						out.send(data)
						count = 0
			else:
				print "\t" "idle", count
			if count == max_idling: break

class ThreadingHTTPServer (SocketServer.ThreadingMixIn,
						   BaseHTTPServer.HTTPServer): pass

if __name__ == '__main__':
	from sys import argv
	if argv[1:] and argv[1] in ('-h', '--help'):
		print argv[0], "[port [allowed_client_name ...]]"
	else:
		if argv[2:]:
			allowed = []
			for name in argv[2:]:
				client = socket.gethostbyname(name)
				allowed.append(client)
				print "Accept: %s (%s)" % (client, name)
			ProxyHandler.allowed_clients = allowed
			del argv[2:]
		else:
			print "Any clients will be served..."
		BaseHTTPServer.test(ProxyHandler, ThreadingHTTPServer)
