#!/usr/bin/python
import os, re
import sys
import smtplib
from optparse import OptionParser 
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
#SMTP_SERVER = 'smtp.126.com'
#SMTP_PORT = 465
 
max_mail_sz =10000000

parser = OptionParser()
parser.add_option("-e", "--sender", dest="sender",
                  help="")
parser.add_option("-p", "--password", dest="password",
                  help="")
parser.add_option("-r", "--recipient", dest="recipient",
                  help="for multiple recipients, pls separate by ;")
parser.add_option("-s", "--subject", dest="subject",
                  help="")
parser.add_option("-m", "--message", dest="message",
                  help="")				  
parser.add_option("-d", "--directory", dest="directory",
                  help="")
parser.add_option("-f", '--filename', dest='filename',help="")
parser.add_option("-R", "--hide_recipient", dest="hide_recipient",
                  help="define hided recipient")
				  
parser.add_option("-S", "--hide_sender", dest="hide_sender",
                  help="define hided sender (cannot work!!)")
				  
(options, args) = parser.parse_args()

if options.recipient is None or options.subject is None or options.message is None:
	parser.print_help()
	assert(0)
 
recipient = options.recipient
hide_recipient=options.hide_recipient
hide_sender=options.hide_sender
subject = options.subject
message = options.message
directory = options.directory
filename = options.filename
sender = options.sender
password = options.password

print options

msg = MIMEMultipart()
msg['Subject'] = subject
if hide_recipient is not None:
	msg['To'] = hide_recipient
else:
	msg['To'] = recipient
	
if hide_sender is not None:
	msg['From'] = hide_sender
else:	
	msg['From'] = sender

if directory is not None:
	files = os.listdir(directory)
	#gifsearch = re.compile(".txt", re.IGNORECASE)
	#files = filter(gifsearch.search, files)
	for filename in files:
		path = os.path.join(directory, filename) 
		print filename
		if not os.path.isfile(path):
			continue
 
		img = MIMEImage(open(path, 'rb').read(), _subtype="gif")
		img.add_header('Content-Disposition', 'attachment', filename=filename)
		msg.attach(img)
		
if filename is not None and os.path.isfile(filename):
		img = MIMEImage(open(filename, 'rb').read(), _subtype="gif")
		img.add_header('Content-Disposition', 'attachment', filename=filename)
		msg.attach(img)
	
part = MIMEText('text', "plain")
part.set_payload(message)
msg.attach(part)

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

session.ehlo()
session.starttls()
session.ehlo
session.login(sender, password)

msgs=msg.as_string()
#print msgs
session.sendmail(sender, recipient.split(';'), msgs)
session.quit()
 
