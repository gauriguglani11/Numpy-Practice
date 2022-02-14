#!/usr/bin/env python
# coding: utf-8

# # NumPy Searching Arrays
# 

# # Searching arrays
# you can search an array for a certain value and return the indexes that get a match.
# 
# To search an array, use the where() method.

# Q1 FIND THE INDEXES WHERE THE VALUE IS 4?

# In[2]:


import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8,9])

x = np.where(array1 = 4)
print(x)


# if i will not put double equal toh then i will get this error "TypeError: where() got an unexpected keyword argument 'array1'"

# In[4]:


array1 = np.array([1,2,3,4,5,4,4])

x = np.where(array1 == 4)
print(x)


# The example above will return a tuple: (array([3, 5, 6],)
# 
# Which means that the value 4 is present at index 3, 5, and 6.

# Q2 Find the indexes where the values are even:

# In[5]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)


# Q3 Find the indexes where the values are odd:

# In[6]:


arr = np.array([1,2,3,4,5,6,7,8])
x = np.where(arr%2==1)
print(x)


# # Search sorted
# There is a method called searchsort() which performs a binary search in the array, and returns the index where the specified value be inserted to maintain the search order.
# 
# The searchsorted() method is assumed to be used on sorted arrays.

# Q4 Find the indexes where the value 7 should be inserted:

# In[10]:


arr = np.array([6, 7, 8, 9])

x = np.where(arr == 7)

print(x)


# In[11]:


arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)


# Example explained: The number 7 should be inserted on index 1 to remain the sort order.
# 
# The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.

# # Search From the Right Side
# By default the left most index is returned, but we can give side='right' to return the right most index instead.

# In[12]:


arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)


# basically this will help the code to find from the right side. so from right side 2 pe ha 7

# # Multiple Values
# To search for more than one value, use an array with the specified values.

# Q5 Find the indexes where the values 2, 4, and 6 should be inserted:

# In[18]:


arr = np.array([1,3,5,7])
x = np.searchsorted(arr, [2,4,6])
print(x)


# The return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.
