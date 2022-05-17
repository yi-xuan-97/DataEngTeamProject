import pandas as pd

data = pd.read_csv('2022-04-07.csv')
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

data.to_csv('2022-04-07.csv')

def line_prepender(filename,line):
    with open(filename, 'r+') as f:
        content = f.read()
        if content.startswith(","):
            f.seek(0, 0)
            f.write(line.rstrip('\r') + content)

line_prepender('2022-04-07.csv',"INDEX")