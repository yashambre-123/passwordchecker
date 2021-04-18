# here we can send email through python
# Before executing your code, it is neccessary to turn on the secure app access.
import smtplib
from email.message import EmailMessage
email=EmailMessage()
email['from']=''  # just enter your name btw the single quotes
email['to']='',   # the recievers email address  btw the single quotes
email['subject']='' # the subject btw the single quotes
email.set_content('') # the content of the email btw the single quotes
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('','') # enter your mail id in the first single quotes, and the password of your mail account in the second single quotes
    smtp.send_message(email)
    print('all good boss')
