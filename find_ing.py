import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Alt-Used": "www.ewg.org",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1"
}

with open('4_outer.txt', 'r') as file:
    ingrs = file.readlines()
    
lines = []

def test_ing(s):
    
    print(s)
    
    URL = "https://www.ewg.org/foodscores/products/?search=" + s

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    target = soup.find(id="showing")
    
    print(target is not None)
    
    if target is not None:
        return 'In'
    
    return 'Not In'

for i in ingrs:
    name = i.strip()
    lines.append(name + ' ' + test_ing(name) + '\n')
    # time.sleep(0.5)

with open('4_outer_out.txt', 'w') as file:
    file.writelines(lines)