# Version 1.0

# first of all import the socket library
import socket
import threading
from Functions.ScanHardware import *

# next create a socket object
s = socket.socket()
ServerVersion = 'Version: 1.0'
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 5050

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" % port)

# put the socket into listening mode
s.listen(5)
print("socket is listening")


class client_thread(threading.Thread):

    def Connected(self, client):
        connected = True
        data = ServerVersion
        client.send(data.encode())
        clientVersion = client.recv(1024).decode()
        print("Checking Version...")
        if clientVersion == ServerVersion:
            print("Version is OK")
            while connected:
                try:
                    inputString = client.recv(1024).decode()
                except:
                    print("Client disconnected")
                    client.close()
                    break
                self.CommandInput(inputString, client)
        else:
            print("Client has a other Version aborting...")
            client.close()

    def run(self, c):
        self.Connected(c)

    def CommandInput(self, input, client):
        if input == "GetCPU":
            client.send(str(CPU_Precent()).encode())
            print("sent CPU values")


# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # Create a Thread to Handle Clients
    ct = client_thread()
    ct.run(c)