# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 07:05:30 2019

@author: Stefan Draghici
"""

def searching(string):
    print('Searching string: {}'.format(string))
    while True:
        name=(yield)
        if string in name:
            print(name)
            
x=searching('hello')
x.__next__()
x.send('hello')