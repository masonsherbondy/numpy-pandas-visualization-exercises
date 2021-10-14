#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mason_functions as mf


# ## Exercises Part I

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


# # Exercises Part II

# In[ ]:


#Exercise I Capitalize all the string values in fruits.
fruits.str.capitalize()


# In[ ]:


#Exercise II Count the letter "a" in all the string values (use string vectorization).
fruits.str.count('a')


# In[ ]:


#Exercise III Output the number of vowels in each and every string value.
fruits.apply(mf.count_vowels)


# In[ ]:


#Exercise IV Write the code to get the longest string value from fruits.
max(fruits, key = len)


# In[ ]:


#Exercise V Write the code to get the string values with 5 or more letters in the name.
fruits[fruits.apply(lambda fruit: len(fruit) > 4)]


# In[ ]:


#Exercise VI 
#Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
fruits[fruits.apply(lambda fruit: fruit.count('o') > 1)]


# In[ ]:


#Exercise VII Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]


# In[ ]:


#Exercise VIII Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]


# In[ ]:


#Exercise IX Which string value contains the most vowels?
max(fruits, key = mf.count_vowels)


# # Exercises Part III

# In[ ]:


#A

letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))


# In[ ]:


#Exercise AI Which letter occurs the most frequently in the letters Series?
letters.value_counts().nlargest(n = 1, keep = 'all')


# In[ ]:


#Exercise AII Which letter occurs the Least frequently?
letters.value_counts().nsmallest(n = 1, keep = 'all')


# In[ ]:


#Exercise AIII How many vowels are in the Series?
mf.count_vowels(letters)


# In[ ]:


#Exercise AIV How many consonants are in the Series?
mf.count_consonants(letters)


# In[ ]:


#Exercise AV Create a Series that has all of the same letters but uppercased.
letters.str.upper()


# In[ ]:


#Exercise AVI Create a bar plot of the frequencies of the 6 most commonly occuring letters.
letters.value_counts().nlargest(n = 6, keep = 'first').plot.bar(color = 'm',
                                                                ec = 'k',
                                                               width = .9)
plt.xlabel('Frequent Flier', fontsize = 13, c = 'm')
plt.ylabel('Flybys', fontsize = 13, c = 'k')

