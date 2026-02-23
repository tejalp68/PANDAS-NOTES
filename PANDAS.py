#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


df = pd.read_csv("zomato_data.csv")
df.head(50)


# In[4]:


df.describe()


# In[5]:


df.info()


# In[6]:


print(df["name"].count())


# In[7]:


df[df['votes'] > 500]


# In[8]:


df.dtypes


# In[9]:


df.shape


# In[10]:


df.columns


# In[11]:


df["name"].replace("Jalsa","Khalsa")


# In[12]:


df


# In[13]:


df.index = df.index +1


# In[14]:


df


# In[15]:


df[df.dtypes[df.dtypes == "int64"].index]


# In[16]:


df.dtypes[df.dtypes == "int64"]


# In[17]:


df.dtypes[df.dtypes == "object"]


# In[18]:


df[df.dtypes[df.dtypes == "object"].index]


# In[19]:


df.iloc[0]          # index based slicing


# In[20]:


df["NEW_COL"] = 20


# In[21]:


df


# In[22]:


df["book"] ="DATA SCIENCE"


# In[23]:


df


# In[65]:


df["name"].duplicated().sum()
# dp = df[df["name"].duplicated()].index
# print(dp)


# In[71]:


duplicates = df[df.duplicated(subset='name', keep=False)]
print(duplicates[['name']])


# In[73]:


df['votes'].plot(kind='hist')
df.plot(kind='scatter', x='votes', y='approx_cost(for two people)')


# In[ ]:





# In[ ]:




