#! Für Linux ausführung freihalten
# Author: Jann Erhardt
# Version 1.0.1
# Changes:
# ================
# No changes yet
# ================
# No Copy Right yet

import time
from Functions import Scrapper_Fooby

finished = False

for i in range(5100,20000):
    print("https://fooby.ch/de/rezepte/{number}/?startAuto1=0".format(number=i))
    Scrapper_Fooby.ScrapFooby("https://fooby.ch/de/rezepte/{number}/?startAuto1=0".format(number=i))