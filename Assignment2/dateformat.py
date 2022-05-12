from lib2to3.pytree import convert
from sqlite3 import Timestamp
import pandas as pd
import os
import datetime as dt

# path = '/Users/zhengmao/Documents/Github/DataEngTeamProject/Assignment2/validData/'
# filelist = os.listdir(path)
# df = pd.read_csv(path+'2022-04-07.csv')
# df
# now = datetime.now()

# date_time = '2022-04-07 00:00:00'
# date_time_obj = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
# timestamp = datetime.timestamp(date_time)
path = '/Users/zhengmao/Documents/Github/DataEngTeamProject/Assignment2/validData/'
filelist = os.listdir(path)

def covertdateToTimestamp(date):
    date_time_str = f'{date} 00:00:00'
    date_time_obj = dt.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    Timestamp = date_time_obj.timestamp()
    print(int(Timestamp))
for file in filelist:
    covertdateToTimestamp(file.split('.')[0])