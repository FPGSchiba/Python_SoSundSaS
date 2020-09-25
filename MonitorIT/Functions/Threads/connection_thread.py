import hashlib
import threading

from Functions.Threads.DashboardThread import dashboard_thread
from Functions.userHandling import *
from Functions.Threads.LoggingThread import *
from Functions.Threads.WarningThread import *
from Functions.Errors.Errors import *

ServerVersion = 'Version: 1.1'


class connection_thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__()
        self.adress = None
        self.username = ""
        self.password = ""
        self.client = None
        self.connected = False

    def Connected(self):
        data = ServerVersion
        self.client.send(data.encode())
        clientVersion = self.client.recv(1024).decode()
        print("Checking Version...")
        if clientVersion == ServerVersion:
            print("Version is OK")
            for i in range(3):
                self.username = self.client.recv(1024).decode()
                self.password = hashlib.md5(self.client.recv(1024)).hexdigest()
                if userIsAllowedToConnect(self.username, self.password):
                    self.client.send("connected".encode())
                    self.connected = True
                    break
                else:
                    self.client.send("wrong".encode())
                    print("Username or Password incorrect for " + i)
            if self.connected:
                createConnectionToken(self.username, self.password, self.adress)
                self.client.send(readConnectionToken(self.adress).encode())
                while self.connected:
                    try:
                        clientOrder = self.client.recv(1024).decode()
                        if clientOrder == "see-dashboard":
                            if userIsAllowedToSeeRight(self.username, self.password, "right-dashboard"):
                                self.client("starting Dashboard".encode())
                                dt = dashboard_thread()
                                dt.run(self.client, self.adress)
                            else:
                                self.client.send("no Permission".encode())
                    except DisconnectedError:
                        print("Client " + self.adress + " disconnected")
                        self.client.close()
            else:
                self.client.send("abort".encode())
                print("to many wrong answers aborting...")
                self.client.close()

        else:
            self.client.send("abort")
            print("Client has a other Version aborting...")
            self.client.close()

    def run(self, c, addr):
        self.client = c
        self.Connected()

