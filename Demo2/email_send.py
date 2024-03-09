from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template
import smtplib

sender_email = "reizonhill342@gmail.com"
recipient_email = "kipkuruihillary05@gmail.com"

template = Template(Path("/home/developer/Documents/Buffalo/Demo2/template.html").read_text(encoding="utf-8"))

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Email demo"

body = template.substitute({"name": "Hillary"})
message.attach(MIMEText(body, "html"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("reizonhill342@gmail.com", "")
    smtp.sendmail(sender_email, recipient_email, message.as_string())
    print("Sent...")
