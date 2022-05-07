#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd


# In[41]:


pwd


# In[46]:


bison=pd.read_csv('C:/Users/Camille Kenworthy/OneDrive/Desktop/BisonTracking.csv')


# In[47]:


bison


# # Look at the first seven rows of your data

# In[48]:


bison.head(7)


# ## OH My the last 10

# In[49]:


bison.tail(10)


# ### Determine the number of rows and columns your dataset has

# In[52]:


len(bison)


# In[54]:


len(bison.columns)


# ### How many bison are of the species antiquus?

# In[60]:


bison.mean()


# In[61]:


bison.count()


# In[63]:


bison.Species.value_counts()


# #### What is the median length of the bison?

# In[64]:


bison.median()


# In[ ]:




