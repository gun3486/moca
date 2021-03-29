import requests
from bs4 import BeautifulSoup
import datetime

present = str(datetime.datetime.now())
print(present)
date = present[:4] + present[5:7] + present[8:10] 
print(date)

req = requests.get("http://gsm.gen.hs.kr/xboard/board.php?tbnum=8")
soup = BeautifulSoup(req.text, "html.parser")
print(soup)