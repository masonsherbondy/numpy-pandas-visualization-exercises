#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])


# In[ ]:


#Exercise 1 Determine the number of elements in fruits.
fruits.size


# In[ ]:


#Exercise 2 Output only the index from fruits.
fruits.index


# In[ ]:


#Exercise 3 Output only the values from fruits.
fruits.values


# In[ ]:


#Exercise 4 Confirm the data type of the values in fruits.
fruits.dtype


# In[ ]:


#Exercise 5 
#Output only the first five values from fruits. 
#Output the last three values. 
#Output two random values from fruits.
fruits.head()
fruits.tail(3)
fruits.sample(2)


# In[ ]:


#Exercise 6 
#Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()


# In[ ]:


#Exercise 7 Run the code necessary to produce only the unique string values from fruits.
fruits.unique()


# In[ ]:


#Exercise 8 Determine how many times each unique string value occurs in fruits.
fruits.nunique()


# In[ ]:


#Exercise 9 Determine the string value that occurs most frequently in fruits.
fruits.value_counts().idxmax()

#all max ids
fruits.value_counts().nlargest(n = 1, keep = 'all')


# In[ ]:


#Exercise 10 Determine the string value that occurs least frequently in fruits.
#all min ids
fruits.value_counts().nsmallest(n = 1, keep = 'all')

