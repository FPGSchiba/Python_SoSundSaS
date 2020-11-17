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
    return data["users"]


def userIsAllowedToConnect(username, hashedpassword):
    data = Decode()
    try:
        for i in range(getUserCount() - 1):
            if data[str(i)]["username"] == username:
                return data[str(i)]["password"] == hashedpassword
        return False
    except Exception as er:
        print("error user: " + er)
        return False


def userIsAllowedToSeeRight(username, hashedpassword, right):
    data = Decode()
    try:
        for i in range(getUserCount() - 1):
            if data[str(i)]["username"] == username:
                if data[str(i)]["password"] == hashedpassword:
                    return data[str(i)]["rights"][right] == 2 or data[str(i)]["rights"][right] == 1
            else:
                return False
        return False
    except KeyError:
        return False


def userIsAllowedToEditRight(username, hashedpassword, right):
    data = Decode()
    try:
        for i in range(getUserCount() - 1):
            if data[str(i)]["username"] == username:
                if data[str(i)]["password"] == hashedpassword:
                    return data[str(i)]["rights"][right] == 2
            else:
                return False
        return False
    except KeyError as er:
        print("error user: " + er)
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


def getAllUsers(username, password):
    data = Decode()
    if userIsAllowedToSeeRight(username, password, "rightUser"):
        return data
    else:
        return False


def setAllUsers(username, password, data):
    if userIsAllowedToEditRight(username, password, "rightUser"):
        Encode(data)
        return True
    else:
        return False


global userFileName
global connectionFileName
global keyFile
userFileName = "../Data/User/users.bin"
keyFile = "../Data/User/key.bin"
connectionFileName = "../Data/User/connection.bin"
global Data
Data = {
    "users": 2,
    "0": {
        "username": "root",
        "password": "bed128365216c019988915ed3add75fb",
        "rights": {
            "rightManage": 2,
            "rightUser": 2,
            "rightWarning": 2,
            "rightDashboard": 2
        }
    },
    "1": {
        "username": "dummy",
        "password": "43278dca20581b0682058a274cbf0c43",
        "rights": {
            "rightManage": 0,
            "rightUser": 0,
            "rightWarning": 0,
            "rightDashboard": 0
        }
    }
}

global Token
Token = {}

checkKey()
checkFile(Data)
