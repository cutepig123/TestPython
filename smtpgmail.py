#coding=utf-8

#fail!

#
#	����Outlook�е��ʼ���Gmail
#
#��ʹ��Gmail֮ǰ��������Outlook Express(OE)�������ʼ����ж�ʱ��Ҳ�ù�Foxmail��Thundmail�ȡ����и�ϰ�ߣ�ϲ������΢�е��ֵ���ż�������������˵����������õ��š������Ǹ�������֮��������ż�������������ʷ���۱���������ʱ��һ���������˼��ٷ��ʼ������ֶڻ���OE�У���̫�ù���
#
#Gmail���д������������������ɿ����ŵ㣬����Щ�ʼ���ת�Ƶ�GMail���Ǹ�����İ취��Ϊ�˱��ڹ����ʼ�����ý��ʼ�һ��һ���ת����GMail�У�ͬʱ���ܱ��������ˡ������˺�ʱ�����Ϣ��
#
#OE�е��ʼ��������Ϊeml��ʽ���ļ�����һ��ֻ�ܱ���һ���ʼ�����һ����������һ���Ե�������ʼ���ѡ��OE�еĶ���ʼ����Ϸŵ���Դ��������һ���ļ����У�OE���Զ�����Щ�ʼ���eml��ʽ�洢�����ļ����У������ʼ��������ɺ��ʵ��ļ����������ظ������ÿ���Ϸŵ�һ���յ��ļ����У������Ϸ�֮�䲻�ܱ�֤�ļ������ظ���
#
#������Ҫ�����ǰ���Щ��eml��ʽ�洢���ʼ�ԭ���ط��͵�Gmail�С�Python�ж�ȡeml��ʽ�ǳ��򵥣���email.message_from_file()���ɡ�����д�������ⲿSMTP������ת���ʼ��ĳ�������ʵ������ûʲô���⣬�����ĳ������£�

import email,smtplib
import os

def forward(toAddr, msg):
	server = smtplib.SMTP( SMTP_SERVER )
	server.login( SMTP_USER, SMTP_PASS )
	server.sendmail( SENDER, toAddr, msg )
	server.quit()
	return True

def backup(dir):
	for root,dirs,files in os.walk(dir):
		for name in files:
			print name
			msg = email.message_from_file( open( os.path.join(root,name) ) )
			sendmail.forward('davies.liu@gmail.com',msg.as_string())
			os.remove(os.path.join(root,name))

#backup( 'email' )  

