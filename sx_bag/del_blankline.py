# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 9:08
# @File    : del_blankline.py
# @Author  : hnq

'''
python读取文件，将文件中的空白行去掉
'''

def delblankline(infile, outfile):
    infopen = open(infile, 'r', encoding="utf-8")
    outfopen = open(outfile, 'w', encoding="utf-8")

    lines = infopen.readlines()
    for line in lines:
        line = line.strip()
        if len(line) != 0:
            outfopen.writelines(line)
            outfopen.write('\n')
    infopen.close()
    outfopen.close()

if __name__ == '__main__':
    delblankline("sx7.txt", "sx_7.txt")


