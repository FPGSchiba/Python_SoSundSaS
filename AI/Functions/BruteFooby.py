#! Für Linux ausführung freihalten
# Author: Jann Erhardt
# Version 1.0.1
# Changes:
# ================
# No changes yet
# ================
# No Copy Right yet

import time
from Scrapper_Fooby import *

finished = False

for i in range(0,19478):
    ScrapFooby("fooby.ch/de/rezepte/{number}/?startAuto1=0".format(number=i))