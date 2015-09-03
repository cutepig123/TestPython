#coding=utf-8

#fail!

#
#	备份Outlook中的邮件到Gmail
#
#在使用Gmail之前，都是用Outlook Express(OE)来处理邮件，有段时间也用过Foxmail、Thundmail等。我有个习惯，喜欢把稍微有点价值的信件都保留下来，说不定哪天就用得着。尤其是跟好朋友之间的往来信件，都被当作历史留痕保存下来。时间一长，积累了几百封邮件，部分囤积在OE中，不太好管理。
#
#Gmail具有大容量、便于搜索、可靠等优点，把这些邮件都转移到GMail中是个不错的办法。为了便于管理邮件，最好将邮件一封一封的转发到GMail中，同时还能保留发信人、收信人和时间等信息。
#
#OE中的邮件可以另存为eml格式的文件，但一次只能保存一封邮件。有一个方法可以一次性导出多封邮件：选中OE中的多封邮件，拖放到资源管理器的一个文件夹中，OE会自动把这些邮件以eml格式存储到该文件夹中，并由邮件标题生成合适的文件名，避免重复。最好每次拖放到一个空的文件夹中，两次拖放之间不能保证文件名不重复。
#
#现在需要做的是把这些以eml格式存储的邮件原样地发送到Gmail中。Python中读取eml格式非常简单，用email.message_from_file()即可。曾经写过利用外部SMTP服务器转发邮件的程序，整个实现起来没什么问题，完整的程序如下：

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

