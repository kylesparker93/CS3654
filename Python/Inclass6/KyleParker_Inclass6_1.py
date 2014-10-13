import pandas as pd

t1 = pd.read_table('work_tab.txt', sep='\t')
t2 = pd.read_csv('work_comma.csv')
t3 = pd.read_table('stress2_1.txt', sep='\t', skiprows=19)

t1
t2
t3


import json
import resuts

r = requests.get('https://api.github.com/events')
r

t = r.json()
fields = ['created_at','public','type','url']
data_fr = pd.DataFrame(t, columns = fields)
data_fr

data_fr.to_pickle('data_fr_pickle')
t1 = pd.read_pickle('data_fr_pickle')
t1

store = pd.HDFStore('mydata.h5')
store['obj1'] = t1

store['obj1']