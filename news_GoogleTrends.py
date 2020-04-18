# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:17:40 2020

@author: ThinkPad
"""

import requests
import pandas as pd                        
from pytrends.request import TrendReq
pytrend = TrendReq()

pytrend.build_payload(kw_list=['Pollution', 'Sustainability'])
# Interest by Region
df = pytrend.interest_by_region()
df.head(10)



print(df.sort_values(by='Pollution', ascending=False))

#df.reset_index().plot(x='geoName', y='Pollution', figsize=(50, 10), kind ='bar')
#auxiliar= df.sort_values(by='Pollution', ascending=False)
#auxiliar.reset_index().plot(x='geoName', y='Pollution', figsize=(50, 10), kind ='bar')

#auxiliar= df.sort_values(by='Sustainability', ascending=False)
#auxiliar.reset_index().plot(x='geoName', y='Sustainability', figsize=(50, 10), kind ='bar')

#booleans = []
#for lenght in df.Pollution:

print(df[df.Pollution > 0])