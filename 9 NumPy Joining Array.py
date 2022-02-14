#!/usr/bin/env python
# coding: utf-8

# # Joining NumPy Arrays
# Joining means putting contents of two or more arrays in a single array.
# 
# In SQL we join tables based on a key, whereas in NumPy we join arrays by axIs.
# 
# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

# Q1 JOIN TWO ARRAYS

# In[1]:


import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

array0 = np.concatenate((array1, array2))
print(array0)


# concatenate string helps in joining 2 arrays

# Q2 JOIN TWO 2D ARRAYS ALONG ROWS(AXIS = 1)

# In[3]:


array1 = np.array([[1,2],[3,4]])
array2 = np.array([[5,6],[7,8]])
array3 = np.concatenate((array1, array2), axis=1)
print(array3)


# we used axis above, so it all came in 1 axis but we dont use axis then below will be the output

# In[5]:


array1 = np.array([[1,2],[3,4]])
array2 = np.array([[5,6],[7,8]])
array3 = np.concatenate((array1, array2))
print(array3)


# this output we will get when we do not use axis

# # Joining Arrays Using Stack Functions
# 

# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# 
# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
# 
# We pass a sequence of arrays that we want to join to the stack() method along with the axis. 
# If axis is not explicitly passed it is taken as 0.

# In[8]:


array11 = np.array([1,2,3])
array12 = np.array([4,5,6])
array13 = np.stack((array11,array12), axis = 1)
print(array13)


# # Stacking Along Rows

# NumPy provides a helper function: hstack() to stack along rows.
# hstack isliye because rows are horizontal so h stack

# In[11]:


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)


# # Stacking Along Columns

# NumPy provides a helper function: vstack()  to stack along columns.
# vstack isliye because rows are vertical so v stack

# In[12]:


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)


# # Stacking Along Height (depth)

# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

# In[13]:


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)


# here in the above example we can see, dstack sleeping ko standing kar rha ha and standing ko sleeping. like 123 in sleeping are now in standing. and14 in standing are in sleeping now.
