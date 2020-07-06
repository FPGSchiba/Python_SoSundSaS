#! Für Linux ausführung freihalten
# Author: Jann Erhardt
# Version 1.0.1
# Changes:
# ================
# No changes yet
# ================
# No Copy Right yet

import requests
from bs4 import BeautifulSoup
from Functions.Scrapper import Scrapper_Fooby


def GetRandomPW(Len=8):

    if Len < 6:
        Len = 6
        print("es geht nicht kürzer als 6")
    elif Len > 24:
        Len = 24
        print("es geht nicht länger als 24")

    URL = "https://www.random.org/passwords/?num=1&len={len:d}&format=html&rnd=new".format(len=Len)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    allli = soup.find_all("li")
    end = Scrapper_Fooby.deleteTagsEinzel(allli[-1])
    return end
