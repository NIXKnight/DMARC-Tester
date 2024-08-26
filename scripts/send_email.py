import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
import time
import os

# Get email configuration from environment variables
sender_email = os.getenv("SENDER_EMAIL", "default_sender@example.com")
recipient_email = os.getenv("RECIPIENT_EMAIL", "default_recipient@example.com")
smtp_server = "postfix"
smtp_port = 587

# Create the email
subject = "Email Test"
body = "This is a test email sent via an open relay."

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Function to check if the SMTP server is up
def wait_for_smtp_server(host, port):
    while True:
        try:
            with socket.create_connection((host, port), timeout=5):
                print(f"SMTP server at {host}:{port} is up!")
                return True
        except (socket.timeout, socket.error) as e:
            print(f"SMTP server at {host}:{port} is not available yet. Retrying in 5 seconds...")
            time.sleep(5)

# Wait for the SMTP server to be up
wait_for_smtp_server(smtp_server, smtp_port)

# Send the email once the SMTP server is up
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
