from sklearn.feature_extraction.text import TfidfVectorizer
from unit.__init__ import csvreader
import pandas as pd

# x,y=csvreader('../otherfiles/meidi_myPosRes_clean1.txt')
# print(x)
# for i in y:
#     print(i)

with open('../otherfiles/meidi_myPosRes_clean1.txt','r',encoding='utf-8')as f:
    re1=f.readlines()
with open('../otherfiles/stoplist.txt','r',encoding= 'utf-8')as s:
    stp=s.readlines()

vector=TfidfVectorizer(stop_words=stp)
tfidf=vector.fit_transform(re1)
# print(tfidf)

wordlist=vector.get_feature_names()#获取词袋模型中的所有词
# print(wordlist)
# for i in range(10):
#     print(wordlist[i])

# for i in tfidf:
#     print(i)
# for i in range(10):
#     for j in range(10):
#         print(wordlist[j],tfidf[i][j])

# tf-idf矩阵 元素a[i][j]表示j词在i类文本中的tf-idf权重
# weightlist=tfidf.toarray()
#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
# for i in range(len(weightlist)):
#     print('-------------第',i,'段文本的词语tf-idf权重')
#     for j in range(len(wordlist)):
#         print(wordlist[j],weightlist[i],[j])





