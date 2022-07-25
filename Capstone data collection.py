from bs4 import BeautifulSoup
from io import BytesIO
import re

import requests, zipfile
r  = requests.get("https://www.retrosheet.org/game.htm")
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all("a"):
    if re.search("[1-9][0-9][0-9][0-9]eve.zip", str(link)) is not None:
        r = requests.get(link.get('href'), allow_redirects=True)
        filename = link.get('href').split('/')[-1]
        
        z = zipfile.ZipFile(BytesIO(r.content))
        z.extractall('C:/Users/warrenahossjr/Springboard/Capstone Project Data')
