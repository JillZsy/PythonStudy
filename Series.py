#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:09:32 2019

@author: JillZsy
"""

#序列
from pandas import Series

#创建
se = Series(['a', 'b', 'c', 1, 2, 3], index = ['aa', 'bb', 'cc', 'dd', 'ee', 'gg'])
se1 = Series(['a', 'b', 'c', 1, 2, 3])
#查询
se[4]
se[2:4]
se['ee']
#定位获取
se[[5,1,4]]
#只能追加序列
tmp = Series(['d'])
se = se.append(tmp)
print(se)
#不能直接追加元素
se.append('adgs')
#修改 
se[4] = 123
#删除  se不变，输出删除后新的序列
se2 = se.drop(0)
se3 = se.drop('bb')
se4 = se.drop(se.index[3])
se5 = se['b'!=se.values]
#判断是否存在
'a' in se.values