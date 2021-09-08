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
    l, r = 0, n - 1
    
    while l < r:
        sub = string[l:r+1]
        c = Counter(sub)
        if c['a'] == c['b']:
            return l, r
        elif c['a'] > c['b']:
            if string[l] == 'a':
                l += 1
            elif string[r] == 'a':
                r -= 1
            else:
                sub1 = string[l+1:r+1]
                l1, r1 = func(len(sub1), sub1)
                
                if l1 == -1 and r1 == -1:
                    sub2 = string[l:r]
                    l2, r2 = func(len(sub2), sub2)
                    if l2 == -1 and r2 == -1:
                        return -1, -1
                    else:
                        l2_n = string.find(string[l2:r2+1])
                        r2_n = l2_n + len(string[l2:r2+1]) - 1
                        return l2_n, r2_n
                else:
                    l1_n = string.find(string[l1:r1+1])
                    r1_n = l1_n + len(string[l1:r1+1]) - 1
                    return l1_n, r1_n
                    
        elif c['a'] < c['b']:
            if string[l] == 'b':
                l += 1
            elif string[r] == 'b':
                r -= 1
            else:
                sub1 = string[l+1:r+1]
                l1, r1 = func(len(sub1), sub1)
                
                if l1 == -1 and r1 == -1:
                    sub2 = string[l:r]
                    l2, r2 = func(len(sub2), sub2)
                    if l2 == -1 and r2 == -1:
                        return -1, -1
                    else:
                        l2_n = string.find(string[l2:r2+1])
                        r2_n = l2_n + len(string[l2:r2+1]) - 1
                        return l2_n, r2_n
                else:
                    l1_n = string.find(string[l1:r1+1])
                    r1_n = l1_n + len(string[l1:r1+1]) - 1
                    return l1_n, r1_n
    
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