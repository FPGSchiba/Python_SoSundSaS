import json


class settings:
    def __init__(self):
        with open("../Data/Settings/settings.json", "r") as f:
            self.Data = json.load(f)

    def GetGoodMin(self):
        return self.Data["overview"]["status"]["good"]["goodMin"]

    def GetGoodMax(self):
        return self.Data["overview"]["status"]["good"]["goodMax"]

    def GetOkMin(self):
        return self.Data["overview"]["status"]["ok"]["okMin"]

    def GetOkMax(self):
        return self.Data["overview"]["status"]["ok"]["okMax"]

    def GetLessMin(self):
        return self.Data["overview"]["status"]["less"]["lessMin"]

    def GetLessMax(self):
        return self.Data["overview"]["status"]["less"]["lessMax"]

    def GetBadMin(self):
        return self.Data["overview"]["status"]["bad"]["badMin"]

    def GetBadMax(self):
        return self.Data["overview"]["status"]["bad"]["badMax"]

    def GetTries(self):
        return self.Data["connection"]["tries"]

    def GetWarnCPU(self):
        return self.Data["warning"]["CPUMax"]

    def GetWarnGPU(self):
        return self.Data["warning"]["GPUMax"]

    def GetWarnMEM(self):
        return self.Data["warning"]["MEMMax"]

    def GetWarnDPC(self):
        return self.Data["warning"]["DPCMax"]

    def GetWarnDFR(self):
        return self.Data["warning"]["DFRMax"]

    def GetServerName(self):
        return self.Data["mail"]["sending"]["server"]["name"]

    def GetServerPort(self):
        return self.Data["mail"]["sending"]["server"]["port"]

    def GetSenderMail(self):
        return self.Data["mail"]["sending"]["sender-mail"]

    def GetSenderPassword(self):
        return self.Data["mail"]["sending"]["password"]

    def GetSendingSubject(self):
        return self.Data["mail"]["sending"]["subject"]

    def GetSendingAdditional(self):
        return self.Data["mail"]["sending"]["additional"]

    def GetMailList(self):
        return self.Data["mail"]["to-mail"]
