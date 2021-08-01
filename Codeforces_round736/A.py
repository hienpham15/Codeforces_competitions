#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:56:18 2021

@author: hienpham
"""
import os
import math
import sys
 
 
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")
 
 
def func(p):
    a = 2
    b = (p-1)//2
    
    if a != b:
        return a, b
    else:
        return a, p-1
 
#arr = [3, 1, 1, 1, 1, 10, 3, 10, 10, 1]
#n, k = 10, 3
#ans = func(n, k, arr)
 
def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        p = int(parse_input())
        ans =  func(p)
        print(' '.join(map(str, ans)))
        
if __name__ == "__main__":
    main()