import os
import sys
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
import json
from alive_progress import alive_bar

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome("./Driver/chromedriver.exe")
driver.set_window_position(-10000, 0)
driver.get("https://animeflix.nl/watch/fairy-tail-dub-bg9m-episode-18/")

header_vid = {
    "authority": "vidstream.pro",
    "method": "GET",
    "path": "/e/48YZ6R0XMY2X?domain=animeflix.nl",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, utf-8",
    "accept-language": "en-US,en;q=0.9",
    "referer": "https://animeflix.nl/",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "iframe",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}

header_skey = {
    "authority": "vidstream.pro",
    "method": "GET",
    "path": "/info/48YZ6R0XMY2X?domain=animeflix.nl&skey=",
    "scheme": "https",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, utf-8",
    "accept-language": "en-US,en;q=0.9,de;q=0.8",
    "referer": "https://vidstream.pro/e/48YZ6R0XMY2X?domain=animeflix.nl",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

Anime_Names = []
episode_links = []
videos = []
Anime_Name = ""
Video_Dir = "D:\\Videos\\"

for episode in soup.findAll("a", attrs={"class": "nav-link btn btn-sm btn-secondary eps-item"}):
    episode_links.append(episode.get("href"))
    Anime_Names.append(re.sub("ANIMEFLIX", "", episode.get("title")))
    Anime_Name = re.sub("ANIMEFLIX Episode \d+", "", episode.get("title"))

Data_Dir = Video_Dir + Anime_Name + "\\"
if not os.path.isdir(Data_Dir):
    os.mkdir(Data_Dir)

for episode_link_id in range(len(episode_links)):
    driver.get(episode_links[episode_link_id])
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    Episode_Name = Anime_Names[episode_link_id]
    for video_link in soup.findAll("a", attrs={"class": "nav-link btn btn-sm btn-secondary link-item"}):
        link = video_link.get("data-embed")
        if "vidstream" in link:
            r_skey = requests.get(link, headers=header_vid, stream=True)
            vid_soup = BeautifulSoup(r_skey.content, "html.parser")
            skey = ""
            for script in vid_soup.findAll("script"):
                if len(script) >= 1:
                    if "window.skey" in script.contents[0]:
                        skey = str(script.contents[0]).replace("window.skey = '", "")
                        skey = skey.replace("';", "")
            link += "&skey=" + skey
            link = str(link).replace("/e/", "/info/")
            header_skey["path"] = "/info/48YZ6R0XMY2X?domain=animeflix.nl&skey=" + skey
            r_vid = requests.get(link, headers=header_skey)
            vid_json = json.loads(r_vid.text)
            remote_list = ""
            file_name = Data_Dir + Episode_Name.replace(Anime_Name, "").replace(" E", "E").replace(" ", "_") + ".mp4"
            if not os.path.isfile(file_name):
                for file_id in range(len(vid_json["media"]["sources"])):
                    if ".m3u8" in vid_json["media"]["sources"][file_id]["file"]:
                        remote_list = vid_json["media"]["sources"][file_id]["file"]

                r_list = requests.get(remote_list)
                remote_list_res = r_list.text
                resolution = "hls/360/360.m3u8"

                if "hls/1080/1080.m3u8" in remote_list_res:
                    resolution = "hls/1080/1080.m3u8"
                    remote_file = remote_list.replace("list.m3u8", resolution)
                elif "hls/720/720.m3u8" in remote_list_res:
                    resolution = "hls/720/720.m3u8"
                    remote_file = remote_list.replace("list.m3u8", resolution)
                elif "hls/480/480.m3u8" in remote_list_res:
                    resolution = "hls/480/480.m3u8"
                    remote_file = remote_list.replace("list.m3u8", resolution)
                else:
                    remote_file = remote_list.replace("list.m3u8", resolution)

                r_ep_list = requests.get(remote_file)
                lines = r_ep_list.text.split("\n")
                ts_list = []
                for line in lines:
                    if ".ts" in line:
                        if resolution == "hls/1080/1080.m3u8":
                            ts_list.append(remote_file.replace("1080.m3u8", line))
                        elif resolution == "hls/720/720.m3u8":
                            ts_list.append(remote_file.replace("720.m3u8", line))
                        elif resolution == "hls/480/480.m3u8":
                            ts_list.append(remote_file.replace("480.m3u8", line))
                        else:
                            ts_list.append(remote_file.replace("360.m3u8", line))


                def download():
                    for ts_url in ts_list:
                        ts = requests.get(ts_url).content
                        while len(ts) % 16 != 0:
                            ts += b"0"
                        with open(file_name, "ab") as file:
                            file.write(ts)
                        yield


                with alive_bar(len(ts_list), title=Episode_Name, bar="classic") as bar:
                    for i in download():
                        bar()
            else:
                print("Skipping Episode: " + Episode_Name)

print("Downloaded Series: " + Anime_Name)
driver.close()
