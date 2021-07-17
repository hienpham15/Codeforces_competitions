#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 16:31:38 2021

@author: hienpham
"""

import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def isBinDec(n):
    n_s = str(n)
    for i in range(len(n_s)):
        if n_s[i] != '0' or n_s[i] != '1':
            return False
        
    return True


def func(n):
    ans = -math.inf
    n_s = str(n)
    
    for i in range(len(n_s)):
        ans = max(ans, int(n_s[i]))
    
    return ans


#ans = func(235)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        print(func(n))
        
        
if __name__ == "__main__":
    main()