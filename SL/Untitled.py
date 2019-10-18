#!/usr/bin/env python
# coding: utf-8

# In[52]:


import numpy as np
import pandas as pd


# In[53]:


df=pd.read_csv("titanictrain.csv")


# In[54]:



df


# In[55]:


df ['Embarked'] = df ['Embarked'].fillna("S")
df ['Survived'] = df ['Survived'].map( {
    0 : 'Died',
    1 : 'Survived'
})
df ['Pclass'] = df ['Pclass'].map( {
    1 : 'Economy',
    2 : 'First',
    3 : 'Business'
})
df ['Embarked'] = df ['Embarked'].map( {
    'S' : 'South Hampton',
    'C' : 'Church Gate',
    'Q' : 'Queens'
})
df ['Cabin'] =df ['Cabin'].fillna("XXX")


# In[56]:


df


# In[57]:


import seaborn as sb
import matplotlib.pyplot as plt


# In[ ]:


print("Visualization : Survival Rate based upon Passenger Sitting Class")


# In[ ]:





# In[ ]:




