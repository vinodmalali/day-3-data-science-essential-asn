#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
x = np.arange(2,50,3)
print("array from 2 to 50")
print(x)

2)
# In[8]:


import numpy as np
lst1=[1,2,3,4]
print(lst1)
lst2=[5,6,7,8]
print(lst2)
print(np.array(lst1))
print(np.array(lst2))
np.concatenate([lst1,lst2])

3)
# In[10]:


arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr.dtype)
print(sum(arr))


# 4)using reshape method we can convert 1D to 2D in np

# In[11]:


import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)


# In[ ]:




