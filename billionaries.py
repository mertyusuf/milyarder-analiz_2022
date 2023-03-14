#!/usr/bin/env python
# coding: utf-8

# In[16]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set_theme()
sns.set(rc={"figure.dpi":300})
import warnings
warnings.filterwarnings("ignore")


# In[18]:


df=pd.read_csv("forbes_billionaires_2022.csv")


# In[19]:


df.columns


# In[20]:


df=df.loc[:,["rank","personName","age","finalWorth","category","source","country","organization","selfMade","gender","title"]]


# In[47]:


df.head()


# In[21]:


df["gender"].value_counts()


# In[25]:


df[df["country"]=="Turkey"].gender.value_counts()


# In[23]:


df.selfMade.value_counts()


# In[27]:


df_gender=df.groupby(["gender"])


# In[76]:


df_gender["age"].mean()


# In[28]:


df_gender.size().plot(kind="bar")
plt.title("DÜNYADAKİ SERVETİN CİNSİYET DAĞILIMI")
plt.xlabel("Cinsiyet")


# In[169]:


sns.barplot(y=df["personName"][:10],x=df["finalWortht"[:10]])
plt.title("EN ZENGİN 10 İŞ İNSANI")
plt.xlabel("SERVET")
plt.ylabel("İSİM")


# In[29]:


df_ulke=df.groupby("country")


# In[30]:


df_ulkes_sayi=pd.DataFrame(df_ulke.size().sort_values(ascending=False),columns=["sayi"])


# In[31]:


df_ulkes_sayi.head(10)


# In[167]:


sns.barplot(x=df_ulkes_sayi["sayi"][:20],y=df_ulkes_sayi.index[:20])
plt.title("MİLYARDERLERİN YAŞADIKLARI ÜLKELER")
plt.ylabel("ÜLKE")


# In[38]:


df_turkey=df[df["country"]=="Turkey"]


# In[100]:


df_turkey.head()


# In[161]:


sns.barplot(y=df_turkey["personName"][:10],x=df_turkey["finalWorth"][:10])
plt.title("EN ZENGİN 10 TÜRK İŞ İNSANI")
plt.xlabel("SERVET")
plt.ylabel("İSİM")


# In[106]:


df["category"].unique()


# In[32]:


df["category"]=df["category"].apply(lambda x:x.replace(" ","")).\
apply(lambda x:x.replace("&","_"))


# In[33]:


df_kategori=df.groupby("category").size()


# In[34]:


df_kategori.head()


# In[35]:


df_kategori=df_kategori.to_frame()


# In[36]:


df_kategori.head()


# In[113]:


df_kategori=df_kategori.rename(columns={0:"sayi"}).sort_values(by="sayi",ascending=False)


# In[114]:


df_kategori.head()


# In[174]:


sns.barplot(x=df_kategori["sayi"][:10],y=df_kategori.index[:10])
plt.title("MİLYARDERLERİN İLGİLENDİĞİ SEKTÖRLER")


# In[176]:


sns.histplot(df["age"])
plt.title("MİLYARDERLERİN YAŞ DAĞILIMI")


# In[148]:


df.loc[(df["country"]=="Turkey") & (df["category"])].head(10)


# In[39]:


sns.histplot(y=df_turkey["personName"][:10],x=df_turkey["source"][:10])
plt.title("Türk iş insanlarinin uğrastığı alanlar")
plt.xlabel("UĞRAŞILAN ALAN")
plt.ylabel("İSİM")


# In[ ]:




