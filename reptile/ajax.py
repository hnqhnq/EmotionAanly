""" 
@file: ajax.py
@Time: 2018/10/14
@Author:heningqiu
"""
#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/7/2 14:01
@Author  : Fate
@File    : 04抓取ajax数据.py
'''

import urllib.request

import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

# ajax请求url

for i in range(100):
    url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=%d" % (i * 20)

    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req).read().decode('utf-8')
    # print(response)

    # json数据
    data = json.loads(response)

    for i in data['data']:
        # 明星
        casts = i['casts']
        # 导演
        directors = i['directors']

        print(casts, directors)
        # 写入文件
        with open('movie.txt', 'a+', encoding='utf-8', errors='ignore') as f:
            f.write(str((casts, directors)) + '\n')
            f.flush()
