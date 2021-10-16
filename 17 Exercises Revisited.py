#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import mason_functions as mf

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

fruits_s = pd.Series(fruits)
numbers_s = pd.Series(numbers)


# In[ ]:


#Exercise 1
uppercased_fruits = fruits_s.str.upper()
uppercased_fruits


# In[ ]:


#Exercise 2
capitalized_fruits = fruits_s.str.capitalize()
capitalized_fruits


# In[ ]:


#Exercise 3
fruits_with_more_than_two_vowels = fruits_s[fruits_s.apply(lambda x: mf.count_vowels(x) > 2)]
fruits_with_more_than_two_vowels


# In[ ]:


#Exercise 4
fruits_with_only_two_vowels = fruits_s[fruits_s.apply(lambda x: mf.count_vowels(x) == 2)]
fruits_with_only_two_vowels


# In[ ]:


#Exercise 5
fruits_with_more_than_five_characters = fruits_s[fruits_s.apply(lambda fruit: len(fruit) > 5)]
fruits_with_more_than_five_characters


# In[ ]:


#Exercise 6
fruits_with_five_characters = fruits_s[fruits_s.apply(lambda fruit: len(fruit) == 5)]
fruits_with_five_characters


# In[ ]:


#Exercise 7
fruits_with_less_than_five_characters = fruits_s[fruits_s.apply(lambda fruit: len(fruit) < 5)]
fruits_with_less_than_five_characters


# In[ ]:


#Exercise 8
fruits_length = fruits_s.apply(lambda x: mf.count_characters(x))
fruits_length


# In[ ]:


#Exercise 9
fruits_with_letter_a = fruits_s[fruits_s.str.lower().str.contains('a')]
fruits_with_letter_a


# In[ ]:


#Exercise 10
even_numbers = numbers_s[numbers_s % 2 == 0]
even_numbers


# In[ ]:


#Exercise 11
odd_numbers = numbers_s[numbers_s % 2 == 1]
odd_numbers


# In[ ]:


#Exercise 12
positive_numbers = numbers_s[numbers_s > 0]
positive_numbers


# In[ ]:


#Exercise 13
negative_numbers = numbers_s[numbers_s < 0]
negative_numbers


# In[ ]:


#Exercise 14
more_than_two_numerals = numbers_s[abs(numbers_s) > 9]
more_than_two_numerals


# In[ ]:


#Exercise 15
numbers_squared = numbers_s * numbers_s
numbers_squared


# In[ ]:


#Exercise 16
odd_negative_numbers = numbers_s[(numbers_s < 0) & (numbers_s % 2 == 1)]
odd_negative_numbers


# In[ ]:


#Exercise 17
numbers_plus_5 = numbers_s + 5
numbers_plus_5


# In[ ]:


#BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list.
#*Hint* you may want to make or find a helper function that determines if a given number is prime or not.
import sympy as sp
primes_mask = (numbers_s.apply(lambda n: sp.isprime(n)))
primes = numbers_s[primes_mask]
primes


# In[ ]:




