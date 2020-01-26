#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import pandas as pd
import numpy as np

with open('NCAAwrestling1.txt') as myFile:
    text = myFile.read()
result = text.split('2019 NCAA Division I Wrestling Championships')

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

words_list = re.split("[- )(]+", doc_285)

list1 = []
for item in words_list:
    if '0' not in item and '1' not in item and '2' not in item and '3' not in item and '4' not in item and '5' not in item and '6' not in item and '7' not in item and '8' not in item and '9' not in item and 'day' not in item:
        list1.append(item)

def caps_func(string):
    if string.isupper() and string != 'TF' and string != 'MD' and string!='TB' and string!='DQ' and string!='SV' and string!= 'DJ':
        return False
    else:
        return True

list2 = list(filter(caps_func,list1))

def remove_stop_words(string):
    if string == '' or string == 'Championships' or string == 'Morning' or string == 'Night' or string == 'Division' or string == 'Wrestling' or string == 'Place' or string == 'Third' or string == 'Fifth' or string == 'Seventh' or string == 'Loser' or string == 'of':
        return False
    else:
        return True

cleaned_list = list(filter(remove_stop_words,list2))

all_Round1_tags = cleaned_list[0:64]

ChampRound1 = []
for i in range(63):
    if i % 2 == 0:
        ChampRound1.append(''.join(all_Round1_tags[i : i+2]))


# In[2]:


ChampRound1


# In[4]:


third_place_match = cleaned_list[126:128]
fifth_place_match = cleaned_list[128:130]
seventh_place_match = cleaned_list[130:132]


# In[5]:


for i in range(0,len(third_place_match)):
    for j in range(0,len(ChampRound1)):
        if third_place_match[i] in ChampRound1[j]:
            third_place_match[i] = ChampRound1[j]
for i in range(0,len(third_place_match)):
    for j in range(0,len(ChampRound1)):
        if fifth_place_match[i] in ChampRound1[j]:
            fifth_place_match[i] = ChampRound1[j]
for i in range(0,len(seventh_place_match)):
    for j in range(0,len(ChampRound1)):
        if seventh_place_match[i] in ChampRound1[j]:
            seventh_place_match[i] = ChampRound1[j]


# In[6]:


third_placekeys = []
third_placevals = []
for i in range(len(third_place_match)):
    if i % 2 == 0:
        third_placekeys.append(third_place_match[i])
    else:
        third_placevals.append(third_place_match[i])


# In[7]:


for i in range(len(ChampRound1)):
    if ChampRound1[i] not in third_placekeys:
        third_placekeys.append(ChampRound1[i])
        third_placevals.append('')


# In[8]:


third_place = {third_placekeys[i]: third_placevals[i] for i in range(len(third_placekeys))}


# In[9]:


third_place


# In[10]:


fifth_placekeys = []
fifth_placevals = []
for i in range(len(fifth_place_match)):
    if i % 2 == 0:
        fifth_placekeys.append(fifth_place_match[i])
    else:
        fifth_placevals.append(fifth_place_match[i])


# In[11]:


for i in range(len(ChampRound1)):
    if ChampRound1[i] not in fifth_placekeys:
        fifth_placekeys.append(ChampRound1[i])
        fifth_placevals.append('')


# In[12]:


fifth_place = {fifth_placekeys[i]: fifth_placevals[i] for i in range(len(fifth_placekeys))}


# In[13]:


fifth_place


# In[14]:


seventh_placekeys = []
seventh_placevals = []
for i in range(len(seventh_place_match)):
    if i % 2 == 0:
        seventh_placekeys.append(seventh_place_match[i])
    else:
        seventh_placevals.append(seventh_place_match[i])


# In[15]:


for i in range(len(ChampRound1)):
    if ChampRound1[i] not in seventh_placekeys:
        seventh_placekeys.append(ChampRound1[i])
        seventh_placevals.append('')


# In[16]:


seventh_place = {seventh_placekeys[i]: seventh_placevals[i] for i in range(len(seventh_placekeys))}


# In[17]:


seventh_place


# In[18]:


all_ConsRound1_tags = cleaned_list[132:164]


# In[19]:


all_ConsRound1_tags


# In[20]:


ConsRound1 = []
for i in range(len(all_ConsRound1_tags)):
    if i % 2 == 0:
        ConsRound1.append(''.join(all_ConsRound1_tags[i : i+2]))


# In[21]:


ConsRound1


# In[22]:


all_ConsRound2_tags = cleaned_list[164:188]


# In[24]:


all_ConsRound2_tags_cleaned = []
for i in range(len(all_ConsRound2_tags)-1):
    if i % 3 == 0:
        all_ConsRound2_tags_cleaned.append(all_ConsRound2_tags[i])
    if i % 3 == 1:
        all_ConsRound2_tags_cleaned.append(all_ConsRound2_tags[i])


# In[25]:


for i in range(0,len(all_ConsRound2_tags_cleaned)):
    for j in range(0,len(ChampRound1)):
        if all_ConsRound2_tags_cleaned[i] in ChampRound1[j]:
            all_ConsRound2_tags_cleaned[i] = ChampRound1[j]


# In[26]:


ConsRound2keys = []
ConsRound2vals = []
for i in range(len(all_ConsRound2_tags_cleaned)):
    if i % 2 == 0:
        ConsRound2keys.append(all_ConsRound2_tags_cleaned[i])
    else:
        ConsRound2vals.append(all_ConsRound2_tags_cleaned[i])


# In[27]:


for i in range(len(ChampRound1)):
    if ChampRound1[i] not in ConsRound2keys:
        ConsRound2keys.append(ChampRound1[i])
        ConsRound2vals.append('')


# In[28]:


ConsRound2 = {ConsRound2keys[i]: ConsRound2vals[i] for i in range(len(ConsRound2keys))}


# In[29]:


ConsRound2


# In[30]:


all_ConsRound3_tags = cleaned_list[188:204]


# In[31]:


all_ConsRound3_tags


# In[32]:


for i in range(0,len(all_ConsRound3_tags)):
    for j in range(0,len(ChampRound1)):
        if all_ConsRound3_tags[i] in ChampRound1[j]:
            all_ConsRound3_tags[i] = ChampRound1[j]


# In[33]:


ConsRound3keys = []
ConsRound3vals = []
for i in range(len(all_ConsRound3_tags)):
    if i % 2 == 0:
        ConsRound3keys.append(all_ConsRound3_tags[i])
    else:
        ConsRound3vals.append(all_ConsRound3_tags[i])


# In[34]:


for i in range(len(ChampRound1)):
    if ChampRound1[i] not in ConsRound3keys:
        ConsRound3keys.append(ChampRound1[i])
        ConsRound3vals.append('')


# In[35]:


ConsRound3 = {ConsRound3keys[i]: ConsRound3vals[i] for i in range(len(ConsRound3keys))}


# In[36]:


ConsRound3


# In[37]:


all_ConsRound4_tags = cleaned_list[204:216]


# In[38]:


all_ConsRound4_tags


# In[39]:


for i in range(0,len(all_ConsRound4_tags)):
    for j in range(0,len(ChampRound1)):
        if all_ConsRound4_tags[i] in ChampRound1[j]:
            all_ConsRound4_tags[i] = ChampRound1[j]


# In[40]:


all_ConsRound4_tags_cleaned = []
for i in range(len(all_ConsRound4_tags)-1):
    if i % 3 != 2:
        all_ConsRound4_tags_cleaned.append(all_ConsRound4_tags[i])


# In[41]:


ConsRound4keys = []
ConsRound4vals = []
for i in range(len(all_ConsRound4_tags_cleaned)):
    if i % 2 == 0:
        ConsRound4keys.append(all_ConsRound4_tags_cleaned[i])
    else:
        ConsRound4vals.append(all_ConsRound4_tags_cleaned[i])


# In[42]:


for i in range(len(ChampRound1)):
    if ChampRound1[i] not in ConsRound4keys:
        ConsRound4keys.append(ChampRound1[i])
        ConsRound4vals.append('')


# In[43]:


ConsRound4 = {ConsRound4keys[i]: ConsRound4vals[i] for i in range(len(ConsRound4keys))}


# In[44]:


ConsRound4


# In[45]:


all_ConsRound5_tags = cleaned_list[216:224]


# In[46]:


all_ConsRound5_tags


# In[47]:


for i in range(0,len(all_ConsRound5_tags)):
    for j in range(0,len(ChampRound1)):
        if all_ConsRound5_tags[i] in ChampRound1[j]:
            all_ConsRound5_tags[i] = ChampRound1[j]


# In[48]:


ConsRound5keys = []
ConsRound5vals = []
for i in range(len(all_ConsRound5_tags)):
    if i % 2 == 0:
        ConsRound5keys.append(all_ConsRound5_tags[i])
    else:
        ConsRound5vals.append(all_ConsRound5_tags[i])


# In[49]:


