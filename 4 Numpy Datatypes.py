#!/usr/bin/env python
# coding: utf-8

# # Get the data type of an array object:

# In[1]:


import numpy as np

array1 = np.array([1,2,3,4])
print(array1.dtype)


# dtype property tells u which data type of your array

# # Get the data type of an array containing strings:

# In[2]:


array1 = np.array(['apple', 'banana', 'cherry'])
print(array1.dtype)


# # Creating Arrays With a Defined Data Type
# EXAMPLE 1:- reate an array with data type string:

# In[16]:


array1 = np.array([1,2,3,4], dtype= 'S')
print(array1)
print(array1.dtype)


# # Create an array with data type 4 bytes integer:

# In[5]:


array1 = np.array([1, 2, 3, 4], dtype='i4')

print(array1)
print(array1.dtype)


# In[9]:


arr = np.array(['a', '2', '3'], dtype='i')


# Here value error will come because we have given data type as I and in the array we have mentioned 'a'
# A non integer string like 'a' can not be converted to integer (will raise an error):

# In[12]:


array1 = np.array(['1', '2', '3'], dtype='i')
print(array1)
print(array1.dtype)


# # Converting Data Type on Existing
# 1. The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
# 2. The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

# # Q1. Change data type from float to integer by using 'i' as parameter value: 

# In[24]:


arr = np.array([2.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)


# # Q2. Change data type from float to integer by using int as parameter value:

# In[27]:


array3 = np.array([2.1,3.7,9.1])

newarray3 = array3.astype(int)
print(newarray3)
print(newarray3.dtype)


# # Q3. Change data type from integer to boolean:

# In[29]:


array4 = np.array([1, 0, 3])

newarray4 = arr.astype(bool)

print(newarray4)
print(newarray4.dtype)


# 
