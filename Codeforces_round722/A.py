#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:34:22 2021

@author: hienpham
"""


import os
import math
import sys
from collections import Counter

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")



def func(arr):
    n = len(arr)
    
    min_val = min(arr)
    counts = Counter(arr)
    max_del = n - counts[min_val]
    return max_del


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        arr = [int(i) for i in parse_input().split()]
        print(func(arr))
        
if __name__ == "__main__":
    main()