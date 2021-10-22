#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pyplot module as alias plt
import matplotlib.pyplot as plt  

#import other libraries 
import numpy as np
import math
from random import randint
import random
import pandas as pd


# In[2]:


#Exercise 1
x = [x * .25 for x in range(-22, 23)]
y = [x ** 2 - x + 2 for x in x]
plt.figure(figsize = (10, 6))
plt.scatter(x, y)
plt.grid(True, ls = '--')
plt.title('$y = x^2 - x + 2$')
plt.xlabel('x')
plt.ylabel('y')
plt.annotate('0rigin', xy = (0, 0), xytext = (-4, 10), fontsize = 16, 
             arrowprops={'facecolor': 'green'})
plt.axhline(0, ls = '-', lw = 1, color = 'k')
plt.axvline(0, ls = '-', lw = 1, color = 'k')
plt.savefig('')


# In[3]:


#Exercise 2 okay whoops, did exercise 3 and 4 prior to reading instructions due to enthusiasm
x1 = range(26)
x2 = range(-3, 4)
x3 = range(-2, 7)
x4 = range(38)

y1 = [x1 ** (1 / 2) for x1 in x1]
y2 = [x2 ** (3) for x2 in x2]
y3 = [2 ** x3 for x3 in x3]
y4 = [1 / (x4 + 1) for x4 in x4]

plt.figure(figsize = (15, 10))

plt.subplot(3, 2, 1)
plt.plot(x1, y1,
         c = 'c',
         ls = '--',
         label = '$y = \sqrt{x}$')
plt.title('$y = \sqrt{x}$')
plt.grid()
plt.axhline(0, c = 'k')
plt.axvline(0, c = 'k')
plt.legend()

plt.subplot(3, 2, 2)
plt.plot(x2, y2,
         c = 'm',
        ls = '--', 
        label = '$y = x^3$')
plt.title('$y = x^3$')
plt.grid()
plt.axhline(0, c = 'k')
plt.axvline(0, c = 'k')
plt.legend()

plt.subplot(3, 2, 3)
plt.plot(x3, y3,
         color = 'g',
         marker = '',
         ls = '--',
         label = '$y = 2^x$')
plt.title('$y = 2^x$')
plt.grid()
plt.axhline(0, color = 'k')
plt.axvline(0, color = 'k')
plt.legend()

plt.subplot(3, 2, 4)
plt.plot(x4, y4, 
         c = 'r',
        ls = '--', 
        label = '$1/(x+1)$')
plt.title('y = $1/(x+1)$')
plt.grid()
plt.xlim(-2, 38)
plt.axhline(0, color = 'k')
plt.axvline(0, color = 'k')
plt.axvline(-1, color = 'k', ls = '--')
plt.legend();


# In[4]:


x1 = range(26)
x2 = range(-3, 4)
x3 = range(-2, 7)
x4 = range(13)

y1 = [x ** (1 / 2) for x in x1]
y2 = [x ** (3) for x in x2]
y3 = [2 ** x for x in x3]
y4 = [1 / (x + 1) for x in x4]

plt.figure(figsize = (10, 8))

plt.plot(x1, y1,
        label = '$y = \sqrt{x}$',
        c = 'c')
plt.plot(x2, y2,
        label = '$y = x^3$',
        c = 'm')
plt.plot(x3, y3,
        label = '$y = 2^x$',
        c = 'g')
plt.plot(x4, y4,
        label = '$1/(x+1)$',
        c = 'r')

plt.xlim(-2, 11)
plt.ylim(-5, 7)
plt.grid()
plt.axhline(0, c = 'k')
plt.axvline(0, c = 'k')
plt.axvline(-1, c = 'k', ls = '--')
plt.title('Here, There Be Dragons', fontsize = 17)
plt.annotate('Vertical Asymptote for $1/(x+1)$', xy = (-1, 5), xytext = (-.5, 2), fontsize = 11,
            arrowprops = {'facecolor':'red'})
plt.xlabel('$x-axis$', fontsize = 13)
plt.ylabel('$y-axis$', fontsize = 13)
plt.legend(fontsize = 13);


# In[ ]:




