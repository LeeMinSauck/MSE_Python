#!/usr/bin/env python
# coding: utf-8

# In[27]:


#message1은 A를 프린트하는 함수
def message1():
    print("A")

#message2는 B를 프린트하는 함수
def message2():
    print("B")
#message3은 3번간 message3을 호출하고 C를 출력한다음 message1을 호출한다
def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()


# In[ ]:




