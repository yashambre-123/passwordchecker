# here we modify the mail and send it to the users accordingly
import smtplib
from email.message import EmailMessage
email=EmailMessage()
email['from']='yash ulhas ambre'  # the name 'yash ulhas ambre'
email['to']='sonalambre8@gmail.com',   # the recievers email address
email['subject']='helllooo' # the subject
email.set_content('what is your name?') # the content of the email
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('yash2002ambre@gmail.com','hoko@123@123')
    smtp.send_message(email)
    print('all good boss')