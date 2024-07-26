import requests
from bs4 import BeautifulSoup

import json


url ="""https://www.tiktok.com/@fazsentidoh/video/7380861803556900102"""

headers= {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36"
}

const_id = "__UNIVERSAL_DATA_FOR_REHYDRATION__"
data_key = "webapp.video-detail"

session = requests.Session()

result = session.get(url,headers=headers,allow_redirects=True)

data= BeautifulSoup(result.content,"lxml")

scp = data.find(name="script",attrs={"id":const_id}).text
data_json = json.loads(scp)

data_result = data_json["__DEFAULT_SCOPE__"][data_key]
url_video = data_result["itemInfo"]["itemStruct"]["video"]["playAddr"]

with session.get(url_video, stream=True) as r:
    r.raise_for_status()
    with open("video.mp4", 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192): 
            
            f.write(chunk)