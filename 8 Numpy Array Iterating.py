#!/usr/bin/env python
# coding: utf-8

# # Iterating Arrays
# Iterating means going through elements one by one.
# 
# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
# 
# If we iterate on a 1-D array it will go through each element one by one.

# Q1. Iterate on the elements of the following 1-D array:

# In[1]:


import numpy as np
array1 = np.array([1,2,3])

for x in array1:
    print(x)


# # Iterating 2-D Arrays
# In a 2-D array it will go through all the rows.
# 

# Q2. Iterate on the elements of the following 2-D array:

# In[2]:


array2 = np.array([[1,2,3],[4,5,6]])
for x in array2:
    print(x)


# # If we iterate on a n-D array it will go through n-1th dimension one by one.
# To return the actual values, the scalars, we have to iterate the arrays in each dimension.

# Q3. Iterate on each scalar element of the 2-D array:

# In[15]:


array3 = np.array([[1,2,3],[4,5,6]])
for x in array3:
    for y in x:
        print(y)
        


# # Iterating 3-D Arrays
# In a 3-D array it will go through all the 2-D arrays.

# Q4 Iterate on the elements of the following 3-D array:

# In[17]:


array4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in array4:
  print(x)


# In[25]:


array0 = np.array([1, 2, 3], ndmin = 5)
for x in array0:
    print(x)


# # To return the actual values, the scalars, we have to iterate the arrays in each dimension.

# Q5 Iterate down to the scalars:

# In[31]:


array5 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in array5:
            for y in x:
                for z in y:
                   print(z)


# # Iterating Arrays Using nditer()

# The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration
# 
# Iterating on Each Scalar Element
# 
# In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.

# Q6 Iterate through the following 3-D array:

# In[37]:


array6 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(array6):
  print(x)


# # Iterating Array With Different Data Types

# a. We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
# b. NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

# Q7 Iterate through the array as a string:

# In[39]:


array7 = np.array([1,2,3])
for x in np.nditer(arr, op_dtypes= ['S']):
    print(x)


# as we can see in the above example, numpy needs extra space to change data type and his is done by buffering and we have not given that extra space, so we got error about copying or buffering is not enabled

# In[41]:


array7 = np.array([1,2,3])
for x in np.nditer(arr, flags = ['buffered'], op_dtypes= ['S']):
    print(x)


# now we can see above, as we entered the buffered flags code worked and gave the space to convert form int to strings. so[1,2,3] ka hogya [b1,b2.b3]

# # Iterating With Different Step Size
# We can use filtering and followed by iteration.

# Q8 iterate through every scalar element of the 2d array skipping 1 element

# In[49]:


array8 = np.array([[1,2,3,4],[5,6,7,8,]])

for x in np.nditer(array8[0:, ::2]):
    print(x)


# In[50]:


array8 = np.array([[1,2,3,4],[5,6,7,8,]])

for x in np.nditer(array8[:, ::1]):
    print(x)


# In[51]:


array8 = np.array([[1,2,3,4],[5,6,7,8,]])

for x in np.nditer(array8[0:1, ::2]):
    print(x)


# In[56]:


array8 = np.array([[1,2,3,4],[5,6,7,8,]])

for x in np.nditer(array8[0:2, ::3]):
    print(x)


# # Enumerated Iteration Using ndenumerate()
# Enumeration means mentioning sequence number of somethings one by one.
# 
# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

# Q9 enumerate on following 1D arrays elements:

# In[54]:


array9 = np.array([1,2,3])
for idx, x in np.ndenumerate(array9):
    print(idx, x)


# in the above eg, we can see that idx is telling the index no. of array and np.ndenumerate is helping to identify. ndenumerator is specically for index iterator.

# Q10 Enumerate on following 2D array's elements:

# In[57]:


array10 = np.array([[1,2,3],[4,5,6]])

for idx, x in np.ndenumerate(array10):
    print(idx, x)


# here we can see as the array is 2d, we can see the index iterator that is idx helping us to know which row and column index that particular array holds. 
