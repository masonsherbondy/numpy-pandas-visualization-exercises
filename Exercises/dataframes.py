#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pydataset import data
import pandas as pd
import mason_functions as mf


# In[4]:


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


# In[13]:


#Exercise 1a Create a column named passing_english that indicates whether each student has a passing grade in 
#english.
df['passing_english'] = df.english > 69
df


# In[15]:


#Exercise 1b Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values('passing_english', ascending = False)


# In[25]:


#Exercise 1c Sort the english grades first by passing_english and then by student name. All the students that are 
#failing english should be first, and within the students that are failing english they should be ordered 
#alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to 
#the .sort_values method)
df.sort_values(by = 'name').sort_values(by = 'passing_english')


# In[26]:


#Exercise 1d Sort the english grades first by passing_english, and then by the actual english grade, similar to how
#we did in the last step.
df.sort_values(by = 'english').sort_values(by = 'passing_english')


# In[29]:


#Exercise 1e Calculate each students overall grade and add it as a column on the dataframe. The overall grade is 
#the average of the math, english, and reading grades.
overall_grade = sum([df.math, df.english, df.reading]) / 3
df['overall_grade'] = overall_grade
df


# In[40]:


#Excercise 2 Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg')


# In[31]:


#Exercise 2i How many rows and columns are there?


# In[32]:


#Exercise 2ii What are the data types of each column?


# In[33]:


#Exercise 2iii Summarize the dataframe with .info and .describe


# In[34]:


#Exercise 2iv Rename the cty column to city.


# In[35]:


#Exercise 2v Rename the hwy column to highway.


# In[36]:


#Exercise 2vi Do any cars have better city mileage than highway mileage?


# In[37]:


#Exercise 2vii Create a column named mileage_difference this column should contain the difference between highway 
#and city mileage for each car.


# In[38]:


#Exercise 2viii Which car (or cars) has the highest mileage difference?


# In[39]:


#Exercise 2ix Which compact class car has the lowest highway mileage? The best?


# In[ ]:


#Exercise 2x Create a column named average_mileage that is the mean of the city and highway mileage.

