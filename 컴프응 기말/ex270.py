#!/usr/bin/env python
# coding: utf-8

# In[ ]:


종목 = []

#stock클래스에 객체를 넣어줌
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

#종목리스트안에 객체를 출력한다.
for i in 종목:
    print(i.code, i.per)

