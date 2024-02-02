import smtplib
import ssl


def send_email(user_mail, message):
    host = "smtp.gmail.com"
    port=465
    username = ""
    password = ""
    context = ssl.create_default_context()

    message_body = f"""\
Subject: Portfolio mail from {user_mail}

From: {user_mail}
{message}
"""

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username,password)
        server.sendmail(username, user_mail, message_body)

