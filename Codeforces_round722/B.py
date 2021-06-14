#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:55:42 2021

@author: hienpham
"""

import os
import math
import sys
from collections import Counter


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")



def func(arr):
    negatives = [val for val in arr if val <= 0]
    positives = [val for val in arr if val > 0]
    
    counts_all_neg = len(negatives)
    
    if not positives:
        counts = len(arr)
    elif not negatives:
        counts = 1
    else:
        unique_neg = set(negatives)
        
        supplement = set([val for val in positives if val < abs(min(negatives))])
        
        if supplement:
            counts = len(unique_neg) + 1
        else:
            counts = len(negatives)
    
    if counts_all_neg >= counts:
        return counts_all_neg
    else:
        return counts
"""
def creat_test(n):
    import numpy as np
    rand_int = np.random.randint(-10, 10, n)
    return rand_int


arr = creat_test(10)
ans = func(arr)
"""
def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        arr = [int(i) for i in parse_input().split()]
        print(func(arr))
        
if __name__ == "__main__":
    main()