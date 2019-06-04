# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 07:25:09 2019

@author: Stefan Draghici
"""

def outside():
    def inside():
        print('inside')
    print('outside')
    inside()
    
outside()