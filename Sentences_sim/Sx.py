""" 
@file: Sx.py
@Time: 2018/10/21
@Author:heningqiu
"""
import pandas as pd
import numpy as np
import jieba

# 加载自定义词典
jieba.load_userdict('./mydict.txt')
# 读取 审讯 数据（dia[0]:问 dia[1]:答）
dia=pd.read_excel('./test.xlsx')
# print(dia)

# 分词处理
dia[2]=dia[0].map(lambda x:' '.join(jieba.cut(x))) # sak
dia[3]=dia[1].map(lambda x:' '.join(jieba.cut(x))) # reply
# print(dia[2])

from Sentences_sim.sim import *

for i in range(len(dia[2])):
    for j in range(len(dia[2])-1):
        print(jaccard_similarity(dia[2][i],dia[2][j]))
    print('\n'+'----------')


# params = [dia[2][0],dia[2][4]]
# print(jaccard_similarity(*params))
# print(cosine_similarity_tf(*params))
# print(cosine_similarity_tfidf(*params))



