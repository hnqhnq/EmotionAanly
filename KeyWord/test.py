# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 16:12
# @File    : test.py
# @Author  : hnq

import jieba
import jieba.posseg as psg
from gensim import corpora, models
from jieba import analyse
import functools

# 停用词表加载方法
def get_stopword_list():
    # 停用词表存储路径，每一行为一个词，按行读取进行加载
    # 进行编码转换确保匹配准确率
    stop_word_path = './stopword.txt'
    stopword_list = [sw.replace('\n', '') for sw in open(stop_word_path ,encoding='utf-8').readlines()]

    return stopword_list
# print(get_stopword_list()) #['———', '》），', '）÷……]

# 分词方法，调用结巴接口
def seg_to_list(sentence, pos=False):
    if not pos:
        # 不进行词性标注的分词方法
        seg_list = jieba.cut(sentence)
    else:
        # 进行词性标注的分词方法
        seg_list = psg.cut(sentence)
        # print('seg_list--',seg_list)
    return seg_list
#-------------------------------------------------------------------------------------
# pos=True
# print(' '.join(seg_to_list('我是中华人民共和国的未来之星',pos=False))) # 我 是 中华人民共和国 的 未来 之星
# print(list(seg_to_list('我是中华人民共和国的未来之星',pos=True))) #[pair('我', 'r'), pair('是', 'v'), pair('中华人民共和国', 'ns'), pair('的', 'uj'), pair('未来', 't'), pair('之', 'u'), pair('星', 'n')]
#-------------------------------------------------------------------------------------

# 去除干扰词
def word_filter(seg_list, pos=False):
    stopword_list = get_stopword_list()
    filter_list = []
    # 根据POS参数选择是否词性过滤
    ## 不进行词性过滤，则将词性都标记为n，表示全部保留
    for seg in seg_list:
        if not pos:
            word = seg
            flag = 'n'
        else:
            word = seg.word
            flag = seg.flag
        if not flag.startswith('n'): # 只有词性为n开头的通过，进入下一环节停用词处理，不是n开头词性则跳过
            continue
        # 过滤停用词表中的词，以及长度为<2的词
        if not word in stopword_list and len(word) > 1:
            filter_list.append(word)

    return filter_list
#-------------------------------------------------------------------------------------
# text='我是中华人民共和国的未来之星，为人民服务，以国家昌盛为宗旨！'
# seg_list=seg_to_list(text,pos=True)
# # print(list(seg_list))
# '''
# [pair('我', 'r'), pair('是', 'v'), pair('中华人民共和国', 'ns'), pair('的', 'uj'), pair('未来', 't'),
# pair('之', 'u'), pair('星', 'n'), pair('，', 'x'), pair('为', 'p'), pair('人民', 'n'), pair('服务', 'vn'),
# pair('，', 'x'), pair('以', 'p'), pair('国家', 'n'), pair('昌盛', 'nz'), pair('为', 'p'), pair('宗旨', 'n'), pair('！', 'x')]
# '''
# word_filter=word_filter(seg_list,pos=True)
# print(word_filter) #['中华人民共和国', '人民', '国家', '昌盛', '宗旨'] #n开头的词性保存了下来，去除了停用词
#-------------------------------------------------------------------------------------
# seg_list=seg_to_list(text,pos=False)
# # print(' '.join(seg_list)) #我 是 中华人民共和国 的 未来 之星 ， 为 人民 服务 ， 以 国家 昌盛 为 宗旨 ！
# word_filter=word_filter(seg_list,pos=False)
# print(word_filter) #['中华人民共和国', '未来', '之星', '人民', '服务', '国家', '昌盛', '宗旨'] # 仅仅去除停用词
#-------------------------------------------------------------------------------------

# 数据加载，pos为是否词性标注的参数，corpus_path为数据集路径
def load_data(pos=False, corpus_path='./corpus.txt'):
    # 调用上面方式对数据集进行处理，处理后的每条数据仅保留非干扰词
    doc_list = []
    for line in open(corpus_path, 'r',encoding='utf-8'):
        content = line.strip() # 去掉多余的空格
        seg_list = seg_to_list(content, pos)
        filter_list = word_filter(seg_list, pos)
        doc_list.append(filter_list)
    return doc_list
# print(load_data())


#--------------------------------------------------
import math
# idf值统计方法
def train_idf(doc_list):
    idf_dic = {}
    # 总文档数
    tt_count = len(doc_list)

    # 每个词出现的文档数
    for doc in doc_list:
        for word in set(doc):
            idf_dic[word] = idf_dic.get(word, 0.0) + 1.0
    # print('idf-dic---1--',idf_dic) #idf-dic---1-- {'今天': 2.0, '好天': 1.0, '明天': 1.0}
    # 按公式转换为idf值，分母加1进行平滑处理
    for k, v in idf_dic.items():
        idf_dic[k] = math.log(tt_count / (1.0 + v))
    # print('idf-dic---2--',idf_dic) #idf-dic---2-- {'今天': 0.0, '好天': 0.4054651081081644, '明天': 0.4054651081081644}
    # 对于没有在字典中的词，默认其仅在一个文档出现，得到默认idf值
    default_idf = math.log(tt_count / (1.0))
    return idf_dic, default_idf
#-------------------------------------------
# doc_list=[['今天','好天'],['明天'],['今天']]
# print(len(doc_list)) # 3
# a,b=train_idf(doc_list)
# print(a) # idf_dic={'好天': 0.4054651081081644, '今天': 0.0, '明天': 0.4054651081081644} 经过idf转换（文档中频率越高，分值越低）
# print("*"*10)
# print(b) # default_idf=math.log(tt_count / (1.0))=1.0986122886681098
# print("*"*10)
#-------------------------------------------



