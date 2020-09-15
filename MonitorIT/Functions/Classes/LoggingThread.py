import threading
import time
import datetime as DateTime
import json

from Functions.ScanHardware import *


class logging_Thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        print("Logging Started")

    def run(self):
        time.sleep(5)
        self.Loop()

    def Loop(self):
        while True:
            with open('data.json', 'w') as f:
                json.dump(data, f)
            print(DateTime.datetime.now())
            time.sleep(1)
