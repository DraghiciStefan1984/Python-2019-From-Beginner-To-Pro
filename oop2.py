# -*- coding: utf-8 -*-
"""
Created on Wed May 29 06:46:27 2019

@author: Stefan Draghici
"""

class Cat:
    def sound(self):
        print('Miau')
        
    def swim(self):
        print('a cat cannot swim')
        
        
class Duck:
    def sound(self):
        print('Mac')
        
    def swim(self):
        print('a duck can swim')
        
        
def animal_props(animal):
    animal.sound()
    animal.swim()
    
    
#test
c=Cat()
d=Duck()

animal_props(c)
animal_props(d)