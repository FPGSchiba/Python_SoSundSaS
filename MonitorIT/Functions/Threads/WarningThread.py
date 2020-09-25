import datetime
import json
import re
import threading
import time
from os.path import isfile
from Functions.ScanHardware import *


class warning_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.fileName = "../Data/Logs/WarningLogs.json"
        self.Data = {"info": {"CPU": {}, "GPU": {}, "MEM": {}, "DPC": {}, "DMX": {}, "DFR": {}}, "warn": {"CPU": {}, "GPU": {}, "MEM": {}, "DPC": {}, "DMX": {}, "DFR": {}}, "crit": {"CPU": {}, "GPU": {}, "MEM": {}, "DPC": {}, "DMX": {}, "DFR": {}}}
        self.CPU = 0
        self.GPU = 0
        self.MEM = 0
        self.DPC = 0
        self.DFR = 0

    def run(self):
        self.Loop()

    def checkLogs(self, input):
        if not input == "DFR":
            if len(self.Data["info"][input]) > 2:
                vs = []
                for i in self.Data["info"][input]:
                    vs.append(re.search(r'\d{1,3}', i).group(0))
                av = sum(vs) / len(vs)
                self.Data["warn"][input].update(datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "-" + input, "Inf: " + av + "% used")
                if len(self.Data["warn"][input]) > 2:
                    for i in self.Data["warn"][input]:
                        vs.append(re.search(r'\d{1,3}', i).group(0))
                    av = sum(vs) / len(vs)
                    self.Data["warn"][input].update(datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "-" + input, "Inf: " + av + "% used")
                    # send Mail for Crit
        else:
            if len(self.Data["info"][input]) > 2:
                vs = []
                for i in self.Data["info"][input]:
                    vs.append(re.search(r'\d{1,3}', i).group(0))
                av = sum(vs) / len(vs)
                self.Data["warn"][input].update(datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "-" + input, "Inf: " + av + "GB")
                if len(self.Data["warn"][input]) > 2:
                    for i in self.Data["warn"][input]:
                        vs.append(re.search(r'\d{1,3}', i).group(0))
                    av = sum(vs) / len(vs)
                    self.Data["warn"][input].update(datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "-" + input, "Inf: " + av + "GB Free")
                    # send Mail for Crit

    def Loop(self):
        if isfile(self.fileName):
            try:
                with open(self.fileName, "r") as f:
                    self.Data = json.loads(f)
            except TypeError:
                print("Warn: No content in Warning File")
        while True:
            self.CPU = CPU_Precent()
            if self.CPU >= 70:
                print("Warning generated")
                self.Data["info"]["CPU"].update(datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "-CPU", "Inf: " + self.CPU + "% used")
                self.checkLogs("CPU")
            self.GPU = GPU_Usage()
            if self.GPU >= 70:
                print("Warning generated")
                self.Data["info"]["GPU"].update(datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "-GPU", "Inf: " + self.CPU + "% used")
                self.checkLogs("GPU")
            self.MEM = MEM_Precent()
            if self.MEM >= 80:
                print("Warning generated")
                self.Data["info"]["MEM"].update(datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "-MEM", "Inf: " + self.CPU + "% used")
                self.checkLogs("MEM")
            self.DPC = DISK_Usage()
            if self.DPC >= 70:
                print("Warning generated")
                self.Data["info"]["DPC"].update(datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "-DPC", "Inf: " + self.CPU + "% used")
                self.checkLogs("DPC")
            self.DFR = DISK_Free()
            if self.DFR <= 100:
                print("Warning generated")
                self.Data["info"]["DFR"].update(datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "-DFR", "Inf: " + self.CPU + "GB Free")
                self.checkLogs("DFR")
            with open(self.fileName, "w") as f:
                json.dump(self.Data, f, indent=4)
            time.sleep(60)
