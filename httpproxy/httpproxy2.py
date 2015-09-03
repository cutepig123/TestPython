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
	������\r\n
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
	# ���url���С�������ָ���˿ڣ�û����ΪĬ��80�˿�
	i = netloc.find(':')
	if i >= 0:
		address = netloc[:i], int(netloc[i + 1:])
	else:
		address = netloc, 80
	return method, version, scm, address, path, params, query, fragment


def handle_connection_old(conn):
	# ��socket��ȡͷ
	req_headers = get_header(conn)
	# ����HTTPͷ
	## Ҫû��HTTPͷ�Ļ�������
	if req_headers is None:
		return
	method, version, scm, address, path, params, query, fragment = \
		parse_header(req_headers)
	path = urlparse.urlunparse(("", "", path, params, query, ""))
	req_headers = " ".join([method, path, version]) + "\r\n" +\
		"\r\n".join(req_headers.split('\r\n')[1:])
	# ����socket��������URLָ���Ļ���
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# soc.settimeout(1)
	# ��������
	try:
		soc.connect(address)
	except socket.error, arg:
		conn.sendall("HTTP/1.1" + str(arg[0]) + " Fail\r\n\r\n")
		conn.close()
		soc.close()
	else:  # �����ӳɹ�
		# ��HTTPͷ����������Ϊ�ж�
		# ��������û���������ﲻ�������صĻ�
		if req_headers.find('Connection') >= 0:
			req_headers = req_headers.replace('keep-alive', 'close')
		else:
			req_headers += req_headers + 'Connection: close\r\n'
		# ��������`GET path/params/query HTTP/1.1`
		# ����HTTPͷ
		req_headers += '\r\n'
		soc.sendall(req_headers)
		# �������, ��������soc��ȡ�������Ļظ�
		# ������������
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
		# ת�����ͻ���
		conn.sendall(data)
		conn.close()
		
def handle_connection(conn):
	# ��socket��ȡͷ
	req_headers = get_header(conn)
	# ����HTTPͷ
	## Ҫû��HTTPͷ�Ļ�������
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
		# ע��
		#address = (path.split(':')[0], int(path.split(':')[1]))
		do_CONNECT(conn,
				   req_headers,
				   address)


def do_CONNECT(conn, req_headers, address):
	# ����socket��������URLָ���Ļ���
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# soc.settimeout(4)
	# ��������
	try:
		soc.connect(address)
	except socket.error, arg:
		conn.sendall("/1.1" + str(arg[0]) + " Fail\r\n\r\n")
		conn.close()
		soc.close()
	else:  # �����ӳɹ�
		conn.sendall('HTTP/1.1 200 Connection established\r\n\r\n')
		# ���ݻ�����
		# ��ȡ�������������Ϣ
		try:
			while True:
				# �ӿͻ��˶�ȡ���ݣ���ת����conn
				data = conn.recv(99999)
				soc.sendall(data)
				# �ӷ�������ȡ�ظ���ת���ؿͻ���
				data = soc.recv(999999)
				conn.sendall(data)
		except:
			conn.close()
			soc.close()


def do_GET(conn, req_headers, address, path, params, query, method, version):
	path = urlparse.urlunparse(("", "", path, params, query, ""))
	req_headers = " ".join([method, path, version]) + "\r\n" +\
		"\r\n".join(req_headers.split('\r\n')[1:])
	# ����socket��������URLָ���Ļ���
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# soc.settimeout(1)
	# ��������
	try:
		soc.connect(address)
	except socket.error, arg:
		conn.sendall("HTTP/1.1" + str(arg[0]) + " Fail\r\n\r\n")
		conn.close()
		soc.close()
	else:  # �����ӳɹ�
		# ��HTTPͷ����������Ϊ�ж�
		# ��������û���������ﲻ�������صĻ�
		if req_headers.find('Connection') >= 0:
			req_headers = req_headers.replace('keep-alive', 'close')
		else:
			req_headers += req_headers + 'Connection: close\r\n'
		# ��������`GET path/params/query HTTP/1.1`
		# ����HTTPͷ
		req_headers += '\r\n'
		soc.sendall(req_headers)
		# �������, ��������soc��ȡ�������Ļظ�
		# ������������
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
		# ת�����ͻ���
		conn.sendall(data)
		conn.close()
		
if __name__ == '__main__':
	server(HOST, PORT)