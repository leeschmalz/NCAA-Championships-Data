#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np


# In[11]:


df = pd.read_csv('cons_285_df.csv')


# In[12]:


df['BonusPoints'] = np.zeros(33)
df['AdvPoints'] = np.zeros(33)
df['PlacementPoints'] = np.zeros(33)


# In[13]:


df


# In[14]:


for i in range(0,33):
    if df['ConsRound2'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
    if df['ConsRound2'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
    if df['ConsRound2'][i] == 'Fall' or df['ConsRound2'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2

for i in range(0,33):
    if df['ConsRound3'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
    if df['ConsRound3'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
    if df['ConsRound3'][i] == 'Fall' or df['ConsRound3'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2

for i in range(0,33):
    if df['ConsRound4'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
    if df['ConsRound4'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
    if df['ConsRound4'][i] == 'Fall' or df['ConsRound4'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2
        
for i in range(0,33):
    if df['ConsRound5'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
    if df['ConsRound5'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
    if df['ConsRound5'][i] == 'Fall' or df['ConsRound5'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2

for i in range(0,33):
    if df['ConsRound6'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
    if df['ConsRound6'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
    if df['ConsRound6'][i] == 'Fall' or df['ConsRound6'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2

for i in range(0,32):
    if df['ThirdPlace'][i] == 'Dec' or df['ThirdPlace'][i] == 'SV':
        df['PlacementPoints'][i] = 10
    if df['ThirdPlace'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
        df['PlacementPoints'][i] = 10
    if df['ThirdPlace'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
        df['PlacementPoints'][i] = 10
    if df['ThirdPlace'][i] == 'Fall' or df['ThirdPlace'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2
        df['PlacementPoints'][i] = 10
        
for i in range(0,32):
    if df['FifthPlace'][i] == 'Dec' or df['FifthPlace'][i] == 'SV':
        df['PlacementPoints'][i] = 7
    if df['FifthPlace'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
        df['PlacementPoints'][i] = 7
    if df['FifthPlace'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
        df['PlacementPoints'][i] = 7
    if df['FifthPlace'][i] == 'Fall' or df['FifthPlace'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2
        df['PlacementPoints'][i] = 7
        
        
for i in range(0,32):
    if df['SeventhPlace'][i] == 'Dec' or df['SeventhPlace'][i] == 'SV':
        df['PlacementPoints'][i] = 4
    if df['SeventhPlace'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
        df['PlacementPoints'][i] = 4
    if df['SeventhPlace'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
        df['PlacementPoints'][i] = 4
    if df['SeventhPlace'][i] == 'Fall' or df['SeventhPlace'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2
        df['PlacementPoints'][i] = 4


# In[15]:


for i in range(0,33):
    if pd.notnull(df.at[i,'ConsRound5']) and pd.isnull(df.at[i,'ConsRound6']) and pd.isnull(df.at[i,'SeventhPlace']):
        df['PlacementPoints'][i] = 3
for i in range(0,33):
    if pd.notnull(df.at[i,'ConsRound6']) and pd.isnull(df.at[i,'ConsRound7']) and pd.isnull(df.at[i,'FifthPlace']):
        df['PlacementPoints'][i] = 6
for i in range(0,33):
    if pd.notnull(df.at[i,'ConsRound7']) and pd.isnull(df.at[i,'ThirdPlace']):
        df['PlacementPoints'][i] = 9


# In[16]:


columns = df.columns[1:10]


# In[18]:


for col in columns:
    for i in range(0,33):
        if pd.notnull(df.at[i,col]):
            df['AdvPoints'][i] = df['AdvPoints'][i] + 0.5


# In[19]:


df


# In[20]:


df1 = pd.read_csv('champ_285_scored_df.csv')


# In[21]:


df1


# In[22]:


df1.drop("Unnamed: 0", axis=1,inplace=True)


# In[23]:


df1.rename(columns={"Unnamed: 0.1": "Unnamed: 0"},inplace=True)


# In[24]:


df1


# In[25]:


df2 = pd.merge(df, df1, on='Unnamed: 0')


# In[26]:


df2['BonusPoints'] = df2['BonusPoints_x'] + df2['BonusPoints_y']


# In[27]:


df2['AdvPoints'] = df2['AdvPoints_x'] + df2['AdvPoints_y']


# In[28]:


df2['PlacementPoints'] = df2['PlacementPoints_x'] + df2['PlacementPoints_y']


# In[29]:


cols = ['Unnamed: 0', 'ConsRound2', 'ConsRound3', 'ConsRound4', 'ConsRound5',
       'ConsRound6', 'ConsRound7', 'ThirdPlace', 'FifthPlace', 'SeventhPlace','Round1', 'Round2', 'Round3', 'Round4', 'Finals','BonusPoints',
       'AdvPoints', 'PlacementPoints']


# In[30]:


df3 = df2[cols]


# In[31]:


df3


# In[32]:


df3.to_csv(r'C:\Users\fq1228hj\Documents\NCAA Wrestling\all_285_scored_df.csv')


# In[ ]:




