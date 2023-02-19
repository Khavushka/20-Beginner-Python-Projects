'''
First projekt
From 'https://www.youtube.com/watch?v=pdy3nh1tn6I'
'''

from email.message import EmailMessage
#her importing the password
from app2 import password
'''
(SSL) Provides access to Transport Layer Security encryption 
and peer authentication facilities for netwoork cockets, 
both client-side and server-side
'''
import ssl
import smtplib

email_sender = 'codewith@gmail.com'
email_password = password

# Derefter går til 'https://temp-mail.org/da/'  
# Den hjemmeside generere en fake email-adresse
email_receiver = 'jabeli2437@ngopy.com'

subject = "Følg mig"
body = 'Følg mig på LinkedIn'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

 