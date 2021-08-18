#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:34:12 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def check(val):
    str_val = str(val)
    if val%3 != 0 and str_val[-1] != '3':
        return True
    else:
        False


def function(k, d):
    
    if k in d.keys():
        return d[k]
    else:
        val = list(d.keys())[-1]
        for i in range(val+1, k+1):
            flag = True
            
            c_val = d[i-1] + 1
            while flag:
                if check(c_val):
                    d[i] = c_val
                    flag = False
                else:
                    c_val += 1
        return d[k]

#k = 10
#d = {}
#d[1] = 1
#ans = function(k, d)

def main():
    n_cases = int(parse_input())
    d = {}
    d[1] = 1
    for i in range(n_cases):
        k = int(parse_input())
        print(function(k, d))
        
if __name__ == "__main__":
    main()