# Version 1.0

# first of all import the socket library
import socket

# import connection handling
from Functions.Threads.connection_thread import *

lt = logging_Thread()
lt.start()

wt = warning_Thread()
wt.start()

s = socket.socket()
print("Socket successfully created")

port = 5050

s.bind(('', port))
print("socket binded to %s" % port)

s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    ct = connection_thread()
    ct.run(c, addr)
