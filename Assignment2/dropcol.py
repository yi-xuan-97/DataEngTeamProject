import pandas as pd
import numpy as np
import os
path = '/Users/zhengmao/Documents/Github/DataEngTeamProject/data/storage/'
filelist = os.listdir(path)

for file in filelist:
    print(f'Trying to vali file: {file}')
    df = pd.read_json(path+file)
    df.drop(columns=['RADIO_QUALITY'],inplace=True)
    filename = file.split('.')
    df.to_csv(f'./validData/{filename[0]}.csv')