import pandas as pd
import os
path = '/Users/zhengmao/Documents/Github/DataEngTeamProject/validData/'
filelist = os.listdir(path)
for file in filelist:
    print(f"Replacing {file}")
    df = pd.read_csv(path+file)
    # GPS_LONGITUDE          True
    # GPS_LATITUDE           True
    # GPS_SATELLITES         True
    # GPS_HDOP               True
    values = {'VELOCITY' : -1, 'DIRECTION': -1,'SCHEDULE_DEVIATION': -99999,
             'GPS_LONGITUDE': 0, 'GPS_LATITUDE': 0, 'GPS_SATELLITES': 0, 'GPS_HDOP':0
            }
    df.fillna(value= values, inplace=True)
    df.to_csv(path+file)