# Cloud Server Library Script
# Version: 1.0
# Author: Lukas Meier, Jann Erhardt
# Changes:
# ===================================================
#
#  1 --> Init // 06.05.2020 // Jann Erhardt
#
# ===================================================
#
# Notice:
# ===================================================
#
# 1 --> Init // import socket // Jann Erhardt
#
# ===================================================

import socket
import datetime


def Log(msg):
    print("[" + socket.gethostname() + "|" + str(datetime.datetime.now()) + "]: " + msg)


def outPut(addr, msg):
    print("[" + addr + "|" + str(datetime.datetime.now()) + "]: " + msg)
