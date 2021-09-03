#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv
import numpy as np
import random 
import math

state = input("Enter State : ")
df = pd.read_csv("/Users/shivanshamattya/Desktop/pincode/state1/" + state +".csv",)


# In[2]:


df.dropna(axis=0, how='any',inplace=True)


# In[3]:


district = df['DISTRICT'].to_numpy()


# In[4]:


district = np.array(district)


# In[5]:


pincode = df['PINCODE'].to_numpy()
pincode = np.array(pincode)


# In[6]:


ds = input("Enter Disctrict : ")


# In[7]:


for i in range(len(district)):
    if district[i].lower()==ds.lower():
        print(pincode[i])


# In[ ]:





# In[ ]:




