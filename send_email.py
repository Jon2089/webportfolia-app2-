import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "arm2001chong@gmail.com"
password = "giqkflcqykixbnif"

receiver = "abdurrehman.otaku@gmail.com"

context = ssl.create_default_context()

message ="""
sup bro
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)