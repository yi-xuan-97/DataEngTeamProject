import pandas as pd
import os
import datetime as dt


path = '/Users/zhengmao/Documents/Github/DataEngTeamProject/Assignment2/validData/'
filelist = os.listdir(path)

def covertdateToTimestamp(date):
    date_time_str = f'{date} 00:00:00'
    date_time_obj = dt.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    Timestamp = date_time_obj.timestamp()
    return int(Timestamp)
for file in filelist:
    df = pd.read_csv(path+file)
    timestamp = covertdateToTimestamp(file.split('.')[0])
    df['ACT_TIME'] = df['ACT_TIME'].map(lambda x : x+timestamp)
    df.to_csv(path+file)