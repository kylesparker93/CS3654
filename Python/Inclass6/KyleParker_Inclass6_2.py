import xml.etree.ElementTree as et
import pandas as pd

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
	
df.describe

bins = [0, 14, 35, 49, 100]

df.TScore = pd.cut(df.TScore, bins)

pd.value_counts(df.TScore)

pref = {'(0, 14]':'Low scoring', '(14, 35]':'Average', '(35, 49]':'High scoring', '(49, 100]':'Blowout'}

df['Result'] = df['TScore'].map(pref)

df.rename(columns={'TScore':'Team Score', 'OScore':'Opponent Score'})

import numpy as np

sampler = np.random.permutation(119)
train = sampler[:60]
train_df1 = df.take(train)

sampler = np.random.permutation(119)
train = sampler[:60]
train_df2 = df.take(train)

df1 = pd.concat([train_df1, train_df2])
df1.drop_duplicates