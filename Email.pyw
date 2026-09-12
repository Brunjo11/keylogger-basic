import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


def send_email():
    # Get email configuration from environment variables
    sender = os.getenv("EMAIL_SENDER")
    receiver = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")
    report_file = os.getenv("REPORT_FILE", "report.txt")

    # Check that the required email credentials are available
    if not all([sender, receiver, password]):
        return

    # Check that the report file exists
    if not os.path.exists(report_file):
        return

    # Read the report
    with open(report_file, "r", encoding="utf-8") as f:
        body = f.read()

    # Do not send an email if the report is empty
    if not body.strip():
        return

    # Create the email
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "PC report"

    try:
        # Connect to the Microsoft SMTP server
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)

        # Clear the report after a successful delivery
        # The file itself is not deleted
        with open(report_file, "w", encoding="utf-8") as f:
            f.write("")

    except Exception as e:
        # Keep the report intact if the email cannot be sent
        print(f"Email sending failed: {e}")


if __name__ == "__main__":
    send_email()
