# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#数据框
from pandas import DataFrame
df = DataFrame({
        'name':['LiLei', 'HanMeimei', 'Lucy'],
        'age':[18, 19, 20]
        })
df

df1 = DataFrame({
        'name':['LiLei', 'HanMeimei', 'Lucy'],
        'age':[18, 19, 20]
        }, index=['aa', 'bb', 'cc'])
df1

from pandas import Series
df2 = DataFrame({
        'age':Series([21, 22, 23], index=['aa', 'bb', 'cc']),
        'name':Series(['HanMeimei', 'LiLei', 'Lucy'], index=['aa', 'bb', 'cc'])})
df2

#按列访问
df['name']
#按行访问
df[0:2]
#按行列号访问:[行范围，列范围]
df.iloc[1:3, 0:2]
#按行索引，列名访问
df.at[1, 'name']
df1.at['bb', 'name']
#修改列名
df.columns = ['name1', 'age1']
df
df.columns = ['name', 'age']
#修改行索引
df.index = range(1,4)
df1.index = ['aaa', 'bbb', 'ccc']
#删除--axis:0 行、1 列  df不变，输出删除后新数据框
df.drop(1)  #axis 默认0
df.drop('age', axis=1) 
#删除列 df直接改变
del df['age']
#根据索引增加或修改行, 索引为已有时修改，索引不存在时添加
df.loc[4] = ['Lily', 14]
df.loc[2] = ['Lucky', 20]
#增加修改列， 列为已有时修改，不存在时添加
df['sex'] = ['male', 'female', 'male', 'female']
df['age'] = [20, 21, 22, 23]