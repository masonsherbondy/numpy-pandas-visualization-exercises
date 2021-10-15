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
letters.value_counts(normalize = True).nlargest(n = 6, keep = 'first').plot.bar(color = 'm',
                                                                ec = 'k',
                                                               width = .9)
plt.xlabel('Alphabetical Frequenter', fontsize = 13, c = 'm')
plt.ylabel('Frequency', fontsize = 13, c = 'm')
plt.title('Letters Frequency', fontsize = 16, c = 'r')


# In[ ]:


#B


numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])


# In[ ]:


#Exercise BI What is the data type of the numbers Series?
numbers.dtype


# In[ ]:


#Exercise BII How many elements are in the number Series?
numbers.size


# In[ ]:


#Exercise BIII Perform the necessary manipulations by accessing Series attributes and methods to convert the
#numbers Series to a numeric data type.

numbers.apply(lambda x: mf.handle_commas(x))


# In[ ]:


#Exercise BIV Run the code to discover the maximum value from the Series.
max(numbers, key = lambda x: mf.handle_commas(x))


# In[ ]:


#Exercise BV Run the code to discover the minimum value from the Series.
min(numbers, key = lambda x: mf.handle_commas(x))


# In[ ]:


#Exercise BVI What is the range of the values in the Series?
range(numbers.size + 1)


# In[ ]:


#Exercise BVII Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
numbers.apply(lambda x: mf.handle_commas(x)).value_counts(bins = 4).sort_index()


# In[ ]:


#Exercise BVIII Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
plt.figure(figsize = (11, 7))
numbers.apply(lambda x: mf.handle_commas(x)).value_counts(bins = 4).sort_index().plot.barh()
plt.title('We got bins', fontsize = 38)
plt.ylabel('Bin range', fontsize = 27)
plt.xlabel('Number of values in Bin', fontsize = 27)
plt.yticks(fontsize = 15)
plt.xticks(fontsize = 14);


# In[ ]:


#C


exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
exam_scores


# In[ ]:


#Exercise CI How many elements are in the exam_scores Series?
exam_scores.size


# In[ ]:


#Exercise CII Run the code to discover the minimum, the maximum, the mean, and the median scores for the
#exam_scores Series.
if __name__ == '__main__':
    print(exam_scores.describe())
    print(exam_scores.median())


# In[ ]:


exam_scores.sort_values


# In[ ]:


#Exercise CIII Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
plt.figure(figsize = (51, 29))
exam_scores.plot.barh(color = 'indigo', ec = 'cyan', width = .98)
plt.title('Exam Score by #', fontsize = 69)
plt.xlabel('Score', fontsize = 44, c = 'indigo')
plt.ylabel('Exam #/ Exam Participant #', fontsize = 44, c = 'gray')
plt.xticks(range(101), fontsize = 19)
plt.yticks(range(21), fontsize = 38);


# In[ ]:


#Exercise CIV Write the code necessary to implement a curve for your exam_grades Series and save this 
#as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points
#to every other score in the Series as well.

curved_grades = exam_scores + 4
curved_grades


# In[ ]:


#Exercise CV Use a method to convert each of the numeric values in the curved_grades Series into a categorical 
#value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named 
#letter_grades.

letter_grades = curved_grades.apply(lambda x: mf.get_letter_grade(x))
letter_grades


# In[ ]:


#Exercise CVI Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
plt.figure(figsize = (8, 5))
letter_grades.value_counts(ascending = True).plot.barh(color = 'purple', ec = 'k', width = .88)
plt.title('Letter Grades', fontsize = 16, c = 'indigo')
plt.xlabel('Quantity', fontsize = 13, c = 'm')
plt.ylabel('Letter Grade', fontsize = 13, c = 'purple')

