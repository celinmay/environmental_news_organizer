# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 09:41:17 2020

@author: ThinkPad
"""


from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key=' cda842aac04d431fa6ee04093ba62f1d')

import requests
import json



all_articles = newsapi.get_everything(q='sustainability OR environment',
                                      from_param='2020-17-04',
                                      to='2020-18-04',
                                      language='de',
                                      sort_by='relevancy',
                                      page=2)

print(all_articles)