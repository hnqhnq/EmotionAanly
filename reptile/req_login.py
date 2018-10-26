#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/7/3 14:30
@Author  : Fate
@File    : 12request登陆.py
'''

import requests

# 用session保存cookie
session = requests.session()

'''
url, data
'''

loginurl = "http://www.renren.com/PLogin.do"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

# 表单数据
data = {
    "email": "18588403840",
    "password": "Changeme_123"
}

# 模拟登陆，post提交表单数据
response = session.post(url=loginurl, data=data, headers=headers)
print(response.text)

print('登陆后' * 30)

# 通过session访问
myIndex = session.get("http://www.renren.com/965557295/profile")
print(myIndex.text)

print('=================' * 30)
print(session.cookies)  # CookieJar对象
# 将cookie对象转为字典
cookieDict = requests.utils.dict_from_cookiejar(session.cookies)
# 保存cookie
with open("session.txt", 'w', encoding='utf-8') as f:
    f.write(str(cookieDict))
    f.flush()

