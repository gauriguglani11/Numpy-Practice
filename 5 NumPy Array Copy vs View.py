#!/usr/bin/env python
# coding: utf-8

# The Difference Between Copy and View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
# 
# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
# 
# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

# # Q1. Make a copy, change the original array, and display both arrays:

# In[4]:


import numpy as np

array1 = np.array([1,2,3,4,5,6,7])
x = array1.copy()
array1[5] = 42
array1[1] = 12
array1[1] = 13
print(array1)
print(x)


# In the above example, array1 is the orignal array and x is the copied array. array ke 5th locn pe change kiya toh copied mein chaanges hua because copy array will make a new data for them

# # Q2. Make a view, change the original array, and display both arrays:

# In[8]:


array2 = np.array([1,2,3,4,5,6,7])
x = array2.view()
array2[0] = 42
print(array2)
print(x)


# here view doesnt create a new array of data for them, they do the changes in the old array itself 

# # Q3. Make a view, change the view, and display both arrays:

# In[9]:


array3 = np.array([1,2,3,4,5,6,7])

x = array3.view()
x[2] = 31
print(array3)
print(x)


# The original array SHOULD be affected by the changes made to the view.

# # Q4. Print the value of the base attribute to check if an array owns it's data or not:

# In[18]:


import numpy as np
array5 = np.array([1,2,3,4,5,9])
x = array5.copy()
y = array5.view()
array5[5] = 6
print(x)
print(array5)
print(x.base)
print(y.base)


# base object if memory is from some other object.
