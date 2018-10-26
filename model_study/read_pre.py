""" 
@file: read_pre.py
@Time: 2018/10/14
@Author:heningqiu
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

'''
数据标准化
'''

def standardization(A):
    m, n = np.shape(A)

    # 每列求均值
    mean = np.zeros([1, n])
    for i in range(n):
        mean[-1, i] = np.mean(A[:, i])

    # 去均值
    B = A - mean

    # 每列求标准差
    B1 = B ** 2
    var = np.zeros([1, n])
    for i in range(n):
        var[-1, i] = sum(B1[:, i]) / m
    sd = np.sqrt(var)

    # 去标准差
    C = B / sd
    return C

'''
数据读取及预处理
'''

def data_pre(file, ratio=0.7, data_sd='N'):
    # 读取csv数据
    data = pd.read_csv(file, header=None)

    m, n = np.shape(data)
    x = data.values[1:, :n - 1]
    y = data.values[1:, n - 1]
    feature = data.values[0, :n - 1]

    # 数据标准化
    if data_sd == 'Y': x = standardization(x)

    # 将数据随机分为训练集与测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=ratio)

    return x_train, x_test, y_train, y_test, feature
