#!/usr/bin/env python
# coding: utf-8

# In[3]:


#부모 클래스의 생성자를 생성하고 부모생성으로한다.
class 부모:
    def __init__(self):
        print("부모생성")

#자식 클래스는 부모클래스를 상속받는다.
class 자식(부모):
    def __init__(self):
        print("자식생성")
#자식 클래스가 생성될때 부모클래스에 접근하여 생성자를 명시적으로 호출
        super().__init__()

나 = 자식()


# In[ ]:




