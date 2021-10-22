#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import mason_functions as mf


# # Exercises Part I

# In[2]:


#Exercise 3 Create a function named get_db_url. It should accept a username, hostname, password, and database
#name and return a url connection string formatted like in the example at the start of this lesson.
def get_db_url(db_name):
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


# In[3]:


#Exercise 4 Use your function to obtain a connection to the employees database.
sql = """
    SELECT * FROM employees LIMIT 1010
"""

url = get_db_url('employees')
tt = pd.read_sql(sql, url)
tt.head()


# In[ ]:


#Exercise 5a  Intentionally make a typo in the database url. What kind of error message do you see?
url = get_db_url('Employees')
q2 = pd.read_sql(sql, url)
#OperationalError: (pymysql.err.OperationalError) (1044, "Access denied for user 'hopper_1550'@'%' to database 'Employees'")
#(Background on this error at: http://sqlalche.me/e/14/e3q8)


# In[ ]:


#Exercise 5b Intentionally make an error in your SQL query. What does the error message look like?
sql = """ SELECT * FROM employee"""
url = get_db_url('employees')
q3 = pd.read_sql(sql, url)
#ProgrammingError: (pymysql.err.ProgrammingError) (1146, "Table 'employees.employee' doesn't exist")
#[SQL:  SELECT * FROM employee]
#(Background on this error at: http://sqlalche.me/e/14/f405)
q3

sql = """ 
    SELECT *
    FROM employees
    WHERE first_nam = 'Maya'
"""
q4 = pd.read_sql(sql, url)
q4
#OperationalError: (pymysql.err.OperationalError) (1054, "Unknown column 'first_nam' in 'where clause'")
#[SQL:  
#    SELECT *
#    FROM employees
#    WHERE first_nam = 'Maya'
#]
#(Background on this error at: http://sqlalche.me/e/14/e3q8)


# In[4]:


sql = """ 
    SELECT * FROM titles WHERE to_date != "9999-01-01" ORDER BY to_date DESC LIMIT 1
"""
url = get_db_url('employees')
q4 = pd.read_sql(sql, url)
q4


# In[5]:


#Exercise 6 Read the employees and titles tables into two separate DataFrames.
e_sql = """
SELECT *
FROM employees
"""
t_sql = """
SELECT *
FROM titles
"""
employees_table = pd.read_sql(e_sql, url)
titles_table = pd.read_sql(t_sql, url)
e_df = pd.DataFrame(employees_table)
t_df = pd.DataFrame(titles_table)


# In[6]:


t_df


# In[7]:


#Exercise 7 How many rows and columns do you have in each DataFrame? Is that what you expected?
if __name__ == '__main__':
    print(e_df.shape)
    print(t_df.shape)
#kinda


# In[8]:


#Exercise 8 Display the summary statistics for each DataFrame.
t_df.info()
t_df.describe()
e_df.info()
e_df.describe()


# In[9]:


#Exercise 9 How many unique titles are in the titles DataFrame?
len(t_df.title.unique())


# In[10]:


#Exercise 10 What is the oldest date in the to_date column?
oldest_to_date = t_df.sort_values(by = 'to_date').head(1)
oldest_to_date.to_date


# In[11]:


#Exercise 11 What is the most recent date in the to_date column?
most_recent_to_date = t_df.sort_values(by = 'to_date', ascending = False).head(1)
most_recent_to_date.to_date


# # Exercises Part II

# In[12]:


#Exercise 1 Copy the users and roles DataFrames from the examples above.
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users
if __name__ == '__main__':
    print(roles)
    print(users)


# In[13]:


#Exercise 2 What is the result of using a right join on the DataFrames?
users.merge(roles, left_on = 'role_id', right_on = 'id', how = 'right')


# In[14]:


#Exercise 3 What is the result of using an outer join on the DataFrames?
users.merge(roles, left_on = 'role_id', right_on = 'id', how = 'outer')


# In[ ]:


#Exercise 4 What happens if you drop the foreign keys from the DataFrames and try to merge them?
roles.drop(columns = 'id', inplace = True)
users.drop(columns = 'role_id', inplace = True)
users.merge(roles, left_on = 'role_id', right_on = 'id', how = 'outer')


# In[15]:


#Exercise 5 Load the mpg dataset from PyDataset.
from pydataset import data
mpg = data('mpg')
mpg


# In[16]:


#Exercise 6 Output and read the documentation for the mpg dataset.
data('mpg', show_doc = True)


# In[17]:


#Exercise 7 How many rows and columns are in the dataset?
mpg.shape


# In[17]:


#Exercise 8 Check out your column names and perform any cleanup you may want on them.
mpg.rename(columns = {'cty': 'city'}, inplace = True)
mpg


# In[18]:


#Exercise 9 Display the summary statistics for the dataset.
mpg.info()
mpg.describe()


# In[19]:


#Exercise 10 How many different manufacturers are there?
len(mpg.manufacturer.unique())


# In[20]:


#Exercise 11 How many different models are there?
len(mpg.model.unique())


# In[21]:


#Exercise 12 Create a column named mileage_difference like you did in the DataFrames exercises; this column should
#contain the difference between highway and city mileage for each car.
mpg['mileage_difference'] = mpg.hwy - mpg.city
mpg


# In[22]:


#Exercise 13 Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the
#city and highway mileage.
mpg['average_mileage'] = mpg[['city', 'hwy']].mean(axis = 1)
mpg


# In[23]:


#Exercise 14 Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether
#the car has an automatic transmission.
mpg['is_automatic'] = mpg.trans.str.contains('auto')
mpg


# In[24]:


#Exercise 15 Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
if __name__ == '__main__':
    print(mpg.groupby('manufacturer').average_mileage.max().nlargest(n = 1, keep = 'all'))
#alternatively
(mpg.groupby('manufacturer').average_mileage.max()).idxmax()


# In[25]:


#Exercise 16 Do automatic or manual cars have better miles per gallon?
mpg.groupby('is_automatic').average_mileage.max()
(mpg.groupby('is_automatic').average_mileage.max()).idxmax()
mpg.groupby('is_automatic').average_mileage.max().nlargest(n = 1, keep = 'all')
#manual cars have better mpg


# # Exercises Part III

# In[26]:


#Exercise 1 Use your get_db_url function to help you explore the data from the chipotle database.
url = get_db_url('chipotle')
sql = """
SELECT *
FROM orders
"""
chipotle = pd.read_sql(sql, url)
chipotle.describe()
chipotle.info()
chipotle


# In[27]:


#Exercise 2 What is the total price for each order?
type(chipotle.groupby('order_id').item_price.sum())
chipotle_orders = chipotle.groupby('order_id').item_price.sum()
chipotle['prices_as_floats'] = chipotle.item_price.apply(lambda x: mf.handle_commas(x))
total_prices = chipotle.groupby('order_id').prices_as_floats.sum()
total_prices


# In[28]:


#Exercise 3 What are the most popular 3 items?
chipotle.groupby('item_name').quantity.sum().nlargest(n = 3, keep = 'all')


# In[29]:


#Exercise 4 Which item has produced the most revenue?
chipotle.groupby('item_name').prices_as_floats.sum().nlargest(n = 1, keep = 'all')


# In[30]:


#Exercise 5 Join the employees and titles DataFrames together.
titles_and_emps = t_df.merge(e_df, on = 'emp_no', how = 'inner')
titles_and_emps.head()


# In[31]:


#Exercise 6 For each title, find the hire date of the employee that was hired most recently with that title.
titles_and_emps.hire_date = pd.to_datetime(titles_and_emps.hire_date)
titles_and_emps.from_date = pd.to_datetime(titles_and_emps.from_date)
if __name__ == '__main__':
    print(titles_and_emps.groupby('title').from_date.max())
    print(titles_and_emps.groupby('title').hire_date.max())


# In[32]:


#Exercise 7 Write the code necessary to create a cross tabulation of the number of titles by department. 
#(Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas code to perform 
#the manipulations.)
url = get_db_url('employees')
sql = """
SELECT title, dept_name
FROM employees
JOIN titles USING(emp_no)
JOIN dept_emp USING(emp_no)
JOIN departments USING(dept_no)
WHERE dept_emp.to_date > NOW()
"""
the_crosst = pd.read_sql(sql, url)
pd.crosstab(the_crosst.title, the_crosst.dept_name)


# In[ ]:




