# -*- coding: utf-8 -*-
# email_util.py
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD, TO_EMAIL

def send_email(content):
    msg = MIMEText(content, "plain", "utf-8")
    msg["From"] = EMAIL_USER
    msg["To"] = ",".join(TO_EMAIL)
    msg["Subject"] = f"{pd.Timestamp.now().strftime('%Y年%m月%d日')}舆情监控提醒"

    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_USER, TO_EMAIL, msg.as_string())
    server.quit()

