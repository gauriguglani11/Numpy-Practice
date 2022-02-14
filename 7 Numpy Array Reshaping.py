#!/usr/bin/env python
# coding: utf-8

# # Reshaping arrays
# Reshaping means changing the shape of an array.
# 
# The shape of an array is the number of elements in each dimension.
# 
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

# # Reshape from 1D to 2D
# Q1. convert the 1d array with 12 elements into a 2d array. The outermost dimension will have 4 arrays, each with 3 elements:

# In[1]:


import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarray = array1.reshape(4,3)
print(newarray)


# In the above example, bracket mein 1st(4) one is how many arrays we want and 2nd(3) is the ek element mein kitne arrays hone chaiye.

# # Reshape From 1-D to 3-D
# Q2. Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

# In[2]:


array3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarray5 = array3.reshape(2,3,2)
print(array3)
print(newarray5)


# # Can We Reshape Into any Shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.
# 
# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.
# 
# Example

# In[5]:


array6 = np.array([1,2,3,4,5,6,7,8])
newarray6 = array6.reshape(3,3)
print(newarray6)


# In[6]:


array6 = np.array([1,2,3,4,5,6,7,8,9])
newarray6 = array6.reshape(3,3)
print(newarray6)


# as we have seen in the above 2 codes, as in the 1st code we have 8 elements and we need 3 cross 3, so with 8 elements it is not possible and for the 2nd code there it is 9 elements so we can do 3 cross 3 and it is successfull.

# # Returns Copy or View?
# Example
# Check if the returned array is a copy or a view:

# In[9]:


array0 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(array0.reshape(2, 4).base)


# The example above returns the original array, so it is a view.

# # Unknown Dimension
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.

# Q2. Convert 1D array with 8 elements to 3D array with 2x2 elements:

# In[13]:


array9 = np.array([1,2,3,4,5,6,7,8]) 
newarray = array9.reshape(2,2,-1)
print(newarray)


# Note: We can not pass -1 to more than one dimension.

# # Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.

# In[15]:


array8 = np.array([[1, 2, 3], [4, 5, 6]])

newarray8 = array8.reshape(-1)

print(newarray8)


# As in the above example we can seeit is a 2 d array but after using -1 it converted from 2d to 1d array.

# Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy
