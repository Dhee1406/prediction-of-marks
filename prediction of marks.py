#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


s_data = pd.read_csv("http://bit.ly/w-data")
print(s_data)


# In[3]:


s_data.head(4)


# In[4]:


s_data.plot()


# In[5]:


s_data.plot(style='0')


# In[6]:


s_data.plot(X = 'hours', y= 'scores', style= '0')


# In[7]:


X = s_data.iloc[ : , :-1 ].values


# In[8]:


y = s_data.iloc[ : , :-1].values


# In[10]:


X.shape
y.shape


# In[11]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[12]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)


# In[13]:


df = pd.Dataframe({'Actual':y_test,'Predicted':y_pred})
df


# In[14]:


from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, y_pred)


# In[ ]:




