import argparse
import os.path
import re
import time

import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.service import Service

service = Service(binary_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome(service=service)

driver.set_window_position(-99999999, 0)


def parse_elements(element_array):
    word_and_pos = element_array[0]
    translation = element_array[1].text
    word_and_pos = re.sub(r'<span.+>', '', str(word_and_pos))
    pos = re.search(r'(?<=;">)(.*)(?=<\/small>)', str(word_and_pos)).group(0)
    word = re.sub(r'(<small.+>|<br\/>|<td.+>|<\/td>)', '', str(word_and_pos)).strip()
    words = re.split(r'\n\s+', word)
    return " | ".join(words), pos, translation


groupings = {
    "mandatory": [
        "chj",
        "cnj",
        "col",
        "con.CAS",
        "con.FOR",
        "con.SEMFOR",
        "deix",
        "eim.CMP",
        "elm.CMP",
        "eml.CMP",
        "elm",
        "elm.SRV",
        "idm",
        "n",
        "name",
        "nlz.CLTC",
        "noun",
        "num",
        "pn.NEU",
        "pn.REV",
        "pn.REV.for",
        "PN.role",
        "Q",
        "Q.sffx",
        "rel",
        "v.NEU",
        "v.REV",
        "vcp",
        "v.neg",
        "v.NEG",
        "vcp.CAS",
        "location",
        "idm.PEJ",
        "elm.CMP.REV"
    ],
    "auxiliary": [
        "coj",
        "elm.CMP.for",
        "nlz",
        "pn",
        "PN",
        "PN.feml",
        "PN.male",
        "pn.PEJ",
        "pn.SRV",
        "slng.GEN",
        "slng.SRV",
        "v.FAM",
        "v.IMP",
        "v.LAUD",
        "v.PEJ",
        "line",
        "vcp.FOR",
        "abbr.FOR",
        "TITLE.hon.arch",
        "num.ORD",
        "PN.male.al",
        "elm.IMP",
        "elm.CMP.prfx",
        "pn.hon.IMP",
        "PN.feml.al",
        "line.al"
    ]
}

UNKNOWN_WORD = "– (∅ o)"

DICTIONARY_URL = 'https://xian-dictionary.ueexi.com/'


def download_ueexi(args: argparse.Namespace):
    driver.get(DICTIONARY_URL)
    driver.implicitly_wait(10)
    time.sleep(10)
    if not os.path.isdir(args.folder):
        os.mkdir(args.folder)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    table_body = soup.findAll('table')[0]
    output = {
        "mandatory": {
            "words": [],
            "translations": []
        },
        "auxiliary": {
            "words": [],
            "translations": []
        }
    }

    for record in table_body.find_all_next('tr'):
        word, pos, translation = parse_elements(record.findChildren('td', attrs={"class": "user-selectable"}))
        if UNKNOWN_WORD in word:
            continue
        formatted_pos = pos
        if pos[-1] == '.':
            formatted_pos = pos[0:-1]

        if formatted_pos in groupings['mandatory']:
            output['mandatory']['words'].append(word)
            output['mandatory']['translations'].append(translation)
        elif formatted_pos in groupings['auxiliary']:
            output['auxiliary']['words'].append(word)
            output['auxiliary']['translations'].append(translation)
        else:
            print(f'New POS: "{formatted_pos}" with word: "{word}" and translation: "{translation}" found, please '
                  f'insert into grouping.')

    for group in output:
        df = pd.DataFrame(output[group])
        df.to_csv(f'{args.folder}/{group}.csv', index=False)
    print(f"Safed Xi'an dictionary to: {args.folder}")
    driver.close()


if __name__ == '__main__':
    args = argparse.Namespace(folder="./test")
    download_ueexi(args)
