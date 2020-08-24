import smtplib
import email.encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import os
server = smtplib.SMTP('smtp.office365.com', 25)

server.ehlo()
server.starttls()
user = os.environ['EmTest']
password = os.environ['EmailTestPass']

server.login(user, password)

msg = MIMEMultipart()

msg['FROM'] = 'TestPleaseIgnore'
msg['TO'] = ''
msg['Subject'] = 'testing python encrypt'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'TestImg.png'
attachment = open(filename, 'rb')

p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

email.encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail(user, '')
