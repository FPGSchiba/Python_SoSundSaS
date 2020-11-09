import json


class settings:
    def __init__(self):
        with open("../Data/Settings/settings.json", "r") as f:
            self.Data = json.load(f)

    def GetGoodMin(self):
        return self.Data["Overview"]["Status"]["Good"]["GoodMin"]

    def GetGoodMax(self):
        return self.Data["Overview"]["Status"]["Good"]["GoodMax"]

    def GetOkMin(self):
        return self.Data["Overview"]["Status"]["Ok"]["OkMin"]

    def GetOkMax(self):
        return self.Data["Overview"]["Status"]["Ok"]["OkMax"]

    def GetLessMin(self):
        return self.Data["Overview"]["Status"]["Less"]["LessMin"]

    def GetLessMax(self):
        return self.Data["Overview"]["Status"]["Less"]["LessMax"]

    def GetBadMin(self):
        return self.Data["Overview"]["Status"]["Bad"]["BadMin"]

    def GetBadMax(self):
        return self.Data["Overview"]["Status"]["Bad"]["BadMax"]

    def GetTries(self):
        return self.Data["Connection"]["Tries"]

    def GetWarnCPU(self):
        return self.Data["Warning"]["CpuMax"]

    def GetWarnGPU(self):
        return self.Data["Warning"]["GpuMax"]

    def GetWarnMEM(self):
        return self.Data["Warning"]["MemMax"]

    def GetWarnDPC(self):
        return self.Data["Warning"]["DpcMax"]

    def GetWarnDFR(self):
        return self.Data["Warning"]["DfrMax"]

    def GetServerName(self):
        return self.Data["Mail"]["Sending"]["Server"]["Name"]

    def GetServerPort(self):
        return self.Data["Mail"]["Sending"]["Server"]["Port"]

    def GetSenderMail(self):
        return self.Data["Mail"]["Sending"]["SenderMail"]

    def GetSenderPassword(self):
        return self.Data["Mail"]["Sending"]["Password"]

    def GetSendingSubject(self):
        return self.Data["Mail"]["Sending"]["Subject"]

    def GetSendingAdditional(self):
        return self.Data["Mail"]["Sending"]["Additional"]

    def GetMailList(self):
        return self.Data["Mail"]["ToMail"]

    def SetSettings(self, data):
        with open("../Data/Settings/settings.json", "w") as f:
            json.dump(data, f, indent=4)
        self.__init__()
