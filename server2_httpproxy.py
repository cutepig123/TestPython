# Socket server in python using select function
# Issues
# * thread.start_new_thread no work 
# * No work in some sites, like qq.com. it will pops up "type not correct"
# * No work in newsmth
# * No work in https?
# * select no work iif >512 connections

import socket, select
import urllib2
import thread
  
def getData(url):
	try:
		return urllib2.urlopen(url).read()
	except:
		return ''
	
def clientthread(sock):
	datas=''
	while 1:
		data = sock.recv(RECV_BUFFER)
		datas =datas+(data)
		
		# echo back the client message
		if not data:break
		if '\n' in data:break
	
	p =datas.find('\r\n')
	if p>0:
		url =datas[:p].split()[1]
		print url
		res =getData(url)
		sock.send(res+'\r\n\r\n')
	
		
if __name__ == "__main__":
	  
	CONNECTION_LIST = []	# list of socket clients
	RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
	PORT = 5000
		 
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# this has no effect, why ?
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(("0.0.0.0", PORT))
	server_socket.listen(10)
 
	# Add server socket to the list of readable connections
	CONNECTION_LIST.append(server_socket)
 
	print "Chat server started on port " + str(PORT)
 
	while 1:
		# Get the list sockets which are ready to be read through select
		read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
		for sock in read_sockets:
			 
			#New connection
			if sock == server_socket:
				# Handle the case in which there is a new connection recieved through server_socket
				sockfd, addr = server_socket.accept()
				CONNECTION_LIST.append(sockfd)
				print "Client (%s, %s) connected" % addr
				 
			#Some incoming message from a client
			else:
				#thread.start_new_thread(clientthread ,(sock,))
				clientthread(sock)	
				#else:
				#	print 'Error', datas
				#sock.send('OK ... ' + datas)
			 
				# client disconnected, so remove from socket list
				sock.close()
				CONNECTION_LIST.remove(sock)
		 
	server_socket.close()