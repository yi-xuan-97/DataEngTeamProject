import pandas as pd

data = pd.read_csv('data.csv')
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

data.to_csv('data.csv',index=False)
