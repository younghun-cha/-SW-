# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 01:09:38 2022

@author: 82102
"""

import json
import requests
import urllib.request
from urllib.request import Request, urlopen
from xml.etree import ElementTree
import pandas as pd


key = '************'  # 재발급

url = 'http://api.visitkorea.or.kr/openapi/service/rest/Durunubi/courseList?ServiceKey='+ key+ '&MobileOS=ETC&MobileApp=AppTest' 


request = Request(url)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)
root = ElementTree.fromstring(response_body)
df = pd.DataFrame()
for item in root.iter('item'):
    print(item)
    item_dict = {}
    item_dict['MobileOS'] = item.find('MobileOS').text
    df = df.append(item_dict, ignore_index = True)
    
df.to_csv(path_or_buf=r"test.csv", encoding='euc-kr')
    
print(df)

#json_array = json.load(json_data)
#print(json_array)