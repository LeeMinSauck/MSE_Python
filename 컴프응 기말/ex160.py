#!/usr/bin/env python
# coding: utf-8

# In[15]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
#.을 기준으로 분리했을때 뒤에 h나c가오면 출력해라
for 변수 in 리스트:
  split = 변수.split(".")
  if (split[1] == "h") or (split[1] == "c"):
    print(변수)


# In[ ]:




