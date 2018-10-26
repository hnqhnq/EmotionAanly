""" 
@file: main.py
@Time: 2018/10/14
@Author:heningqiu
"""
from participle_2.clean_word import part_word,stop_word
from algorithms.LDA import lda_ana

if __name__ == '__main__':
    inputfile = '../otherfiles/meidi_jd_pos.txt'  # 未分词
    outputfile1 = '../otherfiles/meidi_myPosRes_clean1.txt'  # 分词
    outputfile2 = '../otherfiles/meidi_myPosRes_clean2.txt'  # 去除停用词
    stoplist = '../otherfiles/stoplist.txt'

    part_word(inputfile,outputfile1)

    stop_word(outputfile1,stoplist,outputfile2)

    lda_ana(outputfile2)
