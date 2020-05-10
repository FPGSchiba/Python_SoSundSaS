# Cloud Server Main Script
# Version: 1.0
# Author: Lukas Meier, Jann Erhardt
# Changes:
# ===================================================
#
# 1 --> Init // 06.05.2020 // Jann Erhardt
# 2 --> Socket Start und Log // 10.05.2020 // Jann Erhardt
#
# ===================================================
#
# Notice:
# ===================================================
#
# 1 --> Init // import socket // Jann Erhardt
# 2 --> Socket Start und Log // Jann Erhardt
#
# ===================================================

from Server.ServerLib import *
import socket
import time
import datetime
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(ADDR)


def handle_client(conn, addr):
    pass


def Start():
    sock.listen()
    Log("Server has Started")
    while True:
        conn, addr = sock.accept()
        Thread = threading.Thread(target=handle_client, args=(conn, addr))
        Thread.start()
        Log("{thread:d3}".format(thread=threading.active_count() - 1))


Log("Server is Starting")
Start()
