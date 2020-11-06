from Functions.Util.Settings import settings
from Functions.Util.userHandling import *

sett = settings()


class Switch(dict):
    def __getitem__(self, item):
        for key in self.keys():
            if item in key:
                return super().__getitem__(key)
        raise KeyError(item)


def clamp(n):
    if n < 0:
        return 0
    elif n > sett.GetBadMax():
        return sett.GetBadMax() - 1
    else:
        return n


def getStatus(argument):
    arg = clamp(argument)
    switch = Switch({
        range(sett.GetGoodMin(), sett.GetGoodMax()): "Good running",
        range(sett.GetOkMin(), sett.GetOkMax()): "OK running",
        range(sett.GetLessMin(), sett.GetLessMax()): "More or less running",
        range(sett.GetBadMin(), sett.GetBadMax()): "Bad running or olf history file"
    })
    return switch[arg]


def getOverview():
    Overview = []
    with open("../Data/Logs/WarningHistory.json", "r") as f:
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
