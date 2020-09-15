# Version 1.0

# first of all import the socket library
import socket
from Functions.Classes.ClientThread import *
from Functions.Classes.LoggingThread import *

lt = logging_Thread()
lt.start()

# next create a socket object
s = socket.socket()
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

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # Create a Thread to Handle Clients
    ct = client_thread()
    ct.run(c)
