#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:26:49 2019

@author: JillZsy
"""

#不带参数
def hello():
    print('Hello')
    
hello()

#带参数
def printUser(name, age):
    print(name, age)
    
printUser('HanMeimei', 21)
printUser(age = 21, name = 'HanMeimei')

#带默认参数
def printUser(name, age = 21):
    print(name, age)
    
printUser('HanMeimei')

#带可变参数
def printUser(name, *args):
    print(name)
    for arg in args:
        print(arg)
    return


