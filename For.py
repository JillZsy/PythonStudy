#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:12:35 2019

@author: JillZsy
"""

from pandas import Series
from pandas import DataFrame

for i in range(10):
    print('i=',i)
    
for i in range(3, 10):
    print('i=',i)
    
#遍历字符串
for char in 'zxcvbnm':
    print (char)
    
#遍历数组
array = ['a', 'bb', 'ccc', 'dddd', 'eeeee']
for item in array:
    print (item)
    
#遍历序列
se = Series(['s', 23, False], index = ['aa', 'bb', 'cc'])
for value in se:
    print (value)
    
for index in se.index:
    print ('index=', index)
    print ('value=', se[index])
    print ('--'*5)
    
#遍历数据框
df = DataFrame({'age':Series([21, 22, 23]),
                'name':Series(['HanMeimei', 'LiLei', 'Lucy'])})
    
df1 = DataFrame({'age':Series([21, 22, 23], index=['aa', 'bb', 'cc']),
                'name':Series(['HanMeimei', 'LiLei', 'Lucy'], 
                              index=['aa', 'bb', 'cc'])})
    
#遍历列
for column in df:
    print ('列名：', column)
    print ('列中的值：', df[column])
    print ('--'*5)

#遍历行
    #1
for index in df1.index:
    print ('行：', index)
    print ('行的值：', df1.loc[index])
    print ('--'*5)
    
    #2
for value in df1.values:
    print (value)
    print (value[0])
    print (value[1])
    print ('--'*5)
    
    #3
for index, row in df.iterrows():
    print ('行：', index)
    print ('行的值：', row)
    print ('--'*5)
    
    

