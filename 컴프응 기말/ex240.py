#!/usr/bin/env python
# coding: utf-8

# In[39]:


#함수0은 *2로 정의한다.
def 함수0(num) :
    return num * 2

#함수1은 함수0 +2로 정의한다.
def 함수1(num) :
    return 함수0(num + 2)

#함수2는 10을 더하고 함수1로 보낸다.
def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)


# In[ ]:




