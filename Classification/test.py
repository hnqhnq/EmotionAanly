""" 
@file: test.py
@Time: 2018/10/21
@Author:heningqiu
"""
import numpy as np
# print(np.ones(5))

with open("data/pos.txt", encoding="utf8") as pos_f, \
        open("data/neg.txt", encoding="utf8") as neg_f, \
        open("data/hes.txt", encoding="utf8") as hes_f:
    pos_data = pos_f.readlines()
    neg_data = neg_f.readlines()
    hes_data = hes_f.readlines()

    pos_label = np.ones(len(pos_data)).tolist()  # 正向情感：1
    neg_label = np.zeros(len(neg_data)).tolist()  # 负向情感：0
    hes_label = np.random.randint(2,3,len(hes_data)).tolist()   # 中性情感：2
    print(len(hes_label))