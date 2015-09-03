#coding=utf-8
#赛尔网络的自动登录程序(做好了)
#发信站: BBS 水木清华站 (Tue Jan 25 16:24:01 2005), 转信
#
#基于python2.4, python2.3的urllib2不支持cookie

#!/usr/bin/python2.4
import urllib, urllib2, cookielib

USER = 'XXX'
PASS = 'xxx'
SERVERIP = '219.223.254.61'
ALLOWABOARD = True

def szlogin(login, passwd):
	prepare()
	status = check(login, passwd)
	print status
	if not status:
		loginon()
		print check(login, passwd)

def prepare():
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	opener.add_handler(urllib2.HTTPSHandler())
	urllib2.install_opener(opener)

def check(login, passwd):
	url = 'https://%s/CustomerLogin.go' % SERVERIP
	data = urllib.urlencode({'login': login,
							 'passwd': passwd})
	print data
	ifile = urllib2.urlopen(url, data)
	print ifile.info()
	result = ifile.read()
	ifile.close()
	if 'green.gif' in result:
		return True
	elif 'red.gif' in result:
		return False
	assert False

def loginon():
	url = 'https://%s/customer.self.CustomerOnLine.co' % SERVERIP
	if ALLOWABOARD:
		data = urllib.urlencode({'allowAboard':'on'})
	else:
		data = urllib.urlencode({'allowAboard':'off'})
	ifile = urllib2.urlopen(url, data)
	print ifile.info()
	ifile.close()

def main():
	szlogin(USER, PASS)

if __name__ == '__main__':
	main()