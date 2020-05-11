# Cloud Server Main Script
# Version: 1.0
# Author: Lukas Meier, Jann Erhardt
# Changes:
# ===================================================
#
# 1 --> Init // 06.05.2020 // Jann Erhardt
# 2 --> Socket Start und Log // 10.05.2020 // Jann Erhardt
# 3 --> handle_client fertiges Ger¨üst // 11.05.2020 // Jann Erhardt
#
# ===================================================
#
# Notice:
# ===================================================
#
# 1 --> Init // import socket // Jann Erhardt
# 2 --> Socket Start und Log // Jann Erhardt
# 3 --> HEADER --> Evtl. zu klein --> Nummer erhöhen // Jann Erhardt
#
# ===================================================

from Server.ServerLib import *
import socket
import time
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT = "!disconnect"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(ADDR)


def handle_client(conn, addr):
    Log("Client [" + addr + "] connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT:
            connected = False
        outPut(addr, msg)

    conn.close()



def Start():
    sock.listen()
    Log(f"Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = sock.accept()
        Thread = threading.Thread(target=handle_client, args=(conn, addr))
        Thread.start()
        Log("{thread:d3}".format(thread=threading.active_count() - 1))


Log("Server is Starting")
Start()
