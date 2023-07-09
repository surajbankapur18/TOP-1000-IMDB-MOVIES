#!/usr/bin/env python
# coding: utf-8

# # IMDB TOP 1000 MOVIES 

# # Importing libraries 

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

import warnings
warnings.filterwarnings(action = "ignore")


# In[2]:


pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)


# In[3]:


df=pd.read_csv(r"C:\UPGRAD CSV\imdb_top_1000.csv")


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.shape


# In[7]:


df.dtypes


# In[8]:


df.info()


# In[9]:


df.describe()


# In[10]:


df.isnull().sum()


# In[11]:


100*df.isnull().mean()


# # Handling missing values 

# In[12]:


df[df['Certificate'].isnull()]


# In[13]:


df['Certificate'].unique()


# In[14]:


df['Gross'].isnull().sum()


# In[15]:


df['Gross'].info()


# In[16]:


df['Gross']=df['Gross'].fillna(0)


# In[17]:


df['Gross']


# In[18]:


x = df['Gross'].loc[df['Gross'] == 0]
print(x)


# In[19]:


mean =df['Meta_score'].mean()
print(mean)


# In[20]:


df['Meta_score'] = df['Meta_score'].fillna(mean)


# In[21]:


df['Gross'] = df['Gross'].apply(lambda x: str(x).replace(',','') if ',' in str(x) else str(x))
df['Gross'] = df['Gross'].apply(lambda x: float(x))
mean = df['Gross'].mean()
print(mean)


# In[22]:


df['Gross'] = df['Gross'].fillna(mean)


# In[23]:


df['Gross']


# In[24]:


mn = df['Gross'].mean()
print(mn)


# # Insight

# In[25]:


# the missing values in meta score and gross has been replaced 


# In[26]:


df['Certificate'].unique()


# In[27]:


df['Certificate'].mode()


# In[28]:


U = df['Certificate'].value_counts()['U']
print(U)


# In[29]:


df['Certificate'] = df['Certificate'].fillna(U)


# In[30]:


df.isnull().sum()


# In[31]:


#Drop the unnecesary columns 


# In[32]:


df = df.drop(['Poster_Link','Series_Title','Overview'],axis=1)


# In[33]:


df.head(2)


# In[34]:


for i in range (len(df)):
    df.loc[i, 'Runtime'] =df.loc[i, 'Runtime'].replace(' min','')


# In[35]:


df['Runtime']


# In[36]:


df['Released_Year'].unique()


# In[37]:


df['Released_Year'].value_counts()


# In[38]:


y = df['Released_Year'].loc[df['Released_Year'] == 'PG']
print(y)


# In[39]:


df = df.drop(labels=966 , axis=0)


# In[40]:


df['Released_Year'] =df['Released_Year'].astype(int)


# In[ ]:





# In[41]:


plt.figure(figsize=(15,8))
sns.countplot(df['Certificate'])

plt.xticks(rotation= 40)
plt.show()


# # Insight

# In[42]:


# the most movies which are of 'U' certificate in Top 1000 imdb movies


# In[ ]:





# In[43]:


plt.figure(figsize=(16,7))
sns.countplot(df['Released_Year'])
plt.xticks(rotation= 90)
plt.show()


# # Insight

# In[44]:


#the top imdb rating movies and tvshows are rated after the year 1960


# In[ ]:





# In[45]:


plt.figure(figsize=(16,8))
sns.countplot(df['IMDB_Rating'])
plt.xticks(rotation=0)
plt.show()


# # Insight

# In[46]:


# majorly ratings are greater than 7.5 and less than 8.5 9.3 is the highest rating


# In[ ]:





# In[49]:


top_rates = df.groupby('Genre').mean().sort_values('IMDB_Rating',ascending=False).head(10)
top_rates = top_rates[['IMDB_Rating']].round(2)
top_rates.reset_index(inplace = True)
top_rates


# # Insight

# In[ ]:


## The "Animation,Drama,War"Genre has the Highest IMDB_rating of 8.50


# In[ ]:





# In[51]:


plt.figure(figsize=(15,8))
plt.bar(top_rates['Genre'],top_rates['IMDB_Rating'])
plt.xticks(rotation=90)
for k,v in top_rates['IMDB_Rating'].items():
    plt.text(k,v-5,str(v),rotation=90)


# In[52]:


top_rates=df.groupby('Genre').mean().sort_values('Meta_score',ascending=False).head(10)
top_rates = top_rates[['Meta_score']].round(2)
top_rates.reset_index(inplace=True)
top_rates


# In[53]:


plt.figure(figsize=(15,8))
plt.bar(top_rates['Genre'],top_rates['Meta_score'])
plt.xticks(rotation='vertical')
for k,v in top_rates['Meta_score'].items():
    plt.text(k,v-11,str(v),rotation=90)


# In[54]:


top_earn = df.groupby('Genre').sum().sort_values('Gross',ascending=False).head(10)
top_earn=top_earn[['Gross']]
top_earn.reset_index(inplace=True)

plt.figure(figsize=(15,8))
plt.bar(top_earn['Genre'],top_earn['Gross'])
plt.xticks(rotation='vertical')
for k,v in top_earn['Gross'].items():
    plt.text(k,v-1450000000,str(v),rotation=90)


# # Insights

# In[55]:


## Movies whose genre 'Action,Adventure ,Sci-Fi' achieve the most earnings


# In[59]:


plt.figure(figsize=(15,8))
sns.barplot(x='Certificate',y='Gross',data=df, ci =False)
plt.xticks(rotation='vertical')
plt.show();


# # Insight

# In[60]:


##Movies whose certificates 'UA' acheived more earnings


# In[61]:


top_director= df.groupby('Director').mean().sort_values('Gross').head(10)
top_director=top_director[['IMDB_Rating']]
top_director.reset_index(inplace=True)

plt.figure(figsize=(15,8))
sns.barplot(x='Director',y='IMDB_Rating',data=top_director)
plt.xticks(rotation='vertical')

for k,v in top_director['IMDB_Rating'].items():
    plt.text(k,v-2,str(v),rotation=90)


# In[64]:


top_director=df.groupby('Director').mean().sort_values('Gross').head(10)
top_director=top_director[['IMDB_Rating']]
top_director.reset_index(inplace=True)

plt.figure(figsize=(15,8))
sns.barplot(x='Director',y='IMDB_Rating',data=top_director)
plt.xticks(rotation='vertical')

for k,v in top_director['IMDB_Rating'].items():
    plt.text(k,v-2,str(v),rotation=90)


# In[65]:


#The directors 'Tigmanshu Dhulia','Vikramaditya Motwane achieved the most high imdb rates


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




