import pandas as pd

df = pd.read_csv('./validData/2022-04-07.csv')
df.isnull().any()