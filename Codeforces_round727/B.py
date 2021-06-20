#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 12:58:29 2021

@author: hienpham
"""
import os
import math
import sys
import string


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")



def func(song, l, r):
    sub_song = song[l-1:r]
    total = 0
    for char in sub_song:
        idx = string.ascii_lowercase.index(char)
        total += idx + 1
    return total

#s = 'abacaba'
#l, r = 2, 5 
#a = func(s, l, r)
def main():
    n, q = [int(i) for i in parse_input().split()]
    song = parse_input()
    for j in range(q):
        l, r = [int(i) for i in parse_input().split()]
        print(func(song, l, r))
         
if __name__ == "__main__":
    main()