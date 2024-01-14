#!/usr/bin/env python
# coding: utf-8

# ### Reading the data

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


# In[31]:


dataset=pd.read_csv("Desktop\Technical Test\sample_data_100.csv")


# In[32]:


dataset


# ### Understanding our data

# In[33]:


dataset.shape


# In[34]:


dataset.dtypes


# In[35]:


dataset.describe()


# In[36]:


dataset.isnull().sum()
#there are significant missing values. Now, we need to analyse for outliers to check the best method for imputation.


# In[37]:


dataset.duplicated().sum()
#No Duplicates


# In[39]:


dataset.columns


# In[40]:


dataset.rename(columns={'Unnamed: 0':'Serial_No'},inplace=True)


# In[42]:


dataset['year']=pd.to_datetime(dataset['year'])


# In[44]:


dataset.head(2)


# In[45]:


dataset.dtypes


# In[48]:


columns_to_drop=['Serial_No','isin','year']
data=dataset.drop(columns_to_drop,axis=1)
data.head(2)


# In[58]:


columns_to_drop_2=['em_60000', 'em_60100', 'em_60200',
       'em_60300', 'em_60400', 'em_60500', 'em_60600', 'em_60700', 'em_60800',
       'em_60900', 'em_61000', 'em_61100', 'em_61200', 'em_61300', 'em_61400',
       'em_61500', 'em_61600', 'em_61700', 'em_61800']
data_2=dataset.drop(columns_to_drop_2,axis=1)


# In[59]:


data_2.head()


# In[52]:


data.corr().T


# ### Outlier Detection

# In[49]:


Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1

# Define outliers as those outside of Q1 - 1.5 * IQR and Q3 + 1.5 * IQR
outliers = ((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR)))
print(outliers)


# In[50]:


ax = sns.boxplot(data, orient="h", palette="Set2")


# ##### No Outliers

# ### Imputation of Missing Values

# In[53]:


from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor


# In[55]:


imputer = IterativeImputer(estimator=RandomForestRegressor(), max_iter=10, random_state=0)
imputed_data = imputer.fit_transform(data)
imputed_data = pd.DataFrame(imputed_data, columns=data.columns)


# In[ ]:


#dataset.fillna(dataset.median(),inplace=True)


# In[56]:


imputed_data.isnull().sum()


# In[60]:


df=pd.concat([data_2,imputed_data],axis=1)


# In[61]:


df.head(2)


# In[62]:


df.isnull().sum()


# In[65]:


df.describe()


# ### Exploratory Data Analysis
