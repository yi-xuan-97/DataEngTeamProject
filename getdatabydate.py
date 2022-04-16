import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

serverip = '34.83.146.240'

def getJsonFromURL(url):
    s = requests.Session()
    print(f"Requesting URL : {url}")
    resp = s.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')
    data = json.loads(str(soup))
    return data
def getDataByDate(month, day):
    formatdate = datetime(2022, month, day).strftime('%Y-%m-%d')
    url = f'http://{serverip}/data/{formatdate}.json'
    data = getJsonFromURL(url)
    print(data)
# getDataByDate(4,11)
