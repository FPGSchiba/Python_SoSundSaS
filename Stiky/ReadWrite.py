# Version 1.0
# Author: Jann Erhardt
# Changes:==============================
#
# Init: 03.06.2020
#
# ======================================
#
# Notes:================================
#
# Notes here
#
# ======================================


def write(inputStr):
    posf = open("./Position.xml", "w+")
    posf.write(inputStr)


def read():
    posf = open("./Position.xml", "w+")
    str = posf.read()
    return str
