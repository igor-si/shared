#!/usr/bin/python
import os,sys,random
import smtplib
from email.mime.text import MIMEText

recipients = []
recipients.append("igor-si@moving-pictures.com")
#recipients.append('natalia-l@moving-pictures.com')
#recipients.append('akmal-s@moving-pictures.com')

me = 'igor-si@moving-pictures.com'
for recipient in recipients:
	messageToSend = 'you are the {}'.format(recipient)
	email = MIMEText(messageToSend)

	email['From'] = 'me {}'.format('batman')
	#email['To'] = 'you are {}'.format('recipient')
	email['To'] = recipient

	s = smtplib.SMTP('localhost')
	s.sendmail(me.recipient.email.as_string())
	s.quit


#import psutil
#process_name = 'houdini'
#for proc in psutil.process_iter():
#	if process_name in proc.name():
#		proc.kill()