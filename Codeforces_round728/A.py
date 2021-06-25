#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 11:03:33 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(n):
    cat = []
    
    if n%2 == 0:
        pairs_2s = n//2
        pairs_3s = 0
        for i in range(pairs_2s):
            cat.append(2*(i + 1))
            cat.append(2*i + 1)
  
    elif n%2 != 0:
        pairs_2s = (n//2) - 1
        for i in range(pairs_2s):
            cat.append(2*(i + 1))
            cat.append(2*i + 1)
        cat.append((pairs_2s)*2 + 3)
        cat.append((pairs_2s)*2 + 1)
        cat.append((pairs_2s)*2 + 2)
        
    return cat
ans = func(21)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        ans = func(n)
        print(*ans)
        
if __name__ == "__main__":
    main()