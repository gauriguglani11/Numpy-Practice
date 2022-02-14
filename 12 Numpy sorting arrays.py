#!/usr/bin/env python
# coding: utf-8

# # Sorting Arrays
# Sorting means putting elements in an ordered sequence.
# 
# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
# 
# The NumPy ndarray object has a function called sort(), that will sort a specified array.

# Q1 Sort the array:

# In[1]:


import numpy as np

array = np.array([3,2,0,1])
print(np.sort(array))


# Note: This method returns a copy of the array, leaving the original array unchanged.
# 
# You can also sort arrays of strings, or any other data type:

# Q2 sort the array alphabetically

# In[2]:


array2 = np.array(['banana', 'cherry', 'apple'])
print([np.sort(array2)])


# Q3 Sort a boolean array:

# In[4]:


array3 = np.array([True, False, True])
print(np.sort(array3))


# IF YOU DO NOT THE WRITE THE TRUE, FALSE KA INITIALS IN CAPITAL LETTERS THAN VOH ERROR DEGA 

# # Sorting a 2-D Array
# If you use the sort() method on a 2-D array, both arrays will be sorted:

# In[5]:


array4 = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(array4))


# basically apne apne arrys ke andar ke elements sort ho jayenge
