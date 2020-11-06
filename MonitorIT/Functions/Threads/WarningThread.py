import datetime
import json
import re
import threading
import time
from os.path import isfile
from Functions.Information.ScanHardware import *
from Functions.Util.CritMail import *
import socket


class warning_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sett = settings()
        self.fileName = "../Data/Logs/WarningLogs.json"
        self.Data = {"info": {"CPU": [], "GPU": [], "MEM": [], "DPC": [], "DMX": [], "DFR": []}, "warn": {"CPU": [], "GPU": [], "MEM": [], "DPC": [], "DMX": [], "DFR": []}, "crit": {"CPU": [], "GPU": [], "MEM": [], "DPC": [], "DMX": [], "DFR": []}}
        self.History = []
        self.HistoryFile = "../Data/Logs/WarningHistory.json"
        self.CPUMax = self.sett.GetWarnCPU()
        self.GPUMax = self.sett.GetWarnGPU()
        self.MEMMax = self.sett.GetWarnMEM()
        self.DPCMax = self.sett.GetWarnDPC()
        self.DFRMax = self.sett.GetWarnDFR()
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
                    vs.append(re.search(r' \d{1,3}\.\d{1}', i).group(0))
                temps = [float(i) for i in vs]
                av = sum(temps) / len(temps)
                self.Data["warn"][input].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + input + "-Inf: " + str(av) + "% used")
                self.Data["info"][input] = []
                if len(self.Data["warn"][input]) > 2:
                    for i in self.Data["warn"][input]:
                        vs.append(re.search(r' \d{1,3}\.\d{1}', i).group(0))
                    temps = [float(i) for i in vs]
                    av = sum(temps) / len(temps)
                    self.Data["crit"][input].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + input + "-Inf: " + str(av) + "% used")
                    self.Data["warn"][input] = []
                    sendEmail(input + "-Crit: \n" + "Time: " + datetime.now().strftime("%d.%m.%Y %H:%M") + "\nValue: " + str(av) + "% used")
                    self.History.append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + socket.gethostname() + " - Crit\n" + input + "-Crit: \n" + "Time: " + datetime.now().strftime("%d.%m.%Y %H:%M") + "\nValue: " + str(av) + "% used")
        else:
            if len(self.Data["info"][input]) > 2:
                vs = []
                for i in self.Data["info"][input]:
                    vs.append(re.search(r' \d{1,3}\.\d{1}', i).group(0))
                temps = [float(i) for i in vs]
                av = sum(temps) / len(temps)
                self.Data["warn"][input].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + input, "-Inf: " + str(av) + "GB Free")
                if len(self.Data["warn"][input]) > 2:
                    for i in self.Data["warn"][input]:
                        vs.append(re.search(r' \d{1,3}\.\d{1}', i).group(0))
                    temps = [float(i) for i in vs]
                    av = sum(temps) / len(temps)
                    self.Data["crit"][input].append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + input + "-Inf: " + str(av) + "GB Free")
                    sendEmail(input + "-Crit: \n" + "Time: " + datetime.now().strftime("%d.%m.%Y %H:%M") + "\nValue: " + str(av) + "GB Free")
                    self.History.append(datetime.now().strftime("%d.%m.%Y %H:%M") + " - " + socket.gethostname() + " - Crit\n" + input + "-Crit: \n" + "Time: " + datetime.now().strftime("%d.%m.%Y %H:%M") + "\nValue: " + str(av) + "GB Free")

    def Loop(self):
        if isfile(self.fileName):
            try:
                with open(self.fileName, "r") as f:
                    self.Data = json.load(f)
                with open(self.HistoryFile, "r") as f:
                    self.History = json.load(f)
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
