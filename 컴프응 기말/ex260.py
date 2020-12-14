#!/usr/bin/env python
# coding: utf-8

# In[3]:


class OMG : 
    def print() :
        print("Oh my god")
        
mystock = OMG()
mystock.print()
#mystock 안에는 print가 없고 따라서 클래스로 가게되어 위에있는 Oh my god이 프린트
#되어야하지만 self가없기에 에러가난다.


# In[4]:


class OMG : 
    def print(self) :
        print("Oh my god")
        
mystock = OMG()
mystock.print()


# In[ ]:




