#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:49:08 2020

@author: duggi
"""

def Complement(Pattern):
  basepairs = {"A":"T", "T":"A", "G":"C", "C":"G"}
  complement = [basepairs[char] for char in Pattern]
  return "".join(complement)