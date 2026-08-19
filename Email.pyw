import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email():
    sender = os.getenv("EMAIL_SENDER")
    receiver = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")
    report_file = os.getenv("REPORT_FILE", "report.txt")

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

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

if __name__ == "__main__":
    send_email()
