""" 
@file: do_1.py
@Time: 2018/10/14
@Author:heningqiu
"""
import urllib.request
import urllib.parse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

starUrl = "https://wenku.baidu.com/view/f01a01c4cd22bcd126fff705cc17552706225e6a.html"
req=urllib.request.Request(starUrl,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode('gbk'))

# print(response.info())
