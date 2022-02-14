#!/usr/bin/env python
# coding: utf-8

# # Get the first element from the following array:

# In[3]:


import numpy as np
arraygg = np.array([1,2,3,9])
print(arraygg[0])


# # Get the second element from the following array.

# In[4]:


arraygg = np.array([6,8,2,3,4])
print(arraygg[3])


# # Get third and fourth elements from the following array and add them.

# In[8]:


arraygg = np.array([6,8,2,1,9])
print(arraygg[3], arraygg[4])
print(arraygg[3] + arraygg[4])


# # Access the element on the first row, second column:2 D arrays

# In[10]:


arraygg = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arraygg[0, 1])


# # Access the element on the 2nd row, 5th column:

# In[11]:


arraygg = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('element of 2nd row, 5th column is:', arraygg[1,4])


# In the above code arraygg[1,4] means 2nd row which is 1st in array (0,1) and 5th column [0,1,2,3,4] 

# # Access the third element of the second array of the first array:

# In[15]:


import numpy as np
arraygg = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arraygg[0,1,2])


# In[ ]:


The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6


# # Use negative indexing to access an array from the end.
# Print the last element from the 2nd dim:

# In[17]:


arraygg = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print('Last element from 2nd dim is:', arraygg[1,-1])

