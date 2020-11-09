import smtplib
import socket
from datetime import datetime
from Functions.Util.Settings import *


def sendEmail(body):
    sett = settings()
    FullBody = body + "\nAdditional Info: \n" + sett.GetSendingAdditional()
    msg = "\r\n".join([
        f"From: {sett.GetSenderMail()}",
        f"To: {sett.GetMailList()}",
        f"Subject: {socket.gethostname() + sett.GetSendingSubject()}",
        "",
        f"{FullBody}"
    ]).encode('utf-8')

    try:
        server = smtplib.SMTP_SSL(sett.GetServerName(), sett.GetServerPort())
        server.ehlo()
        server.login(sett.GetSenderMail(), sett.GetSenderPassword())
        server.sendmail(sett.GetSenderMail(), sett.GetMailList(), msg)
        server.close()
        print('Critical sent at: ' + str(datetime.now()))
        return True
    except Exception as e:
        print(e)
        print("failed to send email")
        return False