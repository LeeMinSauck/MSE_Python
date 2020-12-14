#!/usr/bin/env python
# coding: utf-8

# In[4]:


per = ["10.31", "", "8.00"]
#per속에 있는 것을 차례로 출력하는데
for i in per:
    try:
        print(float(i))
#예외일때는 0 아니면 clean data를 출력
    except:
        print(0)
    else:
        print("clean data")
#변환완료는 항상 출력
    finally:
        print("변환 완료")


# In[ ]:




