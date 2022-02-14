#!/usr/bin/env python
# coding: utf-8

# # Slice elements from index 1 to index 5 from the following array:

# In[1]:


import numpy as np

array1 = np.array([1,2,3,4,5,6,7])

print(array1[1:5])


# # Slice elements from index 4 to the end of the array:

# In[2]:


array1 = np.array([1,2,3,4,5,6,7])

print(array1[4:])


# # Slice elements from the beginning to index 4 (not included):

# In[7]:


array1 = np.array([1,2,3,4,5,6,7])

print(array1[:4])


# # Slice from the index 3 from the end to index 1 from the end:

# In[8]:


array1 = np.array([1,2,3,4,5,6,7])
print(array1[-3:-1])


# # Return every other(alternate) element from index 1 to index 5:

# In[14]:


array1 = np.array([1,2,3,4,5,6,7])

print(array1[1:5:2])


# step value above is adding the condition, like we had to print numbers from index no. 2 to 5 but ek condition hai ki every other number means alternate, so output should come 2,4. so for that we did [1:5:2] yaha 2 used kiya because need every other number

# # Return every other element from the entire array:

# In[20]:


array1 = np.array([1,2,3,4,5,6,7])

print(array1[::2])


# # 2-d array-From the second element, slice elements from index 1 to index 4 (not included):

# In[21]:


array1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(array1[1, 1:4])


# in the above example, we have been told from the 2nd element which means the 2nd array jiski indexing ha 1(0,1), now in the 2nd element slice elements from index 1 to 4

# # From both elements, return index 2:

# In[33]:


array1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(array1[0:2, 3])


# In the above example as we are having 2-d array and we need to return index 2 from both so pehle arrays likhenge(0:2) now 0:2 means array at 0th position which is [1,2,3,4,5] and array at 2th means 1st position pe(because 2 se pehle vala no. lete ha na)1st which is [6,7,8,9,10] and then comma daalkar jaha se indexing chahiye dono mein voh add krdo.

# # From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:

# In[34]:


array1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(array1[0:2, ])

