# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:07:28 2019

@author: maxga
"""

import pythainlp 
import pythainlp.corpus 
with open("data.txt","r",encoding="utf-8-sig") as f:
    data=f.read() 
from collections import Counter
list_word=pythainlp.word_tokenize(data)
stop = set(pythainlp.corpus.stopwords.words('thai')) 
etcstop = [' ','\r\n','\n','1','2','3','4','5','6','7','8','9','0',':','!',
           '@','#','$','%','^','&','*','&','(',')','_','+',',','\t']
list_word=[i for i in pythainlp.word_tokenize(data) if i not in stop and i not in etcstop]
wordcont=Counter(list_word)#นับคำ
print(wordcont)