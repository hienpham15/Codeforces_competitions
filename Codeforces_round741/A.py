#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:34:34 2021

@author: hienpham
"""

import os
import math
import sys



parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def func(l, r):
    if l==r:
        return 0
    
    if r//2 > l:
        if r%2 == 0:
            return r - (r//2 + 1)
        else:
            return r - ((r+1)//2)
    elif r//2 < l:
        return r%l
    elif r//2 == l:
        return r%(l+1)



def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        l, r = [int(i) for i in parse_input().split()]
        print(func(l, r))
        
if __name__ == "__main__":
    main()