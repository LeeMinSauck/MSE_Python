#!/usr/bin/env python
# coding: utf-8

# In[26]:


apart = [ [101, 102], [201, 202], [301, 302] ]
#아파트안에 층이있고 층안에 집이있음 (이중루프)
for 층 in apart:
    for 집 in 층:
#집옆에 호를 붙여준다.
        print(집, "호")
#-----를 마지막에 출력해준다.
print("-" * 5)


# In[ ]:




