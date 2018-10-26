# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 10:38
# @File    : ar_merge.py
# @Author  : hnq
import pandas as pd

s1=pd.read_csv('./a_7.txt',header=None)
s2 = pd.read_csv('./r_7.txt', header=None)
data = s1.copy()
data[1]=s2
data.columns=['ask','reply']
data.to_excel('./sx_d7.xlsx',index=None)
