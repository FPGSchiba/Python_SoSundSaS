import argparse
import os.path

import pandas as pd
import requests

from bs4 import BeautifulSoup

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
        "vcp"
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
        "line"
    ]
}

UNKNOWN_WORD = "– (∅ o)"

DICTIONARY_URL = 'https://robertsspaceindustries.com/comm-link/spectrum-dispatch/16202-Xian-Dictionary'


def download_rsi(args: argparse.Namespace):
    if not os.path.isdir(args.folder):
        os.mkdir(args.folder)

    content = requests.get(DICTIONARY_URL).content
    soup = BeautifulSoup(content, "html.parser")

    table_bodies = soup.findAll('tbody')
    dictionary = table_bodies[1]
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

    for record in dictionary.find_all_next('tr'):
        word = record.find_all_next('td')[0].text.replace('<strong>', '').replace('</strong>', '').strip()
        if UNKNOWN_WORD in word:
            continue
        pos = record.find_all_next('td')[1].text.replace('<strong>', '').replace('</strong>', '')
        formatted_pos = pos
        if pos[-1] == '.':
            formatted_pos = pos[0:-1]
        translation = record.find_all_next('td')[2].text.replace('<strong>', '').replace('</strong>', '')

        if formatted_pos in groupings['mandatory']:
            output['mandatory']['words'].append(word)
            output['mandatory']['translations'].append(translation)
        elif formatted_pos in groupings['auxiliary']:
            output['auxiliary']['words'].append(word)
            output['auxiliary']['translations'].append(translation)
        else:
            print(f'New POS: "{formatted_pos}" found, please insert into grouping.')

    for group in output:
        df = pd.DataFrame(output[group])
        df.to_csv(f'{args.folder}/{group}.csv', index=False)
    print(f"Safed Xi'an dictionary to: {args.folder}")
