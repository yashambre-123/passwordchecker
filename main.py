# for sending an common mail to all the users , here we take the help of the index.html file
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html=Template(Path('index.html').read_text())
email=EmailMessage()
email['from']=''   # the name 'yash ulhas ambre'
email['to']=''     # the recievers email address
email['subject']='' # the subject
email.set_content(html.substitute({'name':'shishuku'}),'html')
with smtplib.SMTP(host='smtp.gmail.com',port=587,) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('yash2002ambre@gmail.com','hoko@123@123')
    smtp.send_message(email)
    print('all good boss')
