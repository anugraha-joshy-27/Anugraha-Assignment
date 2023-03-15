#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Read the dataset to python environment

# In[2]:


data=pd.read_excel('iris.xls')


# # Display the columns in the dataset

# In[3]:


data.head()


# In[4]:


data


# # Calculate the mean of each column of the dataset

# In[5]:


print(data['SL'].mean())
print(data['SW'].mean())
print(data['PL'].mean())
print(data['PW'].mean())


# # Check for the null values present in the dataset

# In[6]:


data.dtypes


# In[7]:


data.isna()


# In[8]:


data.isna().sum()


# # Perform meaningful visualizations using the dataset. Bring at least 3 visualizations

# In[9]:


sns.pairplot(data)
plt.show()


# In[10]:


#bold too
plt.hist(data['Classification'], color='purple')
plt.title('Classification vs Frequency',fontweight='bold')
plt.xlabel('Classification',fontweight='bold')
plt.ylabel('Frequency',fontweight='bold')
plt.show()


# In[11]:


plt.figure(figsize=(8,6))

plt.subplot(2,1,1)
plt.scatter(data['PW'],data['PL'], color='green', s=22)
plt.title('PW vs PL',fontweight='bold')
plt.xlabel('PW',fontweight='bold')
plt.ylabel('PL',fontweight='bold')
plt.show()

plt.figure(figsize=(8,6))
plt.subplot(2,1,2)
plt.scatter(data['PL'],data['PW'], color='red', s=22)
plt.title('PL vs PW',fontweight='bold')
plt.xlabel('PL',fontweight='bold')
plt.ylabel('PW',fontweight='bold')
plt.show()


# In[12]:


#just replace plt with sns, 8,6 is big size?
plt.figure(figsize=(8,6))
sns.boxplot(data=data)
plt.show()


# In[ ]:




