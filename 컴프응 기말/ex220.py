#!/usr/bin/env python
# coding: utf-8

# In[36]:


def print_max(a, b, c) :
    max_val = 0
#a가 max_val보다크면 a b가 크면 b c가크면 c를출력한다.
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)


# In[ ]:




