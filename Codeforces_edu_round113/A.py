#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:23:52 2021

@author: hienpham
"""

import os
import math
import sys
from collections import Counter


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")



def func(n, string):
    
    if len(string) < 2:
        return -1, -1
    
    for l in range(n-1):
        for r in range(l+1, n):
            sub = string[l:r+1]
            c = Counter(sub)
            if c['a'] == c['b']:
                return l, r
    return -1, -1

#n = 1
#s = 'a'
#l, r = func(n, s)


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        string = parse_input()
        l, r = func(n, string)
        if l == -1 and r == -1:
            print("{} {}".format(l, r))
        else:
            print("{} {}".format(l+1, r+1))

if __name__ == "__main__":
    main()