#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:53:47 2021

@author: hienpham
"""
import os
import math
import sys
import itertools

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(n, k, arr):
    max_val = -math.inf
    arr_id = [i for i in range(n)]
    comb = list(itertools.combinations(arr_id, 2))
    
    for r in range(len(comb)):
        i, j = comb[r]
        f_ij = (i+1)*(j+1) - k*(arr[i]|arr[j])
        max_val = f_ij if f_ij > max_val else max_val
    return max_val

#n, k = 6, 6
#arr = [3, 2, 0, 0, 5, 6]
#ans = func(n, k, arr)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n, k = [int(i) for i in parse_input().split()]
        arr = [int(i) for i in parse_input().split()]
        print(func(n, k, arr))
        
if __name__ == "__main__":
    main()