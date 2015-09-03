#coding=utf-8

import smtplib
import string
import base64

#不好用呢？？！！

#"""
#新浪邮件的SMTP的认证方式为：LOGIN
#另外一种较常见的方式是PLAIN。与LOGIN机制的不同之处在于一次性输入账号和密码，
#格式为“<NUL>账号<NUL>密码”，其中<NUL>为字节0。验证过程:
#username = base64.encodestring("<NUL>wudiboy<NUL>XXXXXXXX")
#
#"""

fromaddr = "hjs00@126.com"
toaddrs  = fromaddr

print('# Add the From: and To: headers at the start!')
msg = "From: %s\r\nTo: %s\r\nSubject: 测试\r\n\r\n"%(fromaddr, toaddrs)
msg = msg + "这是邮件的内容部分\r\n"

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