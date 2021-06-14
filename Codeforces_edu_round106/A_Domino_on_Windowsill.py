#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:29:16 2021

@author: hienpham
"""

import os
import math
import sys

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def func(n, k1, k2, w, b):
    
    total_cell = 2*n
    n_w_cell = k1 + k2
    n_b_cell = total_cell - n_w_cell
    
    dom_w_cell = 2 * w
    dom_b_cell = 2 * b
    
    if (n_w_cell >= dom_w_cell) & (n_b_cell >= dom_b_cell):
        answer = 'YES'
    else:
        answer = 'NO'
    return answer

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n, k1, k2 = [int(i) for i in parse_input().split()]
        w, b = [int(i) for i in parse_input().split()]
        print(func(n, k1, k2, w, b))
        
if __name__ == "__main__":
    main()