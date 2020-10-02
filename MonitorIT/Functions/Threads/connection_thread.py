from Functions.Errors.Errors import *
from Functions.Threads.DashboardThread import dashboard_thread
from Functions.Threads.LoggingThread import *
from Functions.Threads.WarningThread import *
from Functions.Mail.CritMail import *
from Functions.Information.Overview import *

ServerVersion = 'Version: 1.1'


class connection_thread(threading.Thread):

    def __init__(self, c, addr):
        threading.Thread.__init__(self)
        self.client = c
        self.adress = str(addr)
        self.username = ""
        self.password = ""
        self.connected = False

    def Connected(self):
        isError = False
        try:
            self.client.send(ServerVersion.encode())
            clientVersion = self.client.recv(1024).decode()
            print("Checking Version...")
            if clientVersion == ServerVersion:
                print("Version is OK")
                self.client.send("sending Name".encode())
                self.client.send(socket.gethostname().encode())
                for i in range(3):
                    self.client.send("need user".encode())
                    self.username = self.client.recv(1024).decode()
                    self.client.send("need pw".encode())
                    self.password = self.client.recv(1024).decode()
                    if userIsAllowedToConnect(self.username, self.password):
                        self.client.send("connected".encode())
                        self.connected = True
                        break
                    else:
                        self.client.send("wrong".encode())
                        print("Username or Password incorrect")
            else:
                self.client.send("abort".encode())
                print("Client has a other Version aborting...")
                self.client.close()
        except ConnectionResetError:
            isError = True
            print("a Client disconnected while Login from: " + self.adress)
            self.client.close()
        except ConnectionAbortedError:
            isError = True
            print("a Client disconnected while Login from: " + self.adress)
            self.client.close()
        except DisconnectedError:
            isError = True
            print("Client " + self.adress + " disconnected")
            self.client.close()
        if self.connected:
            print("Client: " + self.adress + " successfully logged in")
            while self.connected:
                clientOrder = ""
                try:
                    clientOrder = self.client.recv(1024).decode()
                    if clientOrder == "see-dashboard":
                        if userIsAllowedToSeeRight(self.username, self.password, "right-dashboard"):
                            self.client.send("starting Dashboard".encode())
                            dt = dashboard_thread()
                            dt.run(self.client, self.adress)
                        else:
                            self.client.send("no Permission".encode())
                    if clientOrder == "get-overview":
                        if userIsAllowedToSeeRight(self.username, self.password, "right-dashboard"):
                            self.client.send("sending Overview".encode())
                            self.client.send(getOverview().encode())
                        else:
                            self.client.send("no Permission".encode())
                    if clientOrder == "disconnect":
                        print("Client " + self.adress + " disconnected")
                        self.client.close()
                        isError = False
                        break
                except DisconnectedError:
                    print("Client " + self.adress + " disconnected")
                    self.client.close()
                    isError = True
                    break
                except ConnectionResetError:
                    print("Client " + self.adress + " disconnected")
                    self.client.close()
                    isError = True
                    break
                except OSError:
                    print("Client " + self.adress + " disconnected")
                    self.client.close()
                    isError = True
                    break
        elif not isError:
            try:
                self.client.send("abort".encode())
                print("to many wrong answers aborting...")
            except OSError:
                print("already lost connection to: " + self.adress)
            sendEmail(socket.gethostname() + " - Crit", "Authentication-Crit: \n" + "Time: " + datetime.now().strftime("%d.%m.%Y %H:%M") + "\nValue: too many wrong Authentication from " + self.adress, ['craftzockerlp@gmail.com'])
            try:
                self.client.close()
            except DisconnectedError:
                print("Cannot close a closed connection")

    def run(self):
        self.Connected()
