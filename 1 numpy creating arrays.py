#!/usr/bin/env python
# coding: utf-8

# # Numpy basics

# In[1]:


import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)


# In[2]:


import numpy as np

print(np.__version__)


# # Numpy creating arrays

# In[4]:


import numpy as np
array= numpy.array([6,7,8,9,10])
print(array)
print(type(array))


# # Use a tuple to create a NumPy array

# In[5]:


import numpy as np
arr = np.array((1, 2, 3, 4, 5))
print(arr)


# # Dimensional arrays
# A dimension in arrays is one level of array depth (nested arrays).
# nested array: are arrays that have arrays as their elements.

# # 0-D array
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

# # Create a 0-D array with value 90

# In[6]:


arraygg = np.array(90)
print(arraygg)


# # Create a 1-D array containing the values 1,2,3,4,5

# In[8]:


arraygg = np.array({1,2,3,4,5})
print(arraygg)


# # Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

# In[11]:


arraygg = np.array([[1,2,3],[5,6,7]])
print(arraygg)


# # Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6

# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# 
# These are often used to represent a 3rd order tensor.

# In[12]:


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)


# # Check how many dimensions the arrays have

# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

# In[13]:


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# # Create an array with 5 dimensions and verify that it has 5 dimensions:

# In[19]:


a = np.array([1, 2, 3, 4], ndmin=5)

print(a)
print('number of dimensions :', a.ndim)

