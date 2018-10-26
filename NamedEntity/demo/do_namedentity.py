# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 14:29
# @File    : do_namedentity.py
# @Author  : hnq
from pyltp import NamedEntityRecognizer, Postagger

import jieba
import jieba.posseg as psg

# 加载分析文档
def load_file(path):
    with open(path,'r',encoding='utf-8')as f:
        file=f.readlines()
    sent_lst=list(map(lambda x:x.replace('\n',''),file))
    return sent_lst

# 停用词表加载方法
def get_stopword_list():
    # 停用词表存储路径，每一行为一个词，按行读取进行加载
    # 进行编码转换确保匹配准确率
    stop_word_path = './stopword.txt'
    stopword_list = [sw.replace('\n', '') for sw in open(stop_word_path ,encoding='utf-8').readlines()]

    return stopword_list

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
# print("&"*10)
# s=seg_to_list('今天是好天气真漂亮',pos=True)
# print(list(s))
#[pair('今天', 't'), pair('是', 'v'), pair('好', 'a'), pair('天气', 'n'), pair('真', 'd'), pair('漂亮', 'a')]

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
        if not flag.startswith('n'):
            continue
        # 过滤停用词表中的词，以及长度为<2的词
        if not word in stopword_list and len(word) > 1:
            filter_list.append(word)

    return filter_list

# 词性标注
def posttagger(words):
    postagger = Postagger()
    postagger.load(r'D:\Corpus\ltp_data_v3.4.0\pos.model')
    posttags = postagger.postag(words)  # 词性标注
    postags = list(posttags)
    postagger.release()  # 释放模型
    # print type(postags)
    return postags

# 命名实体识别 主要：人名，地名，机构名
def ner(words, postags):
    print('--------** 命名实体开始 **--------')
    recognizer = NamedEntityRecognizer()
    recognizer.load(r'D:\Corpus\ltp_data_v3.4.0\ner.model')  # 加载模型
    netags = recognizer.recognize(words, postags)  # 命名实体识别
    name_dic={}
    for word, ntag in zip(words, netags):
        # print(word + '/' + ntag)
        # 筛选出不含‘O'的 人名、地名、机构名
        if ntag!='O':
            # print(word + '/' + ntag)
            name_dic[word]=ntag
    recognizer.release()  # 释放模型
    # nerttags = list(netags) # ['O', 'O', 'O', 'B-Nh', 'I-Nh', 'I-Nh', 'I-Nh',……]
    return name_dic

if __name__ == '__main__':
    # print(load_file(path='sx_5.txt'))
    pos=False
    text='友联的决策机构是执委会，老执委有张业光、王宏、唐万川、李强(2002年我叫他负责收购南京国投和南昌商行的工作，' \
         '空了一年左右)、赵戈飞和我六人，后来又增加了王海秦、李向春、孔清华和黄平等人，' \
         '具体以友联文件为准。战略管理部的职责是制定每个金融机构的年度计划、未来三年战略、实施SAP系统，' \
         '先由赵戈飞分管，后来由李强分管，由潘维强负责;' \
         '客户部的职责是进行客户需求分析、客户服务过程监控、研究分析目标客户和发展培训客户经理，' \
         '由张业光分管，由陈纪负责;产品部的职责是负责所有金融产品的开发、实施对客户的服务，' \
         '由王宏分管，由王世瑜(注：应为“渝”)负责;' \
         '证券投资与研究部的职责是进行证券研究(曹融负责)、证券投资(董公元负责)和行业研究(王建军负责)，' \
         '这个部门与中企东方是一套班子，两块牌子，由唐万川分管。唐万川同时兼任中企东方的法人代表、总经理。' \
         '财务部是由唐万川和赵戈飞分管，我管全面工作，主要职责就是救火，其他两个部门即风险管理部和产业投资监管部没有运转起来。'
    seg_list = seg_to_list(text, pos)  # 分词
    # print(' '.join(seg_list))
    words = word_filter(seg_list, pos)  # 过滤停用词
    # print(words)
    postags = posttagger(words)  # 词性标注
    ners=ner(words, postags) # 命名实体
    print(ners.keys())
#---------------------------------------------------
    # sent_lst=load_file(path='sx_5.txt') # 读入数据
    # for sentence in sent_lst:   # 遍历每一句
    #     seg_list=seg_to_list(sentence, pos)  # 分词
    #     # print(' '.join(seg_list))
    #     words=word_filter(seg_list, pos) # 过滤停用词
    #     print(words)
    #     # postags=posttagger(words) # 词性标注
    #     # print(ner(words, postags)) # 命名实体


    pass
