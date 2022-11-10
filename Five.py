#!/usr/bin/env python
# coding: utf-8

# In[3]:


set1={1,2,3,4,5}
set2={6,7,8,9,10}
res=set1.union(set2)
print(res)


# In[4]:


res1=set1.intersection(res)
print(res1)


# In[10]:


res2=set2.difference(set1)
print(res2)


# In[11]:


res3=set2.symmetric_difference(set1)
print(res3)


# In[ ]:




