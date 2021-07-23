#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:46:01 2021

@author: hienpham
"""
import os
import math
import sys
from collections import Counter

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")



def func(s):
    n = len(s)
    if n < 2:
        return 0
    t_max = n//2
    
    chars = Counter(s)
    red, green = [], []
    for char, num in chars.items():
        if num >= 2:
            red.append(char)
            green.append(char)
        else:
            if len(red) > len(green):
                green.append(char)
            else:
                red.append(char)
    ans = min(len(red), len(green))
    return ans
 
#s = 'xyxx'
#ans = func(s)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        s = parse_input()
        print(func(s))
        
if __name__ == "__main__":
    main()