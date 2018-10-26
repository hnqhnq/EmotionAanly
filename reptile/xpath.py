#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/7/5 10:06
@Author  : Fate
@File    : 02抓取51城市列表.py
'''

import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

url = "https://jobs.51job.com/"

response = requests.get(url, headers=headers).content.decode('gbk')
# print(response)

mytree = lxml.etree.HTML(response)

cityList = mytree.xpath('//div[@class="e e4"][1]//div[@class="lkst"]/a')

for city in cityList:
    cityName = city.xpath('./text()')[0]
    cityUrl = city.xpath('./@href')[0]
    print(cityName, cityUrl)
