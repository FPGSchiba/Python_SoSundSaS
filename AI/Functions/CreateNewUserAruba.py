#! Für Linux ausführung freihalten
# Author: Jann Erhardt
# Version 1.0.0
# Changes:
# ================
# No changes yet
# ================
# No Copy Right yet

import requests
from bs4 import *
from Functions.Scrapper import Scrapper_Fooby
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "80",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "SESSION=",
    "Host": "aruba01.apgsga.ch:4343",
    "Origin": "https://aruba01.apgsga.ch:4343",
    "Referer": "https://aruba01.apgsga.ch:4343/screens/switch/gpp.html",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}

login_data = {
    "opcode": "login",
    "url": "/screens/switch/gpp.html",
    "needxml": "0",
    "uid": "zhg",
    "passwd": "Empfang"
}


def CreateNewUser():
    with requests.Session() as s:

        url = "https://aruba01.apgsga.ch:4343/screens/cmnutil/gc_data.xml"
        r = s.post(url, verify=True, cert=["C:\\CertificateAruba.cer", "C:\\CertificateAruba.cer"], data=login_data, headers=headers)

        HTTPResponse = requests.packages.urllib3.response.HTTPResponse
        orig_HTTPResponse__init__ = HTTPResponse.__init__

        def new_HTTPResponse__init__(self, *args, **kwargs):
            orig_HTTPResponse__init__(self, *args, **kwargs)
            try:
                self.peercert = self._connection.sock.getpeercert()
            except AttributeError:
                pass

        HTTPResponse.__init__ = new_HTTPResponse__init__

        HTTPAdapter = requests.adapters.HTTPAdapter
        orig_HTTPAdapter_build_response = HTTPAdapter.build_response

        def new_HTTPAdapter_build_response(self, request, resp):
            response = orig_HTTPAdapter_build_response(self, request, resp)
            try:
                response.peercert = resp.peercert
            except AttributeError:
                pass
            return response

        HTTPAdapter.build_response = new_HTTPAdapter_build_response
        print(r.content)
