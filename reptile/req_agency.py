#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/7/3 15:05
@Author  : Fate
@File    : 13requests代理.py
'''

import requests

# 使用代理
# proxy = {'http': "10.3.137.91:808"}  # 无密码

proxyPasswd = {'http': "http://User1:123456@10.3.137.91:808"}
# 带密码的 requests {'协议类型':"协议类型://用户:密码:IP:端口"}

# proxies
response = requests.get(url="http://www.baidu.com", proxies=proxyPasswd)
print(response)
