import pandas as pd
import os
path= '/Users/yixuanfeng/Documents/Github/DataEngTeamProject/Assignment3/cars_record/'
filelist = os.listdir(path)
def validCarsRecord(filename):
    data = pd.read_csv(filename)
    data['stop_time'] =  data['stop_time'].fillna(method='ffill')
    data['x_coordinate'] =  data['x_coordinate'].fillna(method='ffill')
    data['y_coordinate'] =  data['y_coordinate'].fillna(method='ffill')

    data['direction'] = data['direction'].fillna(-999)
    data['location_id'] = data['location_id'].fillna(0)
    data['pattern_distance'] = data['pattern_distance'].fillna(-1)
    data['location_distance'] = data['location_distance'].fillna(-1)

    data.drop(['maximum_speed','service_key','door','lift','ons','offs','dwell'], axis=1,inplace=True)

    n = 2
    data.drop(data.tail(n).index,inplace = True)
    data['leave'] = pd.to_datetime(data['leave_time'],unit='s')
    data['stop'] = pd.to_datetime(data['stop_time'], unit='s')
    data['arrive'] = pd.to_datetime(data['arrive_time'], unit='s')
    data['leave'] = data['leave'].dt.time
    data['stop'] = data['stop'].dt.time
    data['arrive'] = data['arrive'].dt.time

    data.to_csv(filename,index=False)
for file in filelist:
    print(f'validating file: {path}{file}')
    validCarsRecord(f'{path}{file}')