# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 15:29
# @File    : cut_word.py
# @Author  : hnq
import jieba

# str1='''
# 在我们处理爬虫的时候，有许多文本信息，如电影简介、新闻报道以及评论等，而关键词提取是指从大量文本中提出最核心、最主要的关键词，而实现关键词提取算法的算法有两种：1. TextRank: 基于词与词直接的上下文关系构建共现网络，将处于网络核心位置的词作为关键词、2. TF-IDF:选出一般不常用但是在指定环境文本中频繁出现的词作为关键词。
# 信息的抽取是从非结构化文本中抽取出有意义或者感兴趣的字段。例如对于一篇新闻报告，从里面提取出标题，事件，时间，主人公等字段，从而将非结构化文本转化为结构化数据，便于信息管理和数据分析。
# '''
str1='''
根据《中华人民共和国刑事诉讼法》的规定，你在被讯问期间有相应的权利和义务
（递上讯问期间权利义务告知单），看一下。如果你无法阅读，我们可以向你宣读，是否清楚了？
'''

jieba.load_userdict('newdict.txt')
# jieba.add_word('字段')
# jieba.add_word('非结构化')
# jieba.add_word('TF-IDF')
stoplist = '../otherfiles/stoplist.txt'
s1=' '.join(jieba.cut(str1))
# print(s1)
with open(stoplist,'r',encoding='utf-8')as f:
    stp=f.readlines()
# print(stp)
cl_stp=list(map(lambda x : x.replace('\n',''),stp))
cl_stp=cl_stp+['\n']

# print(cl_stp)
s2=s1.split(' ')
s3=[i for i in s2 if i not in cl_stp]
print(s3)

