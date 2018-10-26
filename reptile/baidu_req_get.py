#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/7/3 14:08
@Author  : Fate
@File    : 10request带参的GET请求.py
'''

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}


# https://www.baidu.com/s?wd=requests保存

def baiduAPI(wd):
    '''
    百度接口
    :param wd: 搜索关键字
    :return: response
    '''
    url = "https://www.baidu.com/s"
    # 搜索，自动拼接还url编码
    data = {"wd": wd}
    response = requests.get(url, params=data)
    print(response.url)


if __name__ == '__main__':
    wd = input("请输入：")
    baiduAPI(wd)
