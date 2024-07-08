#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import streamlit as st
import os
from tqdm import tqdm
from matplotlib import pyplot 


# In[3]:


csvfile_path = os.path.join('..','Hayu-Gen-Finder','elections.csv')
df = pd.read_csv(csvfile_path, dtype= {'bnakavaer':str})


# In[7]:


unique_hayeranun = set(df["haeranun"])
df["gender"] = df['anun'].apply(lambda x: 'male' if x+'ի' in unique_hayeranun else 'female')
print(df.head(10))



# In[16]:


percent_male = df['gender'].value_counts().get('male',0) / len(df) * 100
percent_female = 100 - percent_male
print("Male::",percent_male)
print("Female::",percent_female)
st.write("hey")

