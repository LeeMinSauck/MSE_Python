#!/usr/bin/env python
# coding: utf-8

# In[32]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

total_profit=0
#수익금을 계속 누적시킨다.
for day_price in ohlc[1:]:
    profit = day_price[0] - day_price[3]
    total_profit += profit

print(total_profit)


# In[ ]:




