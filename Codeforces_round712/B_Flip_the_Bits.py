#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:23:09 2021

@author: hienpham
"""

import os
import math
import sys
from collections import Counter

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def flip_bits(bin_string):
    return ''.join('1' if x == '0' else '0' for x in bin_string)

def is_transformable(a, b, n):
    counts_a = Counter(a)

    if n == 2:
        if a == b:
            return 'YES'
        elif a[1] != b[1] and a[0] != b[0]:
            if a[0] != a[1]:
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'
            
    else:
        if a[-2::] == b[-2::]:
            
            return is_transformable(a[:-2], b[:-2], len(a[:-2]))
        else:
            if counts_a['0'] == counts_a['1']:
                new_a = flip_bits(a)
                return is_transformable(new_a[:-2], b[:-2], len(a[:-2]))
            else:
                return 'NO'

def func(a, b, n):
    if a == b:
        return 'YES'
    
    if n%2 == 0:
        return is_transformable(a, b, n)
    else:
        if a[-1] != b[-1]:
            return 'NO'
        else:
           return is_transformable(a[:-1], b[:-1], len(a[:-1]))



def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        a = parse_input()
        b = parse_input()
 
        print(func(a, b, n))
        
if __name__ == "__main__":
    main()