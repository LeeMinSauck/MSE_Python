#!/usr/bin/env python
# coding: utf-8

# In[23]:


low_prices  = [100, 200, 400, 800, 1000] #저가
high_prices = [150, 300, 430, 880, 1000] #고가

#비어있는 리스트 생성
volatility = []
#데이터를 비어있는 리스트에 저장
for i in range(len(low_prices)) :
    diff = high_prices[i] - low_prices[i]
    volatility.append(diff)

print(volatility)


# In[ ]:




