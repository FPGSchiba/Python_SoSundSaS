from Functions.Util.Errors import *
from Functions.Threads.DashboardThread import dashboard_thread
from Functions.Threads.WarningThread import *
from Functions.Util.CritMail import *
from Functions.Information.Overview import *

ServerVersion = 'Version: 1.1'


class connection_thread(threading.Thread):

    def __init__(self, c, addr):
        threading.Thread.__init__(self)
        self.sett = settings()
        self.client = c
        self.adress = str(addr)
        self.username = ""
        self.password = ""
        self.connected = False
        self.wrongUsers = self.sett.GetTries()

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
                for i in range(self.wrongUsers):
                    self.client.send("need user".encode())
                    self.username = self.client.recv(1024).decode()
                    self.client.send("need pw".encode())
                    self.password = self.client.recv(1024).decode()
                    if userIsAllowedToConnect(self.username, self.password):
                        self.client.send("connected".encode())
                        self.connected = True
                        break
                    else:
                        if i < self.wrongUsers - 1:
                            self.client.send("wrong".encode())
                            print("Username or Password incorrect")
                        else:
                            try:
                                self.client.send("abort".encode())
                                print("to many wrong answers aborting...")
                            except OSError:
                                print("already lost connection to: " + self.adress)
                            sendEmail("Authentication-Crit: \n" + "Time: " + datetime.now().strftime("%d.%m.%Y %H:%M") + "\nValue: too many wrong Authentication from " + self.adress)
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
                    if clientOrder == "get-settings":
                        if userIsAllowedToSeeRight(self.username, self.password, "right-manage"):
                            self.client.send("sending Settings".encode())
                            if self.client.recv(1024).decode() == "send Settings":
                                self.client.send(str(sett.Data).encode())
                                print("sent Settings")
                        else:
                            self.client.send("no Permission".encode())
                    if clientOrder == "set-settings":
                        if userIsAllowedToEditRight(self.username, self.password, "right-manage"):
                            self.client.send("get Settings".encode())
                            if not self.client.recv(1024).decode() == "abort":
                                sett.SetSettings(json.loads(self.client.recv(1024).decode()))
                                print("changed Settings")
                            else:
                                print("settings changing aborted")
                        else:
                            self.client.send("no Permission".encode())
                    if clientOrder == "disconnect":
                        print("Client " + self.adress + " disconnected")
                        self.client.close()
                        isError = False
                        break
                except DisconnectedError as er:
                    print("Client " + self.adress + " disconnected bc: " + er.message)
                    self.client.close()
                    isError = True
                    break
                except ConnectionResetError as er:
                    print("Client " + self.adress + " disconnected bc: " + er.message)
                    self.client.close()
                    isError = True
                    break
                except OSError as er:
                    print("Client " + self.adress + " disconnected bc: " + er.message)
                    self.client.close()
                    isError = True
                    break
        elif not isError:
            try:
                self.client.close()
            except DisconnectedError:
                print("Cannot close a closed connection")

    def run(self):
        self.Connected()
