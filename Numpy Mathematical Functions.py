#!/usr/bin/env python
# coding: utf-8

# # Mathematical function

# # Q1.SIN() - This function helps user to calculate trigonometric sine for all x(being the array elements)

# In[16]:


# sin() function
 
import numpy as np

 
array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", array)
 
Sin_Values = np.sin(array)
print ("\nSine values : \n", Sin_Values)


# we can use np also as well as math also to use pi functions.
# here pi value is defined in the package as 3.14159

# In[14]:


import numpy as np
import math
 
array = [0, math.pi / 2, math.pi / 3, math.pi]
print ("Input array : \n", array)
 
Sin_Values = np.sin(array)
print ("\nSine values : \n", Sin_Values)


# # Q2. COS() - This mathematical function helps user to calculate trignmetric cosine for all x(being the array elements).

# In[25]:


# Python program explaining
# cos() function
 
import numpy as np
import math
 
array = [0, np.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", array)
 
cos_Values = np.cos(array)
print ("\nCosine values : \n", cos_Values)


# # Q3. TAN() - This mathematical function helps user to calculate trigonometric tangent for all x(being the array elements). 

# 2pi Radians = 360 degrees
# 
# tan(x) = sin(x) / cos(x)
# 
# An array with trigonometric sine
# of x for all x i.e. array elements 

# In[26]:


import numpy as np
import math
 
in_array = [0, math.pi / 4, 3*np.pi / 2, math.pi/6]
print ("Input array : \n", in_array)
 
tan_Values = np.tan(in_array)
print ("\nTan values : \n", tan_Values)


# # Q4. conversion from Radian to degrees

# In[27]:


# rad2deg() function
  
import numpy as np
import math
  
array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Radian values : \n", array)
  
conversion = np.rad2deg(array)
print ("\nDegree values : \n", conversion)


# In[28]:


#2nd method to get radians converted to degrees
# degrees() function
import numpy as np
import math
  
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Radian values : \n", in_array)
  
degree_Values = np.degrees(in_array)
print ("\nDegree values : \n", degree_Values)


# # Q5. conversion from Degrees to Radian 

# In[29]:


# degrees() function
  
import numpy as np
import math
  
in_array = np.arange(10.) * 90
print ("Degree values : \n", in_array)
  
radian_Values = np.radians(in_array)
print ("\nRadian values : \n", radian_Values)


# In[30]:


#method2

# degrees() function
  
import numpy as np
import math
  
in_array = np.arange(10.) * 90
print ("Degree values : \n", in_array)
  
radian_Values = np.radians(in_array)
print ("\nRadian values : \n", radian_Values)


# # Q6. Hyperbolic Functions 
# This mathematical function helps user to calculate hypotenuse for the right angled triangle, given its side and perpendicular.

# In[31]:


# hypot() function
  
import numpy as np
  
leg1 = [12, 3, 4, 6]
print ("leg1 array : ", leg1)
  
  
leg2 = [5, 4, 3, 8]
print ("leg2 array : ", leg2)
  
result = np.hypot(leg1, leg2)
print("\nHypotenuse is as follows :")
print(result)

