#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 14:23:43 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

    

def func(n, x, t):
    
    k = t//x
    m = n - k
    
    p1 = max(0, n - k)
    p2 = int(min(n - 1, k -1)*min(n, k)//2)
    ans = p1*k + p2
    #return int(ans)
    if n <= k:
        return int(n*(n - 1)//2)
    else:
        return int(k*(k - 1)//2) + (n - k)*k


ans_correct = 1999999998999999999

a = func(2000000000, 1, 1999999998)


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n, x, t = [int(i) for i in parse_input().split()]
        print(func(n, x, t))
        
if __name__ == "__main__":
    main()        