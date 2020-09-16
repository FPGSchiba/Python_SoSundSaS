import threading
import time
import datetime as DateTime
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
        self.Loop()

    def cutFile(self, input, string):
        if input == "cpu":
            ret = re.match(r'CPU:\s(\s|\d)(\s|\d)\d', string)
            return re.match(r'\d+', ret)
        if input == "mem":
            ret = re.match(r'MEM:\s(\s|\d)(\s|\d)\d', string)
            return re.match(r'\d+', ret)
        if input == "gpu":
            ret = re.match(r'GPU:\s(\s|\d)(\s|\d)\d', string)
            return re.match(r'\d+', ret)
        if input == "dpc":
            ret = re.match(r'DPC:\s(\s|\d)(\s|\d)\d', string)
            return re.match(r'\d+', ret)
        if input == "dmx":
            ret = re.match(r'DMX:\s(\s|\d)(\s|\d)(\s|\d)(\s|\d)\d', string)
            return re.match(r'\d+', ret)
        if input == "dfr":
            ret = re.match(r'DFR:\s(\s|\d)(\s|\d)(\s|\d)(\s|\d)\d', string)
            return re.match(r'\d+', ret)

    def Loop(self):
        while True:
            with open('../../Data/Loggs.json', 'w') as f:
                self.data['Logg']['LoggPerTime']['Minute-Log'].append("{computername:15s} // {DateTime:10s} - CPU: {cpu:3f}% || MEM: {mem:3f}% || GPU: {gpu:3f}% || DPC: {dpc:3f}% || DMX: {dmx:5f}GB || DFR: {dfr:5f}GB".format(computername=socket.gethostname(), DateTime=DateTime.datetime.now(), cpu=CPU_Precent(), mem=MEM_Precent(), gpu=GPU_Usage(), dpc=DISK_Usage(), dmx=DISK_Max(), dfr=DISK_Free()))
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
                    cpuav = int(sum(cpus) / len(cpus))
                    memav = int(sum(mems) / len(mems))
                    gpuav = int(sum(gpus) / len(gpus))
                    dpcav = int(sum(dpcs) / len(dpcs))
                    dmxav = int(sum(dmxs) / len(dmxs))
                    dfrav = int(sum(dfrs) / len(dfrs))
                    self.data['Logg']['LoggPerTime']['Hour-Log'].append("{computername:s15} // {DateTime:10s} - CPU: {cpu:3f}% || MEM: {mem:3f}% || GPU: {gpu:3f}% || DPC: {dpc:3f}% || DMX: {dmx:5f}GB || DFR: {dfr:5f}GB".format(computername=socket.gethostname(), DateTime=DateTime.datetime.now(), cpu=cpuav, mem=memav, gpu=gpuav, dpc=dpcav, dmx=dmxav, dfr=dfrav))
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
                    cpuav = int(sum(cpus) / len(cpus))
                    memav = int(sum(mems) / len(mems))
                    gpuav = int(sum(gpus) / len(gpus))
                    dpcav = int(sum(dpcs) / len(dpcs))
                    dmxav = int(sum(dmxs) / len(dmxs))
                    dfrav = int(sum(dfrs) / len(dfrs))
                    self.data['Logg']['LoggPerTime']['Day-Log'].append("{computername:s15} // {DateTime:10s} - CPU: {cpu:3f}% || MEM: {mem:3f}% || GPU: {gpu:3f}% || DPC: {dpc:3f}% || DMX: {dmx:5f}GB || DFR: {dfr:5f}GB".format(computername=socket.gethostname(), DateTime=DateTime.datetime.now(), cpu=cpuav, mem=memav, gpu=gpuav, dpc=dpcav, dmx=dmxav, dfr=dfrav))
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
                    cpuav = int(sum(cpus) / len(cpus))
                    memav = int(sum(mems) / len(mems))
                    gpuav = int(sum(gpus) / len(gpus))
                    dpcav = int(sum(dpcs) / len(dpcs))
                    dmxav = int(sum(dmxs) / len(dmxs))
                    dfrav = int(sum(dfrs) / len(dfrs))
                    self.data['Logg']['LoggPerTime']['Week-Log'].append("{computername:s15} // {DateTime:10s} - CPU: {cpu:3f}% || MEM: {mem:3f}% || GPU: {gpu:3f}% || DPC: {dpc:3f}% || DMX: {dmx:5f}GB || DFR: {dfr:5f}GB".format(computername=socket.gethostname(), DateTime=DateTime.datetime.now(), cpu=cpuav, mem=memav, gpu=gpuav, dpc=dpcav, dmx=dmxav, dfr=dfrav))
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
                    cpuav = int(sum(cpus) / len(cpus))
                    memav = int(sum(mems) / len(mems))
                    gpuav = int(sum(gpus) / len(gpus))
                    dpcav = int(sum(dpcs) / len(dpcs))
                    dmxav = int(sum(dmxs) / len(dmxs))
                    dfrav = int(sum(dfrs) / len(dfrs))
                    self.data['Logg']['LoggPerTime']['Month-Log'].append("{computername:s15} // {DateTime:10s} - CPU: {cpu:3f}% || MEM: {mem:3f}% || GPU: {gpu:3f}% || DPC: {dpc:3f}% || DMX: {dmx:5f}GB || DFR: {dfr:5f}GB".format(computername=socket.gethostname(), DateTime=DateTime.datetime.now(), cpu=cpuav, mem=memav, gpu=gpuav, dpc=dpcav, dmx=dmxav, dfr=dfrav))
                    with open('../../Data/Loggs{mon:d4}.json'.format(mon=DateTime.now().date())) as outfile:
                        json.dump(self.data, outfile)
                    self.data.clear()
                json.dump(self.data, f)
            print("Log entry done: " + DateTime.datetime.now())
            time.sleep(60)
