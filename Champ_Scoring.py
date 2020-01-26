#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('champ_285_df.csv')


# In[3]:


df['BonusPoints'] = np.zeros(32)
df['AdvPoints'] = np.zeros(32)
df['PlacementPoints'] = np.zeros(32)


# In[4]:


for i in range(0,32):
    if df['Round1'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
    if df['Round1'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
    if df['Round1'][i] == 'Fall' or df['Round1'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2
        
for i in range(0,32):
    if df['Round2'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
    if df['Round2'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
    if df['Round2'][i] == 'Fall' or df['Round2'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2

for i in range(0,32):
    if df['Round3'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
    if df['Round3'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
    if df['Round3'][i] == 'Fall' or df['Round3'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2

for i in range(0,32):
    if df['Round4'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
    if df['Round4'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
    if df['Round4'][i] == 'Fall' or df['Round4'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2
        
for i in range(0,32):
    if df['Finals'][i] == 'MD':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1
    if df['Finals'][i] == 'TF':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 1.5
    if df['Finals'][i] == 'Fall' or df['Finals'][i] == 'DQ':
        df['BonusPoints'][i] = df['BonusPoints'][i] + 2


# In[5]:


for i in range(0,32):
    if df['Round1'].notnull()[i] == True:
        df['AdvPoints'][i] = df['AdvPoints'][i] + 1
    if df['Round2'].notnull()[i] == True:
        df['AdvPoints'][i] = df['AdvPoints'][i] + 1
    if df['Round3'].notnull()[i] == True:
        df['AdvPoints'][i] = df['AdvPoints'][i] + 1
    if df['Round4'].notnull()[i] == True:
        df['AdvPoints'][i] = df['AdvPoints'][i] + 1
        df['PlacementPoints'][i] = 12
    if df['Finals'].notnull()[i] == True:
        df['AdvPoints'][i] = df['AdvPoints'][i] + 1
        df['PlacementPoints'][i] = 16


# In[6]:


df


# In[7]:


df.to_csv(r'C:\Users\fq1228hj\Documents\NCAA Wrestling\champ_285_scored_df.csv')


# In[ ]:




