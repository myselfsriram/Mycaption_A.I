#!/usr/bin/env python
# coding: utf-8

# In[6]:


a=int(input("Enter a number:"))
sum1=0
sum2=1
for i in range(0,a):
    print(sum1,end=" ")
    res=sum1
    sum1+=sum2
    sum2=res


# In[ ]:




