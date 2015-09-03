import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os,sys

#to = ['recipient1@some.where', 'recipient2@some.where']
#msg['To'] = ', '.join(you)
def mail(to, subject, text, attach):
	msg = MIMEMultipart()

	gmail_user = "jinshouhe@gmail.com"
	gmail_pwd = "wE6558"
	
	msg['From'] = gmail_user
	msg['To'] = ','.join(to)
	msg['Subject'] = subject

	msg.attach(MIMEText(text))

	if os.path.isfile(attach):
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(open(attach, 'rb').read())
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition',
			  'attachment; filename="%s"' % os.path.basename(attach))
		msg.attach(part)

	
	mailServer = smtplib.SMTP("smtp.gmail.com", 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	print 'login',
	mailServer.login(gmail_user, gmail_pwd)
	print 'ok'
	mailServer.sendmail(gmail_user, to, msg.as_string())
	# Should be mailServer.quit(), but that crashes...
	mailServer.close()
	print 'done'
	raw_input('XXX')
	
if len(	sys.argv)<4:
	print 	"Usage: sEmail title msg file"
	raw_input('XXX')
else:
	title=sys.argv[1]
	msg=sys.argv[2]
	file=sys.argv[3]

	mail(["jinshouhe@gmail.com",'lillian.li@huawei.com','16630048@qq.com'],
		title,
		msg,
		file)
