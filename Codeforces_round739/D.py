#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 21:14:35 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

 

def func(n, string):
    tp, sp, taken = 0, 0, 0
    
    while sp < len(n) and tp < len(string):
        if n[sp] == string[tp]:
            taken += 1
            tp += 1
        sp +=1
    
    m = len(n) - taken + len(string) - taken
    return m


def main():
    p = 1
    arr = []
    while p <= 2**18:
        arr.append(str(p))
        p *= 2
        
        
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = parse_input()
        ans = len(n) + 1
        for string in arr:
            ans = min(ans, func(n, string))
        print(ans)
        
if __name__ == "__main__":
    main()