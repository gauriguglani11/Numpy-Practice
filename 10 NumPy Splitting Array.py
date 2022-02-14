#!/usr/bin/env python
# coding: utf-8

# # NumPy Splitting Array

# # Splitting NumPy Arrays
# Splitting is reverse operation of Joining.
# 
# Joining merges multiple arrays into one and Splitting breaks one array into multiple.
# 
# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

# Q1 SPLIT THE ARRAY IN 3 PARTS

# In[2]:


import numpy as np
array10 = np.array([1, 2, 3, 4, 5, 6])

newarray1 = np.array_split(array10, 3)

print(newarray1)


# Note: The return value is an array containing three arrays.
# 
# If the array has less elements than required, it will adjust from the end accordingly.

# Q2 SPLIT THE ARRAY IN 4 PARTS

# In[3]:


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)


# # Split Into Arrays
# The return value of the array_split() method is an array containing each of the split as an array.
# 
# If you split an array into 3 arrays, you can access them from the result just like any array element:

#     Q3 Access the splitted arrays:

# In[4]:


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])


# # Splitting 2-D Arrays
# Use the same syntax when splitting 2-D arrays.
# 
# Use the array_split() method, pass in the array you want to split and the number of splits you want to do.

# Q4 Split the 2-D array into three 2-D arrays.

# In[5]:


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)


# In[6]:


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)


# In[12]:


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)


# An alternate solution is using hsplit() opposite of hstack()
# 
# Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.

# In[13]:


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)


# Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().
