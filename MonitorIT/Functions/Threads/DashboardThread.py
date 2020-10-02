import threading
from Functions.Information.ScanHardware import *
from Functions.Errors.Errors import *


class dashboard_thread(threading.Thread):

    def __init__(self):
        super().__init__()
        self.client = None
        self.adress = None
        self.connected = True

    def Connected(self):
        print("Dashboard started")
        while self.connected:
            try:
                inputString = self.client.recv(1024).decode()
            except DisconnectedError:
                print("Client" + self.adress + " not responding")
                break
            self.CommandInput(inputString)
        print("Dashboard Closed")

    def run(self, c, addr):
        self.client = c
        self.adress = addr
        self.Connected()

    def CommandInput(self, input):
        if input == "GetCPU":
            self.client.send(str(CPU_Precent()).encode())
        elif input == "GetGPU":
            self.client.send(str(GPU_Usage()).encode())
        elif input == "GetMEM":
            self.client.send(str(MEM_Precent()).encode())
        elif input == "GetDPC":
            self.client.send(str(DISK_Usage()).encode())
        elif input == "GetDMX":
            self.client.send(str(DISK_Max()).encode())
        elif input == "GetDFR":
            self.client.send(str(DISK_Free()).encode())
        elif input == "disconnect":
            self.connected = False
        else:
            print("unhandled String aborting")
            self.client.close()
