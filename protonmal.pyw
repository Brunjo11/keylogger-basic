import os
import ssl
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email():
    sender = os.getenv("EMAIL_SENDER")
    receiver = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")  # password SMTP generata dal Bridge, non quella dell'account
    report_file = os.getenv("REPORT_FILE", "report.txt")
    server_name = os.getenv("SMTP_SERVER", "127.0.0.1")
    port = int(os.getenv("SMTP_PORT", "1025"))

    if not all([sender, receiver, password]):
        return
    if not os.path.exists(report_file):
        return

    with open(report_file, "r", encoding="utf-8") as f:
        body = f.read()

    msg = MIMEText(body)
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "PC report"

    # Il Bridge usa un certificato self-signed: serve un contesto SSL permissivo
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with smtplib.SMTP(server_name, port) as server:
        server.starttls(context=context)
        server.login(sender, password)
        server.send_message(msg)

if __name__ == "__main__":
    send_email()
