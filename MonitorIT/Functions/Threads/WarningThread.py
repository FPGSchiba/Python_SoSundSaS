import datetime
import json
import re
import threading
import time
from Functions.Information.ScanHardware import *
from Functions.Util.CritMail import *
import socket


class warning_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.fileName = "../../Data/Logs/WarningLogs.json"
        self.Data = {"info": {"CPU": [], "GPU": [], "MEM": [], "DPC": [], "DMX": [], "DFR": []}, "warn": {"CPU": [], "GPU": [], "MEM": [], "DPC": [], "DMX": [], "DFR": []}, "crit": {"CPU": [], "GPU": [], "MEM": [], "DPC": [], "DMX": [], "DFR": []}}
        self.History = []
        self.HistoryFile = "../../Data/Logs/WarningHistory.json"
        self.CPUMax = 70
        self.GPUMax = 70
        self.MEMMax = 80
        self.DPCMax = 70
        self.DFRMax = 100
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
                av = str(sum(vs) / len(vs))
                self.Data["warn"][input].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + input + "-Inf: " + str(av) + "% used")
                if len(self.Data["warn"][input]) > 2:
                    for i in self.Data["warn"][input]:
                        vs.append(re.search(r'\d{1,3}', i).group(0))
                    av = str(sum(vs) / len(vs))
                    self.Data["warn"][input].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + input + "-Inf: " + str(av) + "% used")
                    sendEmail(socket.gethostname() + " - Crit", input + "-Crit: \n" + "Time: " + datetime.now().strftime("%d.%m.%Y %H:%M") + "\nValue: " + str(av) + "% used", ['craftzockerlp@gmail.com'])
                    self.History.append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + socket.gethostname() + " - Crit\n" + input + "-Crit: \n" + "Time: " + datetime.now().strftime("%d.%m.%Y %H:%M") + "\nValue: " + str(av) + "% used")
        else:
            if len(self.Data["info"][input]) > 2:
                vs = []
                for i in self.Data["info"][input]:
                    vs.append(re.search(r'\d{1,3}', i).group(0))
                av = str(sum(vs) / len(vs))
                self.Data["warn"][input].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + input, "-Inf: " + str(av) + "GB Free")
                if len(self.Data["warn"][input]) > 2:
                    for i in self.Data["warn"][input]:
                        vs.append(re.search(r'\d{1,3}', i).group(0))
                    av = str(sum(vs) / len(vs))
                    self.Data["warn"][input].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + input + "-Inf: " + str(av) + "GB Free")
                    sendEmail(socket.gethostname() + " - Crit", input + "-Crit: \n" + "Time: " + datetime.now().strftime("%d.%m.%Y %H:%M") + "\nValue: " + str(av) + "GB Free", ['craftzockerlp@gmail.com'])
                    self.History.append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + socket.gethostname() + " - Crit\n" + input + "-Crit: \n" + "Time: " + datetime.now().strftime("%d.%m.%Y %H:%M") + "\nValue: " + str(av) + "GB Free")

    def Loop(self):
        if isfile(self.fileName):
            try:
                with open(self.fileName, "r") as f:
                    self.Data = json.loads(f)
                with open(self.HistoryFile, "r") as f:
                    self.History = json.loads(f)
            except TypeError:
                print("Warn: No content in Warning/History File")
        while True:
            self.CPU = CPU_Precent()
            if self.CPU >= self.CPUMax:
                print("CPU Warning generated")
                self.Data["info"]["CPU"].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - CPU" + "-Inf: " + str(self.CPU) + "% used")
                self.checkLogs("CPU")
            self.GPU = GPU_Usage()
            if self.GPU >= self.GPUMax:
                print("GPU Warning generated")
                self.Data["info"]["GPU"].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - GPU" + "-Inf: " + str(self.GPU) + "% used")
                self.checkLogs("GPU")
            self.MEM = MEM_Precent()
            if self.MEM >= self.MEMMax:
                print("MEM Warning generated")
                self.Data["info"]["MEM"].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - MEM" + "-Inf: " + str(self.MEM) + "% used")
                self.checkLogs("MEM")
            self.DPC = DISK_Usage()
            if self.DPC >= self.DPCMax:
                print("DPC Warning generated")
                self.Data["info"]["DPC"].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - DPC" + "-Inf: " + str(self.DPC) + "% used")
                self.checkLogs("DPC")
            self.DFR = DISK_Free()
            if self.DFR <= self.DFRMax:
                print("DFR Warning generated")
                self.Data["info"]["DFR"].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - DFR" + "-Inf: " + str(self.DFR) + "GB Free")
                self.checkLogs("DFR")
            with open(self.fileName, "w") as f:
                json.dump(self.Data, f, indent=4)
            with open(self.HistoryFile, "w") as f:
                json.dump(self.History, f, indent=4)
            time.sleep(60)