for i in range(len(ChampRound1)):
    if ChampRound1[i] not in ConsRound5keys:
        ConsRound5keys.append(ChampRound1[i])
        ConsRound5vals.append('')


# In[50]:


ConsRound5 = {ConsRound5keys[i]: ConsRound5vals[i] for i in range(len(ConsRound5keys))}


# In[51]:


all_ConsRound6_tags = cleaned_list[224:230]


# In[52]:


for i in range(0,len(all_ConsRound6_tags)):
    for j in range(0,len(ChampRound1)):
        if all_ConsRound6_tags[i] in ChampRound1[j]:
            all_ConsRound6_tags[i] = ChampRound1[j]


# In[53]:


all_ConsRound6_tags_cleaned = []
for i in range(len(all_ConsRound6_tags)-1):
    if i % 3 != 2:
        all_ConsRound6_tags_cleaned.append(all_ConsRound6_tags[i])


# In[54]:


ConsRound6keys = []
ConsRound6vals = []
for i in range(len(all_ConsRound6_tags_cleaned)):
    if i % 2 == 0:
        ConsRound6keys.append(all_ConsRound6_tags_cleaned[i])
    else:
        ConsRound6vals.append(all_ConsRound6_tags_cleaned[i])


# In[55]:


for i in range(len(ChampRound1)):
    if ChampRound1[i] not in ConsRound6keys:
        ConsRound6keys.append(ChampRound1[i])
        ConsRound6vals.append('')


# In[56]:


ConsRound6 = {ConsRound6keys[i]: ConsRound6vals[i] for i in range(len(ConsRound6keys))}


# In[57]:


all_ConsRound7_tags = cleaned_list[230:234]


# In[58]:


all_ConsRound7_tags


# In[59]:


for i in range(0,len(all_ConsRound7_tags)):
    for j in range(0,len(ChampRound1)):
        if all_ConsRound7_tags[i] in ChampRound1[j]:
            all_ConsRound7_tags[i] = ChampRound1[j]


# In[60]:


ConsRound7keys = []
ConsRound7vals = []
for i in range(len(all_ConsRound7_tags)):
    if i % 2 == 0:
        ConsRound7keys.append(all_ConsRound7_tags[i])
    else:
        ConsRound7vals.append(all_ConsRound7_tags[i])


# In[61]:


for i in range(len(ChampRound1)):
    if ChampRound1[i] not in ConsRound7keys:
        ConsRound7keys.append(ChampRound1[i])
        ConsRound7vals.append('')


# In[62]:


ConsRound7 = {ConsRound7keys[i]: ConsRound7vals[i] for i in range(len(ConsRound7keys))}


# In[76]:


columns = ['ConsRound1','ConsRound2','ConsRound3','ConsRound4','ConsRound5','ConsRound6','ThirdPlace','FifthPlace','SeventhPlace']


# In[77]:


cons_bracket_dict_for_pd = {}


# In[78]:


for i in range(0,len(ChampRound1)):
    cons_bracket_dict_for_pd.update({ChampRound1[i]:[]})


# In[79]:


ConsRound1


# In[80]:


ConsRound2


# In[81]:


ConsRound3


# In[82]:


ConsRound4


# In[ ]:





# In[83]:


for key in ConsRound2.keys():
    cons_bracket_dict_for_pd[key].append(ConsRound2[key])
for key in ConsRound3.keys():
    cons_bracket_dict_for_pd[key].append(ConsRound3[key])
for key in ConsRound4.keys():
    cons_bracket_dict_for_pd[key].append(ConsRound4[key])
for key in ConsRound5.keys():
    cons_bracket_dict_for_pd[key].append(ConsRound5[key])
for key in ConsRound6.keys():
    cons_bracket_dict_for_pd[key].append(ConsRound6[key])
for key in ConsRound7.keys():
    cons_bracket_dict_for_pd[key].append(ConsRound7[key])
for key in third_place.keys():
    cons_bracket_dict_for_pd[key].append(third_place[key])
for key in fifth_place.keys():
    cons_bracket_dict_for_pd[key].append(fifth_place[key])
for key in seventh_place.keys():
    cons_bracket_dict_for_pd[key].append(seventh_place[key])


# In[84]:


cons_bracket_df = pd.DataFrame(cons_bracket_dict_for_pd)


# In[85]:


cons_bracket_df = cons_bracket_df.transpose()


# In[86]:


cons_bracket_df.columns=columns


# In[87]:


cons_bracket_df


# In[88]:


cons_bracket_df.to_csv(r'C:\Users\fq1228hj\Documents\NCAA Wrestling\cons_285_df.csv')


# In[ ]:




