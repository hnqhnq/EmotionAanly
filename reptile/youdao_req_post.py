#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/7/3 14:15
@Author  : Fate
@File    : 11requests的POST请求.py
'''

import requests

import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

'''
url,
data=None 表单数据，不需要url编码
'''


def youdaoAPI(kw):
    '''
    有道翻译接口
    :param kw: 要翻译的内容
    :return: 翻译结果
    '''

    # url

    # 去掉_o
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    data = {
        "i": kw,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1530598760913",
        "sign": "92691936d81b1aaf2316c682773c2012",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false",
    }

    response = requests.post(url, data=data, headers=headers)

    # print(response.text)
    result = json.loads(response.text)
    result = result['translateResult'][0][0]['tgt']
    print(result)

    # 自带json模块
    # result = response.json()
    # result = result['translateResult'][0][0]['tgt']
    # print(result)

if __name__ == '__main__':
    kw = input("请输入：")
    youdaoAPI(kw)
