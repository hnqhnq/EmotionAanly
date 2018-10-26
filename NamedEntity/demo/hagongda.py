# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 11:38
# @File    : hagongda.py
# @Author  : hnq
# -*- coding: utf-8 -*-

import codecs
from pyltp import SentenceSplitter #分句
from pyltp import Segmentor #分词
from pyltp import Postagger #词性标注
from pyltp import NamedEntityRecognizer #词性标注

from pyltp import SementicRoleLabeller #角色标注
from pyltp import Parser #句法分析


# 读取待处理文本
'''
    读取的文本格式是encoding参数值，codecs函数将其转化为unicode格式。
'''
news_files = codecs.open('news_content.txt', 'r', encoding='utf8')
news_list = news_files.readlines()
# type(news_list[1].encode('utf-8'))
# print(news_list)#['首节开局双方开场你来我往。深圳队在利用贾里德-萨林……']

# 分句
'''
此函数参数输入的格式必须为str格式，所以直接获取的list里的参数值需要
通过encode('utf-8')，从Unicode转换为str
'''
def sentence_splitter(sentence):
    sents = SentenceSplitter.split(sentence)
    print( '\n'.join(sents))
    sents_list = list(sents)
    return sents_list
# print(sentence_splitter('今天是个好日子。天气真好！没想到？哈哈，就专业。')) # ['今天是个好日子。', '天气真好！', '没想到？', '哈哈，就专业。']
# print(sentence_splitter(news_list[0]))

# 分词
def segmentor(sentence):
    segmentor = Segmentor() # 初始化实例
    segmentor.load(r'D:\Corpus\ltp_data_v3.4.0\cws.model')  # 加载模型
    words = segmentor.segment(sentence)  # 分词
    # 默认可以这样输出
    # print('\t'.join(words))
    # 可以转化成List输出
    word_list = list(words)
    segmentor.release()  # 释放模型
    return word_list
# print(segmentor(news_list[0]))#['首', '节', '开局', '双方', '开场', '你来我往', '。', '深圳',……]

# 词性标注
def posttagger(words):
    postagger = Postagger()
    postagger.load(r'D:\Corpus\ltp_data_v3.4.0\pos.model')
    posttags = postagger.postag(words)  # 词性标注
    postags = list(posttags)
    postagger.release()  # 释放模型
    # print type(postags)
    return postags
# print(posttagger(['今天','是','好','天气','真','漂亮'])) #['nt', 'v', 'a', 'n', 'd', 'a']
# s=segmentor(news_list[0])
# print(posttagger(s)) #['m', 'q', 'n', 'n', 'v', 'i'……]

# 命名实体识别 主要：人名，地名，机构名
def ner(words, postags):
    print('命名实体开始！')
    recognizer = NamedEntityRecognizer()
    recognizer.load(r'D:\Corpus\ltp_data_v3.4.0\ner.model')  # 加载模型
    netags = recognizer.recognize(words, postags)  # 命名实体识别
    for word, ntag in zip(words, netags):
        print(word + '/' + ntag)
    recognizer.release()  # 释放模型
    nerttags = list(netags)
    return nerttags
# words=['今天','是','好','天气','何宁秋','和','杨美丽','出门','逛街','超市','最后','南宁']
# postags=posttagger(['今天','是','好','天气','何宁秋','和','杨美丽','出门','逛街','超市','最后','南宁'])
# print(ner(words,postags))#['O', 'O', 'O', 'O', 'S-Nh', 'O', 'S-Nh', 'O', 'O', 'O', 'O', 'S-Ns']

# 新建一个txt文件保存命名实体识别的结果
# out_file = codecs.open('out_nerfile.txt', 'w', encoding='utf8') # 打开新文件
# sents = sentence_splitter(news_list[0].encode('utf-8')) # 分句 形如 ['今天真好！','是个不错的样子。']
# for sent in sents:
#     words = segmentor(sent) # 分词 形如 ['今天','真好']
#     tags = posttagger(words) # 词性标注 形如 ['m', 'q', 'n', 'n', 'v', 'i'……]
#     nertags = ner(words, tags) # 命名识别 形如 ['O', 'S-Nh', 'O', 'S-Nh', 'O', 'O', 'O', 'O', 'S-Ns']
#     for word, nertag in zip(words, nertags):
#         # out_file.write(word.decode('utf-8') + '/' + nertag.decode('utf-8') + ' ') #word没有deconde
#         out_file.write(word + '/' + nertag + ' ') # 分词+标注 形如： 在/O 利用/O 贾里德/S-Nh -/O 萨林杰/S-Nh
#
# out_file.close()


#依存句法分析
def parse(words, postags):
    parser = Parser() # 初始化实例
    parser.load(r'D:\Corpus\ltp_data_v3.4.0\parser.model')  # 加载模型
    arcs = parser.parse(words, postags)  # 句法分析
    print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
    parser.release()  # 释放模型
    return arcs #<pyltp.VectorOfParseResult object at 0x00000000035E6630>
print("*"*10)
# words = ['元芳', '你', '怎么', '看']
# postags = ['nh', 'r', 'r', 'v']
# words=['今天','是','好','天气','真漂亮']
# postags=posttagger(['今天','是','好','天气','真漂亮'])
# print(parse(words, postags))
# #2:SBV	0:HED	4:ATT	5:SBV	2:VOB
# #主谓关系 核心关系  定中关系 主谓关系 动宾关系
#-------------------------------------------------
#角色标注
# def role_label(words, postags, netags, arcs):
#     labeller = SementicRoleLabeller() # 初始化实例
#     labeller.load(r'D:\Corpus\ltp-models_full\3.3.1\ltp-data-v3.3.1\ltp_data\srl')  # 加载模型
#     roles = labeller.label(words, postags, netags, arcs)  # 语义角色标注
#     # print('看这里看这里！！！！:',roles)
#     for role in roles:
#         print(role.index, "".join(
#             ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))
#     labeller.release()  # 释放模型
#
# words=['天安门','国旗','张思思','优秀']
# postags=posttagger(['天安门','国旗','张思思','优秀'])
# netags=ner(words, postags)
# arcs=parse(words, postags)
# print("---*---"*10)
# role_label(words, postags, netags, arcs)
#-------------------------------------------------
# 没有找到对应版本的 srl 模型
labeller = SementicRoleLabeller() # 初始化实例
labeller.load(r'D:\Corpus\ltp-models_full\3.2.0\submodels\srl\srl')  # 加载模型
words = ['元芳', '你', '怎么', '看']
postags = ['nh', 'r', 'r', 'v']
# arcs 使用依存句法分析的结果
arcs=parse(words, postags)
roles = labeller.label(words, postags, arcs)  # 语义角色标注
print('roles====',roles)
# 打印结果
for role in roles:
    print(role.index, "".join(
        ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end)
         for arg in role.arguments]))
labeller.release()  # 释放模型
