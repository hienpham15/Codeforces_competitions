#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 17:21:43 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def function(k):
    
    a, x, i = 1, 1, 1
    
    while (k >= x + a):
        x += a
        a += 2
        i += 1
    m = k - x + 1
    if m <= i:
        return (m, i)
    else:
        return (i, i - (m - i))
    


def main():
    n_cases = int(parse_input())
    d = {}
    d[1] = (1, 1)
    for i in range(n_cases):
        k = int(parse_input())
        print(function(k, d))
        
if __name__ == "__main__":
    main()