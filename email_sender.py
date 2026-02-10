import smtplib
from email.message import EmailMessage
#Email details
sender_email = "tmnithya981@gmail.com"
receiver_email = "4mh23cs168@gmail.com"
password = "pkme wlhc qaqb jwty"
# Create email
msg = EmailMessage()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = 'Test Email from Python'
msg.set_content('Hello 👋\nThis email was sent using Python.')

# SMTP server setup
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, password)
    server.send_message(msg)

print("Email sent successfully!")
