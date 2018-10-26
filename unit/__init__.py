""" 
@file: __init__.py.py
@Time: 2018/10/14
@Author:heningqiu
"""
import csv
import xlrd

def csvreader(filepath):
    outpath = open(filepath,'r',encoding='utf-8')
    reader = csv.reader(outpath,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    return reader,outpath

def csvwrite(filepath):
    infile = open(filepath,'w')
    writer = csv.writer(infile,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=False)
    return writer,infile

def xlsreader(filepath,sheetname):
    bk = xlrd.open_workbook(filepath)
    sh = bk.sheet_by_name(sheetname)
    return sh