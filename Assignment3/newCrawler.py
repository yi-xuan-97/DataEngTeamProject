import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree

pageurl = 'http://www.psudataeng.com:8000/getStopEvents/'
s = requests.Session()
resp = s.get(url = pageurl)
soup = BeautifulSoup(resp.text,'html.parser')
allTable = soup.find_all('table')
print(len(allTable))
records = []
def tableformtodict(table):
    s = str(table)
    table = etree.HTML(s).find("body/table")
    rows = iter(table)
    headers = [col.text for col in next(rows)]
    for row in rows:
        values = [col.text for col in row]
        records.append(dict(zip(headers, values)))
for table in allTable:
    tableformtodict(table)
df = pd.DataFrame(records)
df.to_csv('data.csv', index=False)