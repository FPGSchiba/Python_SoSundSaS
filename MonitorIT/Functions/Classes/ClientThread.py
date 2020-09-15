import threading
from Functions.ScanHardware import *

ServerVersion = 'Version: 1.0'


class client_thread(threading.Thread):

    def Connected(self):
        connected = True
        data = ServerVersion
        self.client.send(data.encode())
        clientVersion = self.client.recv(1024).decode()
        print("Checking Version...")
        if clientVersion == ServerVersion:
            print("Version is OK")
            while connected:
                try:
                    inputString = self.client.recv(1024).decode()
                except:
                    print("Client disconnected")
                    self.client.close()
                    break
                self.CommandInput(inputString)
        else:
            print("Client has a other Version aborting...")
            client.close()

    def run(self, c):
        self.client = c
        self.Connected()

    def CommandInput(self, input):
        if input == "GetCPU":
            self.client.send(str(CPU_Precent()).encode())
            print("sent CPU values")
        if input == "GetGPU":
            self.client.send(str(GPU_Usage()).encode())
            print("sent GPU values")
        if input == "GetMEM":
            self.client.send(str(MEM_Precent()).encode())
            print("sent MEM values")
        if input == "GetDPC":
            self.client.send(str(DISK_Usage()).encode())
            print("sent DPC values")
        if input == "GetDMX":
            self.client.send(str(DISK_Max()).encode())
            print("sent DMX values")
        if input == "GetDFR":
            self.client.send(str(DISK_Free()).encode())
            print("sent DFR values")
