#!/usr/bin/env python
# coding: utf-8

# # Q1. Write a Python program to multiply two matrices using numpy

# In[1]:


import numpy as np
 
# input two matrices 
mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3]) 
mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7]) 

# This will return dot product 
res = np.dot(mat1,mat2) 
print(res) 


# # Q2. Write a Python program to get the floor, ceiling and truncated values of the elements of an numpy array.

# In[5]:


import numpy as np

x = np.array([-1.6, -1.5, -0.3, 0.1, 1.4, 1.8, 2.0])
print("orignal array: ",x)

#floor value
print("Floor values of the above array elements: ", np.floor(x))

#ceiling value
print("ceiling values of the array is: ", np.ceil(x))

#truncate
print("Truncated values of the array elements: ", np.trunc(x))


# # Q3. Write a python program to find the inverse of a matrix

# In[7]:


import numpy as np
array1 = np.array([[2,3],[4,5]])
try:
    inverse = np.linalg.inv(array1)
    print(inverse)
except np.linalg.LinalgError:
    #not invertible. skip this one.
    pass


# In[8]:


import numpy as np
array1 = np.array([[2,3],[4,5]])
inverse = np.linalg.inv(array1)
print(inverse)


# # Q4. Write a Python program to perform addition, subtraction, multiplication and divsion on the given polynomials

# In[9]:


from numpy.polynomial import polynomial as P
x = (10,20,30)
y = (30,40,50)
print("Addition:")
print(P.polyadd(x,y))
print("Subtraction:")
print(P.polysub(x,y))
print("Multiplication:")
print(P.polymul(x,y))
print("Division:")
print(P.polydiv(x,y))


# # Q5. Write a Python program to create a random array with N elements and compute the average, variance, standard deviation of the array elements

# In[75]:


import numpy as np
n=int(input("Enter a number: "))
K = np.random.randn(n)

print("Average of the array elements:")
mean = K.mean()

print("\t",mean)

print("Standard deviation of the array elements:")
std = K.std()
print("\t",std)

print("Variance of the array elements:")
var = K.var()
print("\t",var)


# # Q6. Write a Python program to compute the reciprocal for all elements in a given array.

# In[78]:


import numpy as np

J = np.array([1.,2.,0.4,.3])
print(J)

r1 = np.reciprocal(J)
print(r1)


# # Q7. Write a Python program to sort the specified number of elements from beginning of a given array

# In[82]:


import numpy as np
nums = np.random.rand(10)
print(nums)

print("\nSorted first N elements:")

print(nums[np.argpartition(nums,range(n))])


# # Q8. write a python program to generate N random numbers from the normal distribution

# In[1]:


import numpy as np
n = int(input("enter number: "))
x = np.random.normal(size=n)
print(x)


# # Q9. Write a Python program to create random vector of size N and replace the maximum value by N

# In[8]:


import numpy as np
n=int(input("Enter value of N: "))
x = np.random.random(n)
print("Original array:")
print(x)
x[x.argmax()] = n
print("Maximum value replaced by -1:")
print(x)


# # Q10. Write a Python program to find the most frequent value in an array

# In[15]:


import numpy as np
x = np.random.randint(0, 10, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())


# # Q11. Write a Python program to convert cartesian coordinates to polar coordinates of a random MxN matrix representing cartesian coordinates

# In[22]:


import numpy as np
m=int(input("Enter no. of rows: "))
n=int(input("Enter no. of columns: "))
z= np.random.random((m,n))
x,y = z[:,0], z[:,1]
r = np.sqrt(x**2+y**2)
t = np.arctan2(y,x)
print("Cartesian Product: \n",r)
print("Polar Product: \n",t)


# # Q12.Write a NumPy program to create a 3x3x3 array with random values

# In[17]:


import numpy as np
x = np.random.random((3,3,3))
print(x)


# # Q13. Write a Python program to find point by point distances of a random vector with shape (J,K) representing coordinates

# In[ ]:


import numpy as np
j=int(input("Enter J: "))
k=int(input("Enter K: "))
a= np.random.random((j,k))
x,y = np.atleast_2d(a[:,0], a[:,1])
d = np.sqrt( (x-x.T)**2 + (y-y.T)**2)
print(d)


# # Q14. Write a NumPy program to check if each element of a given array is composed of digits only, lower case letters only and upper case letters only.

# In[18]:


import numpy as np
x = np.array(['Python', 'PHP', 'JS', 'Examples', 'html5', '5'], dtype=np.str)
print("\nOriginal Array:")
print(x,"\n")
r1 = np.char.isdigit(x)
r2 = np.char.islower(x)
r3 = np.char.isupper(x)
print("Digits only =", r1)
print("Lower cases only =", r2)
print("Upper cases only =", r3)


# # Q15. Write a Python program to Triangulate a location based on co-ordinates.

# In[19]:


import numpy as np
data = [20.0497520, 31.39864012947, 12.30974023]
print(np.mean(data, axis=0))


# # Q16. Write a Python code to determine the rank of the matrix

# In[20]:


import numpy
A = numpy.matrix([[1,3,7],[2,8,3],[7,8,1]])
numpy.linalg.matrix_rank(A)


# # Q17. Write a NumPy program to multiply a MxN matrix by a NxA matrix and create a real matrix product

# In[21]:


import numpy as np
m=int(input("Enter value M: "))
n=int(input("Enter value N: "))
a=int(input("Enter value A: "))
x = np.random.random((m,n))
print("First array:")
print(x)
y = np.random.random((n,a))
print("Second array:")
print(y)
z = np.dot(x, y)
print("Dot product of two arrays:")
print(z)

