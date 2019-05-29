# -*- coding: utf-8 -*-
"""
Created on Wed May 29 06:46:27 2019

@author: Stefan Draghici
"""


class King:
    def __init__(self):
        print('constructor called with self.')
        self.name='Stefan'
        
    def instance_method(self):
        print('Instance method called: ', self.name)
        
    @classmethod
    def class_method(cls):
        print('Class method called.')
        
    @staticmethod
    def static_method():
        print('Static method called')
        
        
#test
k=King()
k.class_method()
k.static_method()
King.class_method()
King.static_method()