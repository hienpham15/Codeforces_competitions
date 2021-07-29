#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:34:27 2021

@author: hienpham
"""

import os
import math
import sys
import itertools

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")
    

def func(n, arr):
    max_val = -math.inf
    arr_id = [i for i in range(n)]
    comb = list(itertools.combinations(arr_id, 2))
    
    for i in range(len(comb)):
        l, r = comb[i]
        f_lr = max(arr[l:r+1])*min(arr[l:r+1])
        max_val = f_lr if f_lr > max_val else max_val
    
    
    return max_val

n = 10
arr = [9, 6, 4, 4, 9, 5, 3, 7, 9, 9]
ans = func(n, arr)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        arr = [int(i) for i in parse_input().split()]
        print(func(n, arr))
        
if __name__ == "__main__":
    main()