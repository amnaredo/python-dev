import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Alejandro Martínez'
email['to'] = 'burnett.chester@gmail.com'
email['subject'] = 'Prueba de correo con Python'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('**********@gmail.com', '**********')
    smtp.send_message(email)
    print('all good boss!')
