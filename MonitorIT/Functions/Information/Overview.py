from Functions.Information.userHandling import *


class Switch(dict):
    def __getitem__(self, item):
        for key in self.keys():
            if item in key:
                return super().__getitem__(key)
        raise KeyError(item)


def clamp(n):
    if n < 0:
        return 0
    elif n > 10000:
        return 10000
    else:
        return n


def getStatus(argument):
    arg = clamp(argument)
    switch = Switch({
        range(0, 10): "Good Running",
        range(11, 30): "OK running",
        range(31, 100): "Look for better Performance",
        range(101, 10001): "Bad please clear History file or check your Server"
    })
    return switch[arg]


def getOverview():
    Overview = []
    with open("../../Data/Logs/WarningHistory.json", "r") as f:
        try:
            Overview.append(len(json.loads(f)))
        except TypeError:
            Overview.append(0)
    Overview.append(getUserCount())
    Overview.append(getStatus(Overview[0]))
    temp = ""
    for i in Overview:
        temp += str(i) + "|"
    return temp
