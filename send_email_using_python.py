import smtplib

host_address = 'smtp.gmail.com'
port = 587
sender_email = 'testmail8521@gmail.com'
password = 'developer@123mail'
receiver_email = ['testmail8521@gmail.com']

mail_info = """\
Subject: First Mail Using Python
This text is sent from Python
"""

server = smtplib.SMTP(host_address, port)
server.starttls()

server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, mail_info)
print("Mail Sent Successfully")
server.quit()
