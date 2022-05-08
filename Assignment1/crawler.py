import requests
from bs4 import BeautifulSoup
import json
import wget
def getJsonFromURL(url):
    s = requests.Session()
    print(f"Requesting URL : {url}")
    resp = s.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')
    data = json.loads(str(soup))
    return data

url = 'http://www.psudataeng.com:8000/getBreadCrumbData'
data = getJsonFromURL(url)
fileName = wget.download(url)
print(fileName)