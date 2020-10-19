import os
import smtplib
from datetime import datetime
from os.path import isfile
from Functions.Crypt import *


def sendEmail(subject, body, to):
    keyFile = "../../Data/Mail/key.bin"
    passFile = "../../Data/Mail/pass.bin"
    gmail_user = 'monitorit.email@gmail.com'

    if not isfile(keyFile):
        writeKey(keyFile)

    key = readKey(keyFile)
    if isfile("../Data/Mail/pass.txt"):
        with open("../Data/Mail/pass.txt", "r") as f:
            encryptData(f.readline(14).encode(), passFile, key)
            f.close()
        os.remove("../Data/Mail/pass.txt")

    password = readData(passFile, key).decode()
    sent_from = gmail_user
    msg = "\r\n".join([
        f"From: {sent_from}",
        f"To: {to}",
        f"Subject: {subject}",
        "",
        f"{body}"
    ])

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, password)
        server.sendmail(sent_from, to, msg)
        server.close()
        print('Critical sent at: ' + str(datetime.now()))
        return True
    except Exception as e:
        print(e)
        print("failed to send email")
        return False