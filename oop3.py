# -*- coding: utf-8 -*-
"""
Created on Wed May 29 06:46:27 2019

@author: Stefan Draghici
"""

import abc

class MathOperation(abc.ABC):
    @abc.abstractmethod
    def sumation(self, a, b):
        pass
    
    @abc.abstractmethod
    def multiplication(self, a, b):
        pass
    
    
class ChildClass(MathOperation):
    def sumation(self, a, b):
        return a+b
    
    def multiplication(self, a, b):
        return a*b
    
    
#test
#m=MathOperation()
c=ChildClass()
print(c.sumation(4, 51))
print(c.multiplication(4, 51))