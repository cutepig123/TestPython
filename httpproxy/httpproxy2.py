#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import urlparse
import pdb

HOST = ''				 # Symbolic name meaning all available interfaces
PORT = 8080			  # Arbitrary non-privileged port
BUFSZ = 8192

def server(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)	#What is the usage? Seems still can work even comment it
	s.bind((host, port))
	s.listen(500)
	print "Serving at %s" % PORT
	while 1:
		try:
			conn, addr = s.accept()
			handle_connection(conn)
		except KeyboardInterrupt:
			print "Bye..."
			break


def getline(conn):
	line = ''
	while 1:
		buf = conn.recv(1)
		if buf == '\r':
			line += buf
			buf = conn.recv(1)
			if buf == '\n':
				line += buf
				return line
		# elif buf == '':
		#	 return
		else:
			line += buf


def get_header(conn):
	'''
	不包括\r\n
	'''
	headers = ''
	while 1:
		line = getline(conn)
		if line is None:
			break
		if line == '\r\n':
			break
		else:
			headers += line
	return headers


def parse_header(raw_headers):
	request_lines = raw_headers.split('\r\n')
	first_line = request_lines[0].split(' ')
	method = first_line[0]
	full_path = first_line[1]
	version = first_line[2]
	
	#pdb.set_trace()
	if full_path.lower().find('http://')<0 and full_path.lower().find('https://')<0:
		full_path =''.join(['//',full_path])
	print "%s %s" % (method, full_path)
	
	#urlmode ='http'
	#if method == 'CONNECT':
	#	urlmode='https'
	
	(scm, netloc, path, params, query, fragment) \
		= urlparse.urlparse(full_path)
	if len(path)==0:
		path='/'
		#= urlparse.urlparse(full_path, urlmode)
	# 如果url中有‘：’就指定端口，没有则为默认80端口
	i = netloc.find(':')
	if i >= 0:
		address = netloc[:i], int(netloc[i + 1:])
	else:
		address = netloc, 80
	return method, version, scm, address, path, params, query, fragment


def handle_connection_old(conn):
	# 从socket读取头
	req_headers = get_header(conn)
	# 更改HTTP头
	## 要没有HTTP头的话。。。
	if req_headers is None:
		return
	method, version, scm, address, path, params, query, fragment = \
		parse_header(req_headers)
	path = urlparse.urlunparse(("", "", path, params, query, ""))
	req_headers = " ".join([method, path, version]) + "\r\n" +\
		"\r\n".join(req_headers.split('\r\n')[1:])
	# 建立socket用以连接URL指定的机器
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# soc.settimeout(1)
	# 尝试连接
	try:
		soc.connect(address)
	except socket.error, arg:
		conn.sendall("HTTP/1.1" + str(arg[0]) + " Fail\r\n\r\n")
		conn.close()
		soc.close()
	else:  # 若连接成功
		# 把HTTP头中连接设置为中断
		# 如果不想让火狐卡在那里不继续加载的话
		if req_headers.find('Connection') >= 0:
			req_headers = req_headers.replace('keep-alive', 'close')
		else:
			req_headers += req_headers + 'Connection: close\r\n'
		# 发送形如`GET path/params/query HTTP/1.1`
		# 结束HTTP头
		req_headers += '\r\n'
		soc.sendall(req_headers)
		# 发送完毕, 接下来从soc读取服务器的回复
		# 建立个缓冲区
		data = ''
		while 1:
			try:
				buf = soc.recv(8192)
				data += buf
			except:
				buf = None
			finally:
				if not buf:
					soc.close()
					break
		# 转发给客户端
		conn.sendall(data)
		conn.close()
		
def handle_connection(conn):
	# 从socket读取头
	req_headers = get_header(conn)
	# 更改HTTP头
	## 要没有HTTP头的话。。。
	if req_headers is None:
		return
	method, version, scm, address, path, params, query, fragment = \
		parse_header(req_headers)
	if method == 'GET':
		do_GET(conn,
			   req_headers,
			   address,
			   path,
			   params,
			   query,
			   method,
			   version)
	elif method == 'CONNECT':
		# 注意
		#address = (path.split(':')[0], int(path.split(':')[1]))
		do_CONNECT(conn,
				   req_headers,
				   address)


def do_CONNECT(conn, req_headers, address):
	# 建立socket用以连接URL指定的机器
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# soc.settimeout(4)
	# 尝试连接
	try:
		soc.connect(address)
	except socket.error, arg:
		conn.sendall("/1.1" + str(arg[0]) + " Fail\r\n\r\n")
		conn.close()
		soc.close()
	else:  # 若连接成功
		conn.sendall('HTTP/1.1 200 Connection established\r\n\r\n')
		# 数据缓冲区
		# 读取浏览器给出的消息
		try:
			while True:
				# 从客户端读取数据，并转发给conn
				data = conn.recv(99999)
				soc.sendall(data)
				# 从服务器读取回复，转发回客户端
				data = soc.recv(999999)
				conn.sendall(data)
		except:
			conn.close()
			soc.close()


def do_GET(conn, req_headers, address, path, params, query, method, version):
	path = urlparse.urlunparse(("", "", path, params, query, ""))
	req_headers = " ".join([method, path, version]) + "\r\n" +\
		"\r\n".join(req_headers.split('\r\n')[1:])
	# 建立socket用以连接URL指定的机器
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# soc.settimeout(1)
	# 尝试连接
	try:
		soc.connect(address)
	except socket.error, arg:
		conn.sendall("HTTP/1.1" + str(arg[0]) + " Fail\r\n\r\n")
		conn.close()
		soc.close()
	else:  # 若连接成功
		# 把HTTP头中连接设置为中断
		# 如果不想让火狐卡在那里不继续加载的话
		if req_headers.find('Connection') >= 0:
			req_headers = req_headers.replace('keep-alive', 'close')
		else:
			req_headers += req_headers + 'Connection: close\r\n'
		# 发送形如`GET path/params/query HTTP/1.1`
		# 结束HTTP头
		req_headers += '\r\n'
		soc.sendall(req_headers)
		# 发送完毕, 接下来从soc读取服务器的回复
		# 建立个缓冲区
		data = ''
		while 1:
			try:
				buf = soc.recv(8129)
				data += buf
			except:
				buf = None
			finally:
				if not buf:
					soc.close()
					break
		# 转发给客户端
		conn.sendall(data)
		conn.close()
		
if __name__ == '__main__':
	server(HOST, PORT)