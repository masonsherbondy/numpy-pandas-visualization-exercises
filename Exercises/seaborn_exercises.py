#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mason_functions as mf
from pydataset import data


# # Exercises Part I

# In[2]:


#Use the iris database to answer the following quesitons:
def get_db_url(db_name):
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


# In[3]:


#Exercise 1 What does the distribution of petal lengths look like?
sql = """
SELECT *
FROM measurements
"""
url = get_db_url('iris_db')
measurements = pd.read_sql(sql, url)
measurements.info()
measurements.describe()

sns.displot(data = measurements, x = 'petal_length', color = 'blue', aspect = 1.1, kde = True, rug = True)


# In[4]:


#Exercise 2 Is there a correlation between petal length and petal width?
sns.relplot(data = measurements, x = 'petal_length', y = 'petal_width', hue = 'species_id')
#there is a positive correlation


# In[5]:


#Exercise 3 Would it be reasonable to predict species based on sepal width and sepal length?
sns.relplot(data = measurements, x = 'sepal_width', y = 'sepal_length', hue = 'species_id')
#not really, no


# In[6]:


#Exercise 4 Which features would be best used to predict species?
sns.pairplot(data = measurements, hue = 'species_id')
#petal length and petal width


# # Exercises Part II

# # Exercise 1

# Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?
# 
# Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

# In[7]:


anscombe = sns.load_dataset('anscombe')
anscombe.info()
anscombe.describe()


# In[8]:


anscombe


# In[9]:


anscombe.groupby('dataset').agg(['count', 'mean', 'median', 'max', 'min'])
#I notice all of the x values are integer-like and all of the y values are float-like.
#the mean is nearly the same for all datasets, it is the same for the x value, and it is damn near the same for the
#y values, the exception being dataset III, off by about .000909.
#all of the x summary statistics are the same or close across the different data sets, and all the y summary statistics
#are simply close across the datasets (besides the mean, which is practically identical across sets).
#there are 11 x-values and 11 y-values for each dataset


# In[10]:


sns.relplot(data = anscombe, x = 'x', y = 'y', col = 'dataset')


# In[11]:


sns.lmplot(data = anscombe, x = 'x', y = 'y', col = 'dataset')


# # Exercise 2

# Exercise 2 Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows the effectiveness of the different insect sprays.

# In[12]:


InsectSprays = data("InsectSprays")
data('InsectSprays', show_doc = True)


# In[13]:


InsectSprays.sample(5)
InsectSprays.value_counts('spray')


# In[14]:


sns.boxplot(data = InsectSprays, x = 'spray', y = 'count')


# # Exercise 3

# Load the swiss dataset and read it's documentation. The swiss dataset is available from pydatset rather than seaborn. Create visualizations to answer the following questions:
# 
# Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic)
# Does whether or not a province is Catholic influence fertility?
# What measure correlates most strongly with fertility?
# 

# In[15]:


swiss = data('swiss')
swiss


# In[16]:


data('swiss', show_doc = True)


# In[17]:


swiss.info()


# In[18]:


swiss['is_catholic'] = swiss['Catholic'] >= 50
swiss


# In[19]:


sns.relplot(data = swiss, x = 'Catholic', y = 'Fertility')
#no, there is no correlation between catholic and fertility measure


# In[20]:


sns.relplot(data = swiss, y = 'Fertility', x = 'Education', kind = 'line')
#The education measure correlates most strongly with fertility


# In[ ]:





# # Exercise 4

# Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.

# In[21]:


sql = """
SELECT * 
FROM orders
"""
url = get_db_url('chipotle')
chipotle = pd.read_sql(sql, url)
chipotle


# In[22]:


four_most_popular = chipotle.groupby('item_name').quantity.sum().nlargest(n = 4, keep = 'all')
four_most_popular
four_most_popular.index


# In[23]:


chipotle['prices_as_floats'] = chipotle.item_price.apply(lambda x: mf.handle_commas(x))


# In[24]:


total_revenue_per_item = chipotle.groupby('item_name').prices_as_floats.sum()
total_revenue_per_item


# In[25]:


bar_me = total_revenue_per_item[four_most_popular.index]
bar_me = bar_me.reset_index()
bar_me


# In[26]:


sns.barplot(data = bar_me, x = 'item_name', y = 'prices_as_floats')
plt.ylabel('Total revenue')
plt.xlabel('Item Name')
plt.tight_layout


# # Exercise 5

# Load the sleepstudy data and read it's documentation. Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.

# In[27]:


sleep = data('sleepstudy')
sleep


# In[28]:


data('sleepstudy', show_doc = True)


# In[29]:


sleep.sample(5)


# In[30]:


sleep['Subject'] = 'Subject_' + sleep.Subject.astype(str) 


# In[31]:


plt.figure(figsize = (16, 9))
sns.lineplot(data = sleep, x = 'Days', y = 'Reaction', hue = 'Subject')
sns.lineplot(data = sleep, x = 'Days', y = 'Reaction', color = 'black', estimator = 'mean')
plt.ylabel('Reaction Time (ms)')
plt.xlabel('Days Without Sleep')


# In[ ]:




