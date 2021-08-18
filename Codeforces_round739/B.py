#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 17:07:28 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(a, b, c):
    d = abs(a - b)
    n = 2 * d
    
    if c > n:
        return -1
    else:
        if a > n or b > n:
            return -1
        else:
            return c+d if c+d <= n else c-d
        



def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        a, b, c = [int(i) for i in parse_input().split()]
        print(func(a, b, c))
        
if __name__ == "__main__":
    main()