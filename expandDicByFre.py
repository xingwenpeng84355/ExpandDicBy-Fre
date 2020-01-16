#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:57:51 2020

@author: xingwenpeng
"""

import ddr
import pandas as pd
import jieba
import csv

model, num_features, model_word_set=ddr.load_model("/Users/xingwenpeng/Desktop/csvdata/merge.model.bin") 

documents_path='/Users/xingwenpeng/Desktop/csvdata/SEED DICTIONARY.csv'

documents = open(documents_path, "r", encoding="utf-8").read()

words=list(jieba.cut(documents))

for i in words:
   if i == ' ' or i=='\n':
        words.remove(i)
print(words)

test=[]

for word in words:
    print(word)
    templist=model.most_similar(word,topn=100)
    for i in range(50):
        if templist[i][1]>0.5:
            print(templist[i][1])
            test.append(templist[i][0])

excel_out_put_path='/Users/xingwenpeng/Desktop/csvdata/expandedDic0.5.xlsx'
df = pd.DataFrame(test, columns=['expandedDic'])
df.to_excel(excel_out_put_path, index=False)