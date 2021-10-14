#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])


# In[ ]:


#Exercise 1
fruits.size


# In[ ]:


#Exercise 2
fruits.index


# In[ ]:


#Exercise 3
fruits.values


# In[ ]:


#Exercise 4
fruits.dtype


# In[ ]:


#Exercise 5
fruits.head()
fruits.tail(3)
fruits.sample(2)


# In[ ]:


#Exercise 6
fruits.describe()


# In[ ]:


#Exercise 7
fruits.unique()


# In[ ]:


#Exercise 8
fruits.nunique()


# In[ ]:


#Exercise 9
fruits.value_counts().idxmax()

#all max ids
fruits.value_counts().nlargest(n = 1, keep = 'all')


# In[ ]:


#Exercise 10
#all min ids
fruits.value_counts().nsmallest(n = 1, keep = 'all')

