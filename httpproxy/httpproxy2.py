#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import urlparse

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8080              # Arbitrary non-privileged port


def server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
        #     return
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
    print "%s %s" % (method, full_path)
    (scm, netloc, path, params, query, fragment) \
        = urlparse.urlparse(full_path, 'http')
    # ���url���С�������ָ���˿ڣ�û����ΪĬ��80�˿�
    i = netloc.find(':')
    if i >= 0:
        address = netloc[:i], int(netloc[i + 1:])
    else:
        address = netloc, 80
    return method, version, scm, address, path, params, query, fragment


def handle_connection(conn):
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