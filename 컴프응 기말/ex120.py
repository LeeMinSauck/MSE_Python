#!/usr/bin/env python
# coding: utf-8

# In[9]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을": "사과"}
user = input("좋아하는 과일은?")
#과일이 밸류안에 있으면
if user in fruit.values():
    print("정답입니다.")
else :
    print("오답입니다.")


# In[ ]:




