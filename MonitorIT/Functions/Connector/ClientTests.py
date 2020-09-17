# Import socket module
import json
import re
import socket

from datetime import datetime
date_object = str(datetime.now().date())

with open('../../Data/Loggs.json', 'r') as f:
    data = json.load(f)

data = ["ws565           // 2020-09-17 - CPU:   2% || MEM:  58% || GPU:   0% || DPC:  31% || DMX:   292GB || DFR:   201GB"]


def cutFile(string):
    ret = re.search(r'CPU:\s(\s|\d)(\s|\d)\d', string).group(0)
    ret = re.search(r'\d+', ret).group(0)
    return ret

cpus = []
for i in data:
    cpus.append(int(cutFile(i)))
cpuav = sum(cpus) / len(cpus)

print(cpuav)
