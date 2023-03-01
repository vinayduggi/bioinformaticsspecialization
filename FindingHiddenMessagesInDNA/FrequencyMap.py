#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:15:24 2020

@author: duggi
"""
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                    freq[Pattern] = freq[Pattern]+1
    return freq
Text = 'CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT'
k=3
print(FrequencyMap(Text, k))
