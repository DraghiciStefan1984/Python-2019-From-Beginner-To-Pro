# -*- coding: utf-8 -*-
"""
Created on Wed May 29 06:46:27 2019

@author: Stefan Draghici
"""

class Parent:
    def __init__(self):
        print('Calling Parent constructor...')
        
    def parent_method(self):
        print('calling parent method')
        
        
class Child(Parent):
    def __init__(self):
        print('Calling Child constructor...')
        
    def child_method(self):
        print('calling child method')
        
    def parent_method(self):
        print('calling child overriden parent method')
        
        
#test
p=Parent()
c=Child()

p.parent_method()
c.child_method()
c.parent_method()