import numpy as np 
import pandas as pd 

# step 1: Add a new column with the key 'Team' and all column values should be 'BOS'

# step 2: Group by the 'Team' column and get total home runs and rbi's

# Produce data for both 2017 and 2018 (ie print both seperated by a newline character \n)

"""
TEAM    HR   RBI
----------------
BOS     144  538
"""

bs2018['Team']='BOS'
bs2018['Year']='2018'
bs2018['TeamHR']= sum(bs2018['HR'])
bs2018['TeamRBI']= sum(bs2018['RBI'])
bs2017['Team']='BOS'
bs2017['Year']='2017'
bs2017['TeamHR']= sum(bs2017['HR'])
bs2017['TeamRBI']= sum(bs2017['RBI'])

bs2018_stats = bs2018.groupby(['Year']).agg({'HR': "sum", "RBI": "sum"})
bs2017_stats = bs2017.groupby(['Year']).agg({'HR': "sum", "RBI": "sum"})

bs2017_stats, bs2018_stats

yearbyyearstats = pd.concat([bs2017_stats, bs2018_stats], axis=0)

yearbyyearstats




# Find the average age of runners in the 2017 Boston Marathon

marathon_data = pd.read_csv('boston_marathon2017_edited.csv')
marathon_data['Age'].mean()