""" 
@file: do_2.py
@Time: 2018/10/14
@Author:heningqiu
"""
import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

url = "https://wenku.baidu.com/view/f01a01c4cd22bcd126fff705cc17552706225e6a.html"

response = requests.get(url, headers=headers).content.decode('gbk')
print(response)

mytree = lxml.etree.HTML(response)

textList = mytree.xpath('//div[@class="ie-fix"]/p')
print(textList)  # respose无法获取[]

for i in textList:
    print('1')
    content=i.xpath('./text()')[0]
    print(content)
