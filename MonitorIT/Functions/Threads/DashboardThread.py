import threading
from Functions.Information.ScanHardware import *
from Functions.Errors.Errors import *


class dashboard_thread(threading.Thread):

    def __init__(self):
        super().__init__()
        self.client = None
        self.adress = None

    def Connected(self):
        connected = True
        while connected:
            try:
                inputString = self.client.recv(1024).decode()
            except DisconnectedError:
                print("Client" + self.adress + " disconnected")
                self.client.close()
                break
            self.CommandInput(inputString)

    def run(self, c, addr):
        self.client = c
        self.adress = addr
        self.Connected()

    def CommandInput(self, input):
        if input == "GetCPU":
            self.client.send(str(CPU_Precent()).encode())
            print("sent CPU values")
        elif input == "GetGPU":
            self.client.send(str(GPU_Usage()).encode())
            print("sent GPU values")
        elif input == "GetMEM":
            self.client.send(str(MEM_Precent()).encode())
            print("sent MEM values")
        elif input == "GetDPC":
            self.client.send(str(DISK_Usage()).encode())
            print("sent DPC values")
        elif input == "GetDMX":
            self.client.send(str(DISK_Max()).encode())
            print("sent DMX values")
        elif input == "GetDFR":
            self.client.send(str(DISK_Free()).encode())
            print("sent DFR values")
        else:
            print("not supported string aborting...")
            self.client.close()

