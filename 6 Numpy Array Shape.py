#!/usr/bin/env python
# coding: utf-8

# # Shape of an Array
# The shape of an array is the number of elements in each dimension.

# # Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

# # Q1 Print the shape of a 2-D array:

# In[1]:


import numpy as np
array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1.shape)


# The example above returns (2, 5), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 5.

# # Q2 Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

# In[17]:


array2 = np.array([1,2,3,4,9,10], ndmin=5)
print(array2)
print('shape of the array is:',array2.shape)


# We check in ine array how many elements are there and of how many dimensions. so like we can see ndmin = 5 means 5 array and each array has 1 element so (1,1,1,1) and one element has 6 nos.
