#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[ ]:


#Exercise 1 How many negative numbers are there?
negatives = a[a < 0]
len(negatives)


# In[ ]:


#Exercise 2 How many positive numbers are there?
positives = a[a > 0]
len(positives)


# In[ ]:


#Exercise 3 How many even positive numbers are there?
even_positives = a[(a > 0) & (a % 2 == 0)]
len(even_positives)


# In[ ]:


#Exercise 4 If you were to add 3 to each data point, how many positive numbers would there be?
add_3 = a + 3
len(add_3[a > 0])


# In[ ]:


#Exercise 5 If you squared each number, what would the new mean and standard deviation be?
squared_away = a ** 2

if __name__ == '__main__':
    print(squared_away.mean())
    print(squared_away.std())


# In[ ]:


#Exercise 6 Center the data set.
this_mean = a.mean()
centered = a - this_mean
if __name__ == '__main__':
    print(centered.mean())


# In[ ]:


#Exercise 7 Calculate the z-score for each data point.
s_dev = a.std()
z_score = (a - this_mean) / s_dev
if __name__ == '__main__':
    print(z_score)


# In[ ]:


#Exercise 8
# Life w/o numpy to life with numpy


## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
a = np.array(a)
sum_of_a = a.sum()

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = a.min()

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = a.max()

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = a.mean()

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = np.product(a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = a * a

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = a[a % 2 != 0]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a[a % 2 == 0]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

b = np.array(b)
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = b.sum()

# Exercise 2 - refactor the following to use numpy. 
min_of_b = b.min()  

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = b.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = b.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = np.product(b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = b * b


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = b[b % 2 != 0]


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b[b % 2 == 0]

# Exercise 9 - print out the shape of the array b.
b.shape

# Exercise 10 - transpose the array b.
b.transpose

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.reshape((1, 6))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape((6, 1))

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c.min()
c.max()
c.sum()
product_c = np.product(c)
# Exercise 2 - Determine the standard deviation of c.
c.std()
# Exercise 3 - Determine the variance of c.
c.var()
# Exercise 4 - Print out the shape of the array c
c.shape
# Exercise 5 - Transpose c and print out transposed result.
ctrans = np.transpose(c)
if __name__ == '__main__':
    print(ctrans)
# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c, c)
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
productc = c * ctrans
productc.sum()
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
product_c = np.product(productc)
product_c

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
sin_d = np.sin(d)
# Exercise 2 - Find the cosine of all the numbers in d
cosine_d = np.cos(d)
# Exercise 3 - Find the tangent of all the numbers in d
tang_d = np.tan(d)
# Exercise 4 - Find all the negative numbers in d
d[d < 0]
# Exercise 5 - Find all the positive numbers in d
d[d > 0]
# Exercise 6 - Return an array of only the unique numbers in d.
import itertools as it
list_d = d.tolist()
gotta_d_list = list(it.chain.from_iterable(list_d))
unique_d = set(gotta_d_list)
unique_d = np.array(unique_d)
unique_d
# Exercise 7 - Determine how many unique numbers there are in d.
unique_d_2 = set(gotta_d_list)
len(unique_d_2)
# Exercise 8 - Print out the shape of d.
d.shape
# Exercise 9 - Transpose and then print out the shape of d.
trans_d = np.transpose(d)
trans_d.shape
# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9, 2)

