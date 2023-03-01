#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:02:57 2020

@author: duggi
"""

def Reverse(Pattern):
    rev = ''
    for char in Pattern:
        rev = char+rev
    return rev