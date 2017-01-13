# -*- coding: utf-8 -*-
'''
Created on 21 oct. 2016

@author: Andrés
'''

import suma
def empieza():
    print 6
    assert 6==5
    assert test()==11
    print suma(-5,-6)
def test():
    return 7+4

if __name__ == '__main__':
    empieza()