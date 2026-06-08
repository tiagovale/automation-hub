import os
import smtplib
from email.message import EmailMessage

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["EMAIL_PASSWORD"]
DESTINO = os.environ["EMAIL_DESTINO"]

msg = EmailMessage()
msg["Subject"] = "Teste GitHub Actions"
msg["From"] = EMAIL
msg["To"] = DESTINO

msg.set_content("Email enviado pelo GitHub Actions 🚀")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(msg)

print("Email enviado com sucesso!")