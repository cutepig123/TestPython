#coding=utf-8

import smtplib
import string
import base64

#�������أ�������

#"""
#�����ʼ���SMTP����֤��ʽΪ��LOGIN
#����һ�ֽϳ����ķ�ʽ��PLAIN����LOGIN���ƵĲ�֮ͬ������һ���������˺ź����룬
#��ʽΪ��<NUL>�˺�<NUL>���롱������<NUL>Ϊ�ֽ�0����֤����:
#username = base64.encodestring("<NUL>wudiboy<NUL>XXXXXXXX")
#
#"""

fromaddr = "hjs00@126.com"
toaddrs  = fromaddr

print('# Add the From: and To: headers at the start!')
msg = "From: %s\r\nTo: %s\r\nSubject: ����\r\n\r\n"%(fromaddr, toaddrs)
msg = msg + "�����ʼ������ݲ���\r\n"

print('start connect.')
mailserver = "smtp.126.com"
server = smtplib.SMTP(mailserver)

server.set_debuglevel(1)

print('authing.')
username = base64.encodestring("hjs00")
password = base64.encodestring("a0315734068")
server.ehlo(name=mailserver)
server.docmd("AUTH","LOGIN")
server.docmd(username,)
server.docmd(password,)

print('send mail.')
server.sendmail(fromaddr, toaddrs, msg)
server.quit()