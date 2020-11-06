import hashlib
import json
from os.path import isfile
from Functions.Util.Crypt import *


def Encode(data):
    encryptData(json.dumps(data).encode('utf-8'), userFileName, readKey(keyFile))


def Decode():
    return json.loads(readData(userFileName, readKey(keyFile)))


def checkKey():
    if not isfile(keyFile):
        writeKey(keyFile)


def checkFile(initData):
    if isfile(userFileName):
        try:
            Decode()
        except KeyError:
            print("Something with the user went wrong")
    else:
        Encode(initData)


def getUserCount():
    data = Decode()
    return len(data)


def userIsAllowedToConnect(username, hashedpassword):
    data = Decode()
    try:
        return data[username]["password"] == hashedpassword
    except KeyError:
        return False


def userIsAllowedToSeeRight(username, hashedpassword, right):
    data = Decode()
    try:
        if data[username]["password"] == hashedpassword:
            if data[username]["rights"][right] == 2 or data[username]["rights"][right] == 1:
                return True
        else:
            return False
    except KeyError:
        return False


def userIsAllowedToEditRight(username, hashedpassword, right):
    data = Decode()
    try:
        if data[username]["password"] == hashedpassword:
            return data[username]["rights"][right] == 2
        else:
            return False
    except KeyError:
        return False


def createConnectionToken(username, hashedpassword, addr):
    try:
        if userIsAllowedToConnect(username, hashedpassword):
            string = username + hashedpassword
            hashed = hashlib.md5(string.encode())
            data = {}
            if isfile(connectionFileName):
                data = readConnectionToken()
                data.update(addr, hashed)
                encryptData(json.dumps(data).encode('utf-8'), connectionFileName, readKey(keyFile))
            else:
                data.update(addr, hashed)
                encryptData(json.dumps(data).encode('utf-8'), connectionFileName, readKey(keyFile))
    except KeyError:
        print("Failed to create a Connection Token")


def readConnectionToken(addr):
    data = json.loads(readData(connectionFileName, readKey(keyFile)))
    return data[addr]


def validateConnectionToken(hashed, addr):
    try:
        data = readConnectionToken()
        return data[addr] == hashed
    except KeyError:
        return False


def deleteConnectionToken(addr):
    try:
        data = readConnectionToken()
        del data[addr]
    except KeyError:
        print("Adress " + addr + " had no Connection-Token")


global userFileName
global connectionFileName
global keyFile
global Data
userFileName = "../Data/User/users.bin"
keyFile = "../Data/User/key.bin"
connectionFileName = "../Data/User/connection.bin"
Data = {
    "root": {
        "username": "root",
        "password": "bed128365216c019988915ed3add75fb",
        "rights": {
            "right-manage": 2,
            "right-user": 2,
            "right-warning": 2,
            "right-dashboard": 2
        }
    }
}

global Token
Token = {}

checkKey()
checkFile(Data)
