""" 
@file: clean_word.py
@Time: 2018/10/14
@Author:heningqiu
"""
import pandas as pd
import jieba

# 分词
def part_word(inputfile,outputfile):
    data1=pd.read_csv(inputfile, encoding = 'utf-8', header = None) #读入数据
    mycut = lambda s: ' '.join(jieba.cut(s))  # 自定义简单分词函数
    data1 = data1.iloc[:,0].apply(mycut)  # 通过“广播”形式分词，加快速度。
    data1.to_csv(outputfile,index = False, header = False, encoding = 'utf-8') #保存结果

# 去停用词
def stop_word(intputfile,stoplist,outputfile2):
    # sep设置分割词，由于csv默认以半角逗号为分割词，而该词恰好在停用词表中，因此会导致读取出错
    # 所以解决办法是手动设置一个不存在的分割词，如tipdm。
    stop=pd.read_csv(stoplist,encoding= 'utf-8', header = None, sep = 'tipdm')
    data1=pd.read_csv(intputfile, encoding = 'utf-8', header = None) #读入数据
    stop = [' ', ''] + list(stop.iloc[:,0])  # Pandas自动过滤了空格符，这里手动添加
    '''先以分词后的符号来分割，再遍历判断是否在停用词里，是的话去除'''
    data1.iloc[:,0] = data1.iloc[:,0].apply(lambda s: s.split(' '))  # 定义一个分割函数，然后用apply广播
    data1.iloc[:,0] = data1.iloc[:,0].apply(lambda x: [i for i in x if i not in stop])  # 逐词判断是否停用词，思路同上

    data1.to_csv(outputfile2,index = False, header = False, encoding = 'utf-8') #保存结果

if __name__ == '__main__':
    inputfile = '../otherfiles/meidi_jd_pos.txt'  # 未分词
    outputfile1 = '../otherfiles/meidi_myPosRes_clean1.txt'  # 分词
    outputfile2 = '../otherfiles/meidi_myPosRes_clean2.txt'  # 去除停用词
    stoplist = '../otherfiles/stoplist.txt'

    part_word(inputfile,outputfile1)
    stop_word(outputfile1,stoplist,outputfile2)
