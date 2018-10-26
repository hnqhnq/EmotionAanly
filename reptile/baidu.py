""" 
@file: baidu.py
@Time: 2018/10/14
@Author:heningqiu
"""
import urllib.request
import urllib.parse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

def baiduAPI(wd):
    '''
    百度接口
    :return:response
    '''
    wd = {"wd": wd}
    wd = urllib.parse.urlencode(wd)  # 字典 ,编码
    kw = urllib.parse.unquote(wd)
    print(kw)
    url = 'https://www.baidu.com/s?' + wd
    print(url)

    request = urllib.request.Request(url, headers=headers)
    respose = urllib.request.urlopen(request)

    return respose.read().decode('utf-8')

if __name__ == '__main__':
    kw = input("请输入搜索关键字：")
    response = baiduAPI(kw)
    print(response)