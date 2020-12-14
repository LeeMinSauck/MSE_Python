#!/usr/bin/env python
# coding: utf-8

# In[11]:


#비트코인 가격 정보를 딕셔녀리로 가져온다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

#시가 변동폭이 최고가보다 크면 상승장이고 아니면 하락장이다.
if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")


# In[ ]:




