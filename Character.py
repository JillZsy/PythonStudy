#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:27:30 2019

@author: JillZsy
"""

#转义字符
print('I\'m Python')
#取消转义r
print('phone\name\age')
print(r'phone\name\age')
#续行
print('zxcv\
bnm')
#""".."""可跨越多行
print("""zxcv
bnm""")
#字符串连接
print('zxcv'+'bnm')
#字符串重复
print('hello'*5)

#索引
#从左往右，从0开始
#从右往左，从-1开始
str = 'abcdefghi'
print(str[0], str[5])
print(str[-9], str[-4])

str[1:5]
str[5:]
str[-8:-4]

#检测开头结尾
str.startswith('abc')
str.endswith('hi')

choice = ('abc', 'hi')
str.startswith(choice)
str.endswith(choice)

#查找字符串
str.find('e')
str.find('w')

#替换
text = 'to be or Not To Be, that is a question'
text.replace('to', 'not to')

#忽略大小写
import re
re.findall('to', text, flags=re.IGNORECASE)
re.sub('to', 'too', text, flags=re.IGNORECASE)

#拼接字符串
parts = ['a', 'b', 'c', 'd', 'e']
','.join(parts)