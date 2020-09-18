import threading
import time
import datetime
import json
import socket
import re
from Functions.ScanHardware import *


class logging_Thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.data = {
            "Logg": {
                "LoggPerTime": {
                    "Minute-Log": [],
                    "Hour-Log": [],
                    "Day-Log": [],
                    "Week-Log": [],
                    "Month-Log": []
                }
            }
        }
        print("Logging Started")

    def run(self):
        time.sleep(5)
        self.read()
        self.Loop()

    def read(self):
        try:
            with open('../../Data/Loggs.json', 'r') as f:
                self.data = json.load(f)
        finally:
            return None

    def cutFile(self, input, string):
        if input == "cpu":
            ret = re.search(r'CPU:\s(\s|\d)(\s|\d)\d', string).group(0)
            return re.search(r'\d+', ret).group(0)
        if input == "mem":
            ret = re.search(r'MEM:\s(\s|\d)(\s|\d)\d', string).group(0)
            return re.search(r'\d+', ret).group(0)
        if input == "gpu":
            ret = re.search(r'GPU:\s(\s|\d)(\s|\d)\d', string).group(0)
            return re.search(r'\d+', ret).group(0)
        if input == "dpc":
            ret = re.search(r'DPC:\s(\s|\d)(\s|\d)\d', string).group(0)
            return re.search(r'\d+', ret).group(0)
        if input == "dmx":
            ret = re.search(r'DMX:\s(\s|\d)(\s|\d)(\s|\d)(\s|\d)\d', string).group(0)
            return re.search(r'\d+', ret).group(0)
        if input == "dfr":
            ret = re.search(r'DFR:\s(\s|\d)(\s|\d)(\s|\d)(\s|\d)\d', string).group(0)
            return re.search(r'\d+', ret).group(0)

    def Loop(self):
        while True:
            with open('../../Data/Loggs.json', 'w') as f:
                self.data['Logg']['LoggPerTime']['Minute-Log'].append("{computername:15s} // {datetime:10s} - CPU: {cpu:3.0f}% || MEM: {mem:3.0f}% || GPU: {gpu:3.0f}% || DPC: {dpc:3.0f}% || DMX: {dmx:5.0f}GB || DFR: {dfr:5.0f}GB".format(computername=socket.gethostname(), datetime=str(datetime.datetime.now().date()), cpu=CPU_Precent(), mem=MEM_Precent(), gpu=GPU_Usage(), dpc=DISK_Usage(), dmx=DISK_Max(), dfr=DISK_Free()))
                if self.data['Logg']['LoggPerTime']['Minute-Log'].__len__() >= 60:
                    cpus = []
                    mems = []
                    gpus = []
                    dpcs = []
                    dmxs = []
                    dfrs = []
                    for i in self.data['Logg']['LoggPerTime']['Minute-Log']:
                        cpus.append(int(self.cutFile("cpu", i)))
                        mems.append(int(self.cutFile("mem", i)))
                        gpus.append(int(self.cutFile("gpu", i)))
                        dpcs.append(int(self.cutFile("dpc", i)))
                        dmxs.append(int(self.cutFile("dmx", i)))
                        dfrs.append(int(self.cutFile("dfr", i)))
                    cpuav = sum(cpus) / len(cpus)
                    memav = sum(mems) / len(mems)
                    gpuav = sum(gpus) / len(gpus)
                    dpcav = sum(dpcs) / len(dpcs)
                    dmxav = sum(dmxs) / len(dmxs)
                    dfrav = sum(dfrs) / len(dfrs)
                    self.data['Logg']['LoggPerTime']['Minute-Log'].clear()
                    self.data['Logg']['LoggPerTime']['Hour-Log'].append("{computername:15s} // {datetime:10s} - CPU: {cpu:3.0f}% || MEM: {mem:3.0f}% || GPU: {gpu:3.0f}% || DPC: {dpc:3.0f}% || DMX: {dmx:5.0f}GB || DFR: {dfr:5.0f}GB".format(computername=socket.gethostname(), datetime=str(datetime.datetime.now().date()), cpu=cpuav, mem=memav, gpu=gpuav, dpc=dpcav, dmx=dmxav, dfr=dfrav))
                if self.data['Logg']['LoggPerTime']['Hour-Log'].__len__() >= 24:
                    cpus = []
                    mems = []
                    gpus = []
                    dpcs = []
                    dmxs = []
                    dfrs = []
                    for i in self.data['Logg']['LoggPerTime']['Hour-Log']:
                        cpus.append(int(self.cutFile("cpu", i)))
                        mems.append(int(self.cutFile("mem", i)))
                        gpus.append(int(self.cutFile("gpu", i)))
                        dpcs.append(int(self.cutFile("dpc", i)))
                        dmxs.append(int(self.cutFile("dmx", i)))
                        dfrs.append(int(self.cutFile("dfr", i)))
                    cpuav = sum(cpus) / len(cpus)
                    memav = sum(mems) / len(mems)
                    gpuav = sum(gpus) / len(gpus)
                    dpcav = sum(dpcs) / len(dpcs)
                    dmxav = sum(dmxs) / len(dmxs)
                    dfrav = sum(dfrs) / len(dfrs)
                    self.data['Logg']['LoggPerTime']['Hour-Log'].clear()
                    self.data['Logg']['LoggPerTime']['Day-Log'].append("{computername:15s} // {datetime:10s} - CPU: {cpu:3.0f}% || MEM: {mem:3.0f}% || GPU: {gpu:3.0f}% || DPC: {dpc:3.0f}% || DMX: {dmx:5.0f}GB || DFR: {dfr:5.0f}GB".format(computername=socket.gethostname(), datetime=str(datetime.datetime.now().date()), cpu=cpuav, mem=memav, gpu=gpuav, dpc=dpcav, dmx=dmxav, dfr=dfrav))
                if self.data['Logg']['LoggPerTime']['Day-Log'].__len__() >= 7:
                    cpus = []
                    mems = []
                    gpus = []
                    dpcs = []
                    dmxs = []
                    dfrs = []
                    for i in self.data['Logg']['LoggPerTime']['Day-Log']:
                        cpus.append(int(self.cutFile("cpu", i)))
                        mems.append(int(self.cutFile("mem", i)))
                        gpus.append(int(self.cutFile("gpu", i)))
                        dpcs.append(int(self.cutFile("dpc", i)))
                        dmxs.append(int(self.cutFile("dmx", i)))
                        dfrs.append(int(self.cutFile("dfr", i)))
                    cpuav = sum(cpus) / len(cpus)
                    memav = sum(mems) / len(mems)
                    gpuav = sum(gpus) / len(gpus)
                    dpcav = sum(dpcs) / len(dpcs)
                    dmxav = sum(dmxs) / len(dmxs)
                    dfrav = sum(dfrs) / len(dfrs)
                    self.data['Logg']['LoggPerTime']['Day-Log'].clear()
                    self.data['Logg']['LoggPerTime']['Week-Log'].append("{computername:15s} // {datetime:10s} - CPU: {cpu:3.0f}% || MEM: {mem:3.0f}% || GPU: {gpu:3.0f}% || DPC: {dpc:3.0f}% || DMX: {dmx:5.0f}GB || DFR: {dfr:5.0f}GB".format(computername=socket.gethostname(), datetime=str(datetime.datetime.now().date()), cpu=cpuav, mem=memav, gpu=gpuav, dpc=dpcav, dmx=dmxav, dfr=dfrav))
                if self.data['Logg']['LoggPerTime']['Week-Log'].__len__() >= 4:
                    cpus = []
                    mems = []
                    gpus = []
                    dpcs = []
                    dmxs = []
                    dfrs = []
                    for i in self.data['Logg']['LoggPerTime']['Week-Log']:
                        cpus.append(int(self.cutFile("cpu", i)))
                        mems.append(int(self.cutFile("mem", i)))
                        gpus.append(int(self.cutFile("gpu", i)))
                        dpcs.append(int(self.cutFile("dpc", i)))
                        dmxs.append(int(self.cutFile("dmx", i)))
                        dfrs.append(int(self.cutFile("dfr", i)))
                    cpuav = sum(cpus) / len(cpus)
                    memav = sum(mems) / len(mems)
                    gpuav = sum(gpus) / len(gpus)
                    dpcav = sum(dpcs) / len(dpcs)
                    dmxav = sum(dmxs) / len(dmxs)
                    dfrav = sum(dfrs) / len(dfrs)
                    self.data['Logg']['LoggPerTime']['Week-Log'].clear()
                    self.data['Logg']['LoggPerTime']['Month-Log'].append("{computername:15s} // {datetime:10s} - CPU: {cpu:3.0f}% || MEM: {mem:3.0f}% || GPU: {gpu:3.0f}% || DPC: {dpc:3.0f}% || DMX: {dmx:5.0f}GB || DFR: {dfr:5.0f}GB".format(computername=socket.gethostname(), datetime=str(datetime.datetime.now().date()), cpu=cpuav, mem=memav, gpu=gpuav, dpc=dpcav, dmx=dmxav, dfr=dfrav))
                    with open(f'../../Data/Loggs{datetime.datetime.now().date()}.json', 'w') as outfile:
                        json.dump(self.data, outfile, indent=4)
                    self.data['Logg']['LoggPerTime']['Minute-Log'].clear()
                    self.data['Logg']['LoggPerTime']['Hour-Log'].clear()
                    self.data['Logg']['LoggPerTime']['Day-Log'].clear()
                    self.data['Logg']['LoggPerTime']['Month-Log'].clear()
                json.dump(self.data, f, indent=4)
            print("Log entry done: " + str(str(datetime.datetime.now())))
            time.sleep(59.99)
