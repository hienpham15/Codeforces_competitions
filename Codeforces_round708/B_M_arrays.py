#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:43:56 2021

@author: hienpham
"""
import os
import math
import sys
from collections import Counter

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(array, n, m):
    mod = []
    for i in range(m + 1):
        mod.append(0)
        
    cum_Sum = 0
    
    for i in range(n):
        cum_Sum += array[i]
        mod[((cum_Sum % m) + m) % m] = mod[((cum_Sum % m) + m) % m] + 1
    
    result = 0
    
    for i in range(m):
        if (mod[i] > 1):
            result = result + (mod[i]*(mod[i] - 1))//2
        
    result += mod[0]
    return result


#s = [0, 3, 3, 2, 1, 1, 1, 7, 4, 7, 5]
#arr = func(s)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n, m = [int(i) for i in parse_input().split()]
        
        array = parse_input()
        
        result = func(array, n, m)
        print(result)
        
if __name__ == "__main__":
    main()