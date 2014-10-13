import pandas as pd

# 3
t1 = pd.read_table('work_tab.txt', sep='\t')
t2 = pd.read_csv('work_comma.csv')
t3 = pd.read_table('stress2_1.txt', sep='\t', skiprows=19)

t1
t2
t3


import json
import resuts

# 4
r = requests.get('https://api.github.com/events')
r

t = r.json()
fields = ['created_at','public','type','url']
data_fr = pd.DataFrame(t, columns = fields)
data_fr

# 5
data_fr.to_pickle('data_fr_pickle')
t1 = pd.read_pickle('data_fr_pickle')
t1

# 6
store = pd.HDFStore('mydata.h5')
store['obj1'] = t1

store['obj1']


# 1
import xml.etree.ElementTree as et

file = 'cfb20130831.xml'
xml = et.parse(file)
root = xml.getroot()

games = root.getchildren()

df = pd.DataFrame(columns=('Team', 'TScore', 'Opponent', 'OScore'))

i = 0
for team in games:
	row = dict(zip(['Team', 'TScore', 'Opponent', 'OScore'], [team[1][0].text, int(team[1].find('offense')[0].text), team[1].find('opponent').text, int(team[1].find('defense')[0].text)]))
	row_s = pd.Series(row)
	row_s.name = i
	df = df.append(row_s)
	i += 1

# 2
df.describe

# 3
bins = [0, 14, 35, 49, 100]

df.TScore = pd.cut(df.TScore, bins)

# 4
pd.value_counts(df.TScore)

# 5
pref = {'(0, 14]':'Low scoring', '(14, 35]':'Average', '(35, 49]':'High scoring', '(49, 100]':'Blowout'}

df['Result'] = df['TScore'].map(pref)

# 6
df.rename(columns={'TScore':'Team Score', 'OScore':'Opponent Score'})

# 7
import numpy as np

sampler = np.random.permutation(119)
train = sampler[:60]
train_df1 = df.take(train)

# 8
sampler = np.random.permutation(119)
train = sampler[:60]
train_df2 = df.take(train)

# 9
df1 = pd.concat([train_df1, train_df2])
df1.drop_duplicates