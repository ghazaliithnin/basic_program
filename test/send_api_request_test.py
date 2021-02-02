# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:41:11 2020

@author: user
"""


import requests

payload = {"firstName":"John","lastName":"Smith"}

url = "https://httpbin.org/post"

r = requests.post(url, data = payload)

print(r.text)