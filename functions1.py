# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:55:56 2019

@author: Stefan Draghici
"""

def education(status=None):
    if status=='I':
        status='qualified'
    print(status)
    
    
def selfie(name='Stefan', age=34, job='programmer'):
    print(name, age, job)
    

import functools

lst=[1,2,3,4,5,6,7]
print(functools.reduce(lambda a, b:a+b, lst))

def partial_func(a, s, d, y):
    return a+s+d+y

partial=functools.partial(partial_func, 4, 8, 88)
print(partial(8))