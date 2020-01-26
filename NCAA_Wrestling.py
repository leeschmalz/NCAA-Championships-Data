#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import pandas as pd
import numpy as np


# In[2]:


with open('NCAAwrestling1.txt') as myFile:
    text = myFile.read()
result = text.split('2019 NCAA Division I Wrestling Championships')


# In[3]:


doc_125 = result[1]
doc_133 = result[2]
doc_141 = result[3]
doc_149 = result[4]
doc_157 = result[5]
doc_165 = result[6]
doc_174 = result[7]
doc_184 = result[8]
doc_197 = result[9]
doc_285 = result[10]


# In[4]:


words_list = re.split("[- )(]+", doc_125)


# In[5]:


list1 = []
for item in words_list:
    if '0' not in item and '1' not in item and '2' not in item and '3' not in item and '4' not in item and '5' not in item and '6' not in item and '7' not in item and '8' not in item and '9' not in item and 'day' not in item:
        list1.append(item)


# In[6]:


def caps_func(string):
    if string.isupper() and string != 'TF' and string != 'MD' and string!='TB' and string!='DQ' and string!='SV' and string!= 'DJ':
        return False
    else:
        return True

list2 = list(filter(caps_func,list1))


# In[7]:


def remove_stop_words(string):
    if string == '' or string == 'Championships' or string == 'Morning' or string == 'Night' or string == 'Division' or string == 'Wrestling' or string == 'Place' or string == 'Third' or string == 'Fifth' or string == 'Seventh' or string == 'Loser' or string == 'of':
        return False
    else:
        return True

cleaned_list = list(filter(remove_stop_words,list2))


# In[10]:


cleaned_list


# In[11]:


all_Round1_tags = cleaned_list[0:64]


# In[12]:


ChampRound1 = []
for i in range(63):
    if i % 2 == 0:
        ChampRound1.append(''.join(all_Round1_tags[i : i+2]))


# In[15]:


all_Round2_tags = cleaned_list[64:96]


# In[16]:


range(0,len(all_Round2_tags)-1)


# In[17]:


for i in range(0,len(all_Round2_tags)):
    for j in range(0,len(ChampRound1)):
        if all_Round2_tags[i] in ChampRound1[j]:
            all_Round2_tags[i] = ChampRound1[j]


# In[18]:


ChampRound2keys = []
ChampRound2vals = []
for i in range(len(all_Round2_tags)):
    if i % 2 == 0:
        ChampRound2keys.append(all_Round2_tags[i])
    else:
        ChampRound2vals.append(all_Round2_tags[i])


# In[19]:


ChampRound2 = {ChampRound2keys[i]: ChampRound2vals[i] for i in range(len(ChampRound2keys))}


# In[20]:


ChampRound2


# In[21]:


all_Round3_tags = cleaned_list[96:112]


# In[22]:


for i in range(0,len(all_Round3_tags)):
    for j in range(0,len(ChampRound1)):
        if all_Round3_tags[i] in ChampRound1[j]:
            all_Round3_tags[i] = ChampRound1[j]


# In[23]:


ChampRound3keys = []
ChampRound3vals = []
for i in range(len(all_Round3_tags)):
    if i % 2 == 0:
        ChampRound3keys.append(all_Round3_tags[i])
    else:
        ChampRound3vals.append(all_Round3_tags[i])


# In[24]:


ChampRound3 = {ChampRound3keys[i]: ChampRound3vals[i] for i in range(len(ChampRound3keys))}


# In[25]:


ChampRound3


# In[26]:


all_Round4_tags = cleaned_list[112:120]


# In[27]:


for i in range(0,len(all_Round4_tags)):
    for j in range(0,len(ChampRound1)):
        if all_Round4_tags[i] in ChampRound1[j]:
            all_Round4_tags[i] = ChampRound1[j]


# In[28]:


ChampRound4keys = []
ChampRound4vals = []
for i in range(len(all_Round4_tags)):
    if i % 2 == 0:
        ChampRound4keys.append(all_Round4_tags[i])
    else:
        ChampRound4vals.append(all_Round4_tags[i])


# In[29]:


ChampRound4 = {ChampRound4keys[i]: ChampRound4vals[i] for i in range(len(ChampRound4keys))}


# In[30]:


ChampRound4


# In[31]:


all_ChampFinals_tags = cleaned_list[120:124]


# In[32]:


for i in range(0,len(all_ChampFinals_tags)):
    for j in range(0,len(ChampRound1)):
        if all_ChampFinals_tags[i] in ChampRound1[j]:
            all_ChampFinals_tags[i] = ChampRound1[j]


# In[33]:


ChampFinalskeys = []
ChampFinalsvals = []
for i in range(len(all_ChampFinals_tags)):
    if i % 2 == 0:
        ChampFinalskeys.append(all_ChampFinals_tags[i])
    else:
        ChampFinalsvals.append(all_ChampFinals_tags[i])


# In[34]:


ChampFinals = {ChampFinalskeys[i]: ChampFinalsvals[i] for i in range(len(ChampFinalskeys))}


# In[35]:


ChampFinals


# In[36]:


Champion_list = cleaned_list[124:126]


# In[37]:


for i in range(0,len(ChampRound1)):
    if Champion_list[0] in ChampRound1[i]:
        Champion_list[0] = ChampRound1[i]


# In[38]:


Champion = {Champion_list[0]:Champion_list[1]}


# In[45]:


placing_rounds = cleaned_list[126:132]
placing_rounds


# In[53]:


columns = ['Round1','Round2','Round3','Round4','Finals']


# In[54]:


champ_bracket_dict_for_pd = {}


# In[55]:


for i in range(0,len(ChampRound1)):
    champ_bracket_dict_for_pd.update({ChampRound1[i]:[]})


# In[56]:


for key in ChampRound2.keys():
    champ_bracket_dict_for_pd[key].append(ChampRound2[key])


# In[57]:


for key in ChampRound3.keys():
    champ_bracket_dict_for_pd[key].append(ChampRound3[key])


# In[58]:


for key in ChampRound4.keys():
    champ_bracket_dict_for_pd[key].append(ChampRound4[key])


# In[59]:


for key in ChampFinals.keys():
    champ_bracket_dict_for_pd[key].append(ChampFinals[key])


# In[60]:


for key in Champion.keys():
    champ_bracket_dict_for_pd[key].append(Champion[key])


# In[63]:


for key in champ_bracket_dict_for_pd.keys():
    if len(champ_bracket_dict_for_pd[key])<5:
        champ_bracket_dict_for_pd[key].append('')
    if len(champ_bracket_dict_for_pd[key])<5:
        champ_bracket_dict_for_pd[key].append('')
    if len(champ_bracket_dict_for_pd[key])<5:
        champ_bracket_dict_for_pd[key].append('')
    if len(champ_bracket_dict_for_pd[key])<5:
        champ_bracket_dict_for_pd[key].append('')
    if len(champ_bracket_dict_for_pd[key])<5:
        champ_bracket_dict_for_pd[key].append('')


# In[64]:


champ_bracket_dict_for_pd


# In[918]:


champ_bracket_df = pd.DataFrame(champ_bracket_dict_for_pd)


# In[919]:


champ_bracket_df = champ_bracket_df.transpose()


# In[920]:


champ_bracket_df.columns=columns


# In[921]:


champ_285_df = champ_bracket_df


# In[937]:


champ_285_df


# In[936]:


champ_285_df.to_csv(r'C:\Users\fq1228hj\Documents\NCAA Wrestling\champ_285_df.csv')


# In[ ]:




