#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pydataset import data
import pandas as pd
import mason_functions as mf


# In[2]:


#Exercise 1 Copy the code from the lesson to create a dataframe full of student grades.
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})


# In[3]:


#Exercise 1a Create a column named passing_english that indicates whether each student has a passing grade in 
#english.
df['passing_english'] = df.english > 69
df


# In[4]:


#Exercise 1b Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values('passing_english', ascending = False)


# In[5]:


#Exercise 1c Sort the english grades first by passing_english and then by student name. All the students that are 
#failing english should be first, and within the students that are failing english they should be ordered 
#alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to 
#the .sort_values method)
df.sort_values(by = ['passing_english', 'name'])


# In[6]:


#Exercise 1d Sort the english grades first by passing_english, and then by the actual english grade, similar to how
#we did in the last step.
df.sort_values(by = ['passing_english', 'english'], ascending = [False, False])


# In[7]:


#Exercise 1e Calculate each students overall grade and add it as a column on the dataframe. The overall grade is 
#the average of the math, english, and reading grades.
overall_grade = sum([df.math, df.english, df.reading]) / 3
df['overall_grade'] = round(overall_grade, 2)
df


# In[8]:


#Excercise 2 Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg')
mpg


# In[9]:


#Exercise 2i How many rows and columns are there?
if __name__ == '__main__':
    print(mpg.shape)
    print(mpg)


# In[10]:


#Exercise 2ii What are the data types of each column?
mpg.dtypes


# In[11]:


#Exercise 2iii Summarize the dataframe with .info and .describe
mpg.info()
mpg.describe()


# In[12]:


#Exercise 2iv Rename the cty column to city.
mpg.rename(columns={'cty': 'city'}, inplace = True)


# In[13]:


#Exercise 2v Rename the hwy column to highway.
mpg.rename(columns = {'hwy': 'highway'})


# In[14]:


#Exercise 2vi Do any cars have better city mileage than highway mileage?
better_mileage_mask =(mpg['city'] > mpg['hwy'])
city_mpg_better = mpg[better_mileage_mask]
city_mpg_better
#no


# In[15]:


#Exercise 2vii Create a column named mileage_difference this column should contain the difference between highway 
#and city mileage for each car.
mpg['mileage_difference'] = mpg['hwy'] - mpg['city']
mpg


# In[16]:


#Exercise 2viii Which car (or cars) has the highest mileage difference?
mpg['mileage_difference'].max()
largest_diff = mpg['mileage_difference'] == mpg['mileage_difference'].max()
mpg[largest_diff]


# In[17]:


#Exercise 2ix Which compact class car has the lowest highway mileage? The best?
mpg_compact = mpg[mpg['class'] == 'compact']
compact_low = mpg_compact['hwy'] == mpg_compact['hwy'].min()
#the lowest
mpg_compact[compact_low]


# In[18]:


#the best
mpg_compact[mpg_compact.hwy == mpg_compact.hwy.max()]


# In[19]:


#Exercise 2x Create a column named average_mileage that is the mean of the city and highway mileage.
mpg['average_mileage'] = (mpg['city'] + mpg['hwy']) / 2
mpg


# In[20]:


#Exercise 2xi Which dodge car has the best average mileage? The worst?
dodges = mpg[mpg['manufacturer'] == 'dodge']
dodges.average_mileage == dodges.average_mileage.min()
#the worst
dodges[dodges.average_mileage == dodges.average_mileage.min()]


# In[21]:


#the best
dodges[dodges.average_mileage == dodges.average_mileage.max()]


# In[22]:


#Exercise 3 Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

mammals = data('Mammals')
mammals


# In[23]:


#Exercise 3i How many rows and columns are there?
mammals.shape


# In[24]:


#Exercise 3ii What are the data types?
mammals.dtypes


# In[25]:


#Exercise 3iii Summarize the dataframe with .info and .describe
mammals.info()
mammals.describe()


# In[26]:


#Exercise 3iv What is the the weight of the fastest animal?
fastest = mammals['speed'] == mammals['speed'].max()
mammals[fastest]
mammals[fastest].weight
#weight is 55 for the fastest animal


# In[27]:


#Exercise 3v What is the overal percentage of specials?
specials = mammals['specials'].value_counts(normalize = True)
specials[True]
#it's 9.35%s


# In[28]:


#Exercise 3vi How many animals are hoppers that are above the median speed? What percentage is this?
hoppers_mask = mammals['hoppers'] == True
count_good_hoppers = mammals[hoppers_mask]
if __name__ == '__main__':
    print(count_good_hoppers)
mammals['good_hoppers'] = count_good_hoppers['speed'] > 48
best_hoppers = mammals[mammals.good_hoppers == True]
if __name__ == '__main__':
    print(best_hoppers)
best_hoppers.shape[0]
#7 hoppers are above the median speed.
count_good_hoppers.shape[0]
best_hoppers.shape[0] / count_good_hoppers.shape[0]
#7 hoppers out of 11 total are above the median speed. This is 63.64% of hoppers
best_hoppers.shape[0] / mammals.shape[0]
#7 animals out of 107 is 6.54%. 6.54% of animals that are hoppers are above the median speed. 63.64% of hoppers
#are above the median speed

