# Version 1.0
# Author: Jann Erhardt
# Changes:==============================
#
# Init: 03.06.2020
# Tests: 03.06.2020
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
    posf.close()


def read():
    posf = open("./Position.xml", "r")
    str = posf.read()
    posf.close()
    return str

"https://fooby.ch/de/rezepte/18080/suesskartoffel-quinoa-bowl?startAuto1=0"