#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:48:53 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(n, m, i, j):
    
    if n != 1 and m != 1:
        if i == 1:
            x1, y1 = n, 1
            x2, y2 = n, m
        elif i == n:
            x1, y1 = 1, 1
            x2, y2 = 1, m
        elif j == 1:
            x1, y1 = 1, m
            x2, y2 = n, m
        elif j == m:
            x1, y1 = 1, 1
            x2, y2 = n, 1
        else:
            d1 = math.sqrt((i-1)**2 + (j-1)**2)
            d2 = math.sqrt((i-1)**2 + (j-m)**2)
            d3 = math.sqrt((i-n)**2 + (j-1)**2)    
            d4 = math.sqrt((i-n)**2 + (j-m)**2)
            amin = min(d1, d2, d3, d4)
            if amin == d1 or amin == d4:
                x1, y1 = 1, m
                x2, y2 = n, 1
            elif amin == d2 or amin == d3:
                x1, y1 = 1, 1
                x2, y2 = n, m

    elif n == 1 and m != 1:
        if j == 1:
            x1, y1 = 1, m
            x2, y2 = 1, 2
        elif j == n:
            x1, y1 = 1, 1
            x2, y2 = 1, 2
        else:
            x1, y1 = 1, m
            x2, y2 = 1, 1
        
    elif m == 1 and n != 1:
        if i == 1:
            x1, y1 = n, 1
            x2, y2 = 2, 1
        elif j == n:
            x1, y1 = 1, 1
            x2, y2 = n-1, 1
        else:
            x1, y1 = n, 1
            x2, y2 = 1, 1
            
    elif n == 1 and m == 1:
        return 1, 1, 1, 1
    return  x1, y1, x2, y2

a = func(1, 1, 1, 1)
def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n, m, i, j = [int(i) for i in parse_input().split()]
        print(*func(n, m, i, j))
        
if __name__ == "__main__":
    main()