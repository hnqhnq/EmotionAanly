# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 9:45
# @File    : extra_txt.py
# @Author  : hnq

def extra(filename,askfile,replyfile):
    with open(filename,'r',encoding='utf-8')as f:
        file=f.readlines()

    for i in range(0,len(file),2):
        with open(askfile,'a+',encoding='utf-8')as f1:
            f1.write(file[i])

    for j in range(1,len(file),2):
        print(file[j])
        with open(replyfile,'a+',encoding='utf-8')as f2:
            f2.write(file[j])

if __name__ == '__main__':
    extra(filename='sx_7.txt',askfile='a_7.txt',replyfile='r_7.txt')


